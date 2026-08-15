#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
EXPECTED_KNOWLEDGE = [
    "01-gpt-role-and-working-style.md", "02-boardgame-project-standard.md", "03-component-design-guide.md",
    "04-game-category-patterns.md", "05-print-and-play-production-guide.md", "06-rulebook-structure-standard.md",
    "07-playtest-and-balancing-guide.md", "08-example-project-pattern.md", "09-mechanics-and-balance-patterns.md",
    "10-blindtest-and-rule-clarity-guide.md", "11-component-economy-and-production-tradeoffs.md",
    "12-llm-boardgame-design-workflow.md", "13-existing-game-analysis-framework.md",
    "14-first-time-designer-guided-workflow.md", "15-release-and-build-workflow.md", "KNOWLEDGE_INDEX.md",
]

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--dist-dir", default="dist")
    p.add_argument("--version")
    return p.parse_args()

def h(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def resolve_version(explicit):
    v = explicit or (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if v.startswith("v"): v = v[1:]
    if not SEMVER.fullmatch(v): raise SystemExit(f"Invalid version {v!r}")
    return v

def read_zip(path: Path):
    with zipfile.ZipFile(path) as z:
        bad = z.testzip()
        if bad: raise SystemExit(f"Corrupt ZIP {path}: {bad}")
        return {n: z.read(n) for n in z.namelist() if not n.endswith("/")}

def main():
    a = parse_args(); v = resolve_version(a.version)
    d = (ROOT / a.dist_dir).resolve() if not Path(a.dist_dir).is_absolute() else Path(a.dist_dir)
    cz = d / f"bradspelsdesigner-custom-gpt-v{v}.zip"
    pz = d / f"bradspelsdesigner-chat-v{v}.zip"
    if not cz.is_file() or not pz.is_file(): raise SystemExit("Expected distribution ZIPs are missing")
    c = read_zip(cz); p = read_zip(pz)
    if c.get("VERSION") != (v + "\n").encode(): raise SystemExit("Custom VERSION mismatch")
    if p.get("VERSION") != (v + "\n").encode(): raise SystemExit("Portable VERSION mismatch")
    src_instr = (ROOT / "gpt-final-config/final-instructions-under-8000-chars.md").read_bytes()
    src_starters = (ROOT / "gpt-final-config/final-conversation-starters.md").read_bytes()
    if c.get("gpt-final-config/final-instructions-under-8000-chars.md") != src_instr: raise SystemExit("Custom instructions changed")
    if p.get("assistant/instructions.md") != src_instr: raise SystemExit("Portable instructions changed")
    if c.get("gpt-final-config/final-conversation-starters.md") != src_starters: raise SystemExit("Custom starters changed")
    if p.get("assistant/conversation-starters.md") != src_starters: raise SystemExit("Portable starters changed")
    for name in EXPECTED_KNOWLEDGE:
        src = (ROOT / "gpt-builder-upload" / name).read_bytes()
        if c.get(f"gpt-builder-upload/{name}") != src: raise SystemExit(f"Custom knowledge changed: {name}")
        if p.get(f"knowledge/{name}") != src: raise SystemExit(f"Portable knowledge changed: {name}")
    manifest = json.loads(p["MANIFEST.json"].decode("utf-8"))
    if manifest["version"] != v: raise SystemExit("Manifest version mismatch")
    for e in manifest["files"]:
        if e["path"] not in p: raise SystemExit(f"Manifest path missing: {e['path']}")
        if h(p[e["path"]]) != e["sha256"]: raise SystemExit(f"Manifest hash mismatch: {e['path']}")
    print(f"OK: distributions validated for {v}; Custom GPT behavior files are byte-identical to source.")
    return 0
if __name__ == "__main__": raise SystemExit(main())
