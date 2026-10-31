#!/usr/bin/env python3
"""Offline, deterministic preflight for G01 and G03 across the five packaged runtimes.

This verifies packaged instructions/resources, not generated answers or host behavior.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import zipfile

RUNTIMES = {
    "chat": ("START-HERE.md",),
    "plugin": ("plugin.json",),
    "claude-project": ("project/instructions.md",),
    "claude-skills": ("runtime-contract.json",),
    "opencode": ("AGENTS.md",),
}

def check_archive(path: Path, required: tuple[str, ...]) -> dict:
    result = {"archive": str(path), "zip_integrity": "FAIL", "entrypoints": "FAIL",
              "g01_host": "NOT VERIFIED", "g03_host": "NOT VERIFIED"}
    if not path.is_file():
        result["error"] = "archive missing"
        return result
    try:
        with zipfile.ZipFile(path) as archive:
            bad = archive.testzip()
            names = set(archive.namelist())
            result["zip_integrity"] = "PASS" if bad is None else "FAIL"
            missing = sorted(set(required) - names)
            result["entrypoints"] = "PASS" if not missing else "FAIL"
            if missing:
                result["missing"] = missing
            if bad:
                result["corrupt_entry"] = bad
    except (OSError, zipfile.BadZipFile) as exc:
        result["error"] = str(exc)
    return result

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dist", default="dist")
    parser.add_argument("--output", default="build/acceptance-preflight.json")
    args = parser.parse_args()
    dist = Path(args.dist)
    files = sorted(dist.glob("*.zip"))
    checks = {}
    for runtime, required in RUNTIMES.items():
        matches = [p for p in files if f"-{runtime}-" in p.name]
        if not matches:
            # Engine naming can vary: preserve an explicit NOT VERIFIED rather than guessing.
            checks[runtime] = {"archive": None, "zip_integrity": "NOT VERIFIED",
                               "entrypoints": "NOT VERIFIED", "g01_host": "NOT VERIFIED",
                               "g03_host": "NOT VERIFIED", "note": "No matching archive filename"}
        else:
            checks[runtime] = check_archive(matches[-1], required)
    report = {"scope": "offline-distribution-preflight", "checks": checks,
              "host_runtime_parity": "NOT VERIFIED", "release_ready": False}
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if any(c["zip_integrity"] == "FAIL" or c["entrypoints"] == "FAIL"
                    for c in checks.values()) else 0

if __name__ == "__main__":
    sys.exit(main())
