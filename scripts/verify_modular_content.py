#!/usr/bin/env python3
"""Check that source behavior excerpts survive packaging; not a host behavior test."""
import json
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
NATIVE = {
    "plugin": ROOT / "build/plugin/skills",
    "claude_skills": ROOT / "build/claude-skills/skills",
    "opencode": ROOT / "build/opencode/.opencode/skills",
}
FALLBACK = {
    "chat": ROOT / "build/chat/assistant/instructions.md",
    "claude_project": ROOT / "build/claude/project/instructions.md",
}
def compact(s):
    return " ".join(s.split())

def markers(file):
    paragraphs = [compact(p) for p in file.read_text(encoding="utf-8").split("\n\n")]
    return [p[:110] for p in paragraphs if len(p) >= 45][:2]

def main():
    report = {"level": "packaged-content", "runtime_host_parity": "NOT VERIFIED",
              "release_ready": False, "results": {}}
    failures = []
    for skill in CONFIG["skills"]["definitions"]:
        sid = skill["id"]
        source = ROOT / skill["source"]
        probes = markers(source)
        if not probes:
            failures.append(f"{sid}: no meaningful source markers")
            continue
        for runtime, base in NATIVE.items():
            target = base / sid / "SKILL.md"
            ok = target.is_file() and all(p in compact(target.read_text(encoding="utf-8")) for p in probes)
            report["results"][f"{runtime}/{sid}"] = "PASS" if ok else "FAIL"
            if not ok:
                failures.append(f"{runtime}/{sid}: behavior excerpt missing")
        for runtime, target in FALLBACK.items():
            if not target.is_file():
                report["results"][f"{runtime}/{sid}"] = "FAIL"
                failures.append(f"{runtime}/{sid}: compiled instructions missing")
            else:
                text = compact(target.read_text(encoding="utf-8"))
                ok = all(p in text for p in probes)
                report["results"][f"{runtime}/{sid}"] = "PASS" if ok else "NOT VERIFIED"
                # Fallback may summarize source; missing exact text is a review item, not a false PASS.
    out = ROOT / "build/modular-content-evidence.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if failures:
        print("CONTENT CHECK: FAIL (" + "; ".join(failures) + ")", file=sys.stderr)
        return 1
    print("CONTENT CHECK: PASS for native Skills; fallback findings require review")
    return 0

if __name__ == "__main__":
    sys.exit(main())
