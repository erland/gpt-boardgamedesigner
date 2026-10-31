#!/usr/bin/env python3
"""Validate explicit modular Skill packaging against the canonical GPT project model."""
from pathlib import Path
import argparse
import sys
import yaml

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--project-root", default=".")
    args = p.parse_args()
    root = Path(args.project_root).resolve()
    cfg = yaml.safe_load((root / "gpt-project.yaml").read_text(encoding="utf-8"))
    errors = []
    instr = cfg.get("instructions", {})
    skills = cfg.get("skills", {})
    if instr.get("mode") != "modular_skills":
        errors.append("instructions.mode must equal modular_skills")
    if skills.get("mode") != "explicit":
        errors.append("skills.mode must equal explicit")
    core = root / instr.get("core", "__missing__")
    if not core.is_file():
        errors.append("missing canonical core")
    defs = skills.get("definitions", [])
    ids = [item["id"] for item in defs]
    if not defs or len(ids) != len(set(ids)):
        errors.append("skills must be defined with unique IDs")
    for item in defs:
        sid = item["id"]
        source = root / item["source"]
        if not source.is_file():
            errors.append(f"{sid}: missing canonical behavior source")
            continue
        for ref in item.get("references", []):
            if not (root / ref).is_file():
                errors.append(f"{sid}: missing source reference {ref}")
        for target, base in (
            ("plugin", root / "build/plugin/skills"),
            ("claude-skills", root / "build/claude-skills/skills"),
            ("opencode", root / "build/opencode/.opencode/skills"),
        ):
            dest = base / sid
            skillfile = dest / "SKILL.md"
            if not skillfile.is_file():
                errors.append(f"{target}: missing {sid}/SKILL.md")
                continue
            content = skillfile.read_text(encoding="utf-8")
            if not content.strip() or f"name: {sid}" not in content:
                errors.append(f"{target}: invalid {sid} SKILL metadata")
            for ref in item.get("references", []):
                if not (dest / "references" / Path(ref).name).is_file():
                    errors.append(f"{target}: missing {sid} reference {ref}")
    if errors:
        print("MODULAR SKILLS PACKAGING: FAIL")
        for error in errors:
            print("- " + error)
        return 1
    print(f"MODULAR SKILLS PACKAGING: PASS ({len(defs)} skills, 3 native-skill distributions)")
    print("Chat/Claude Project textual fallbacks and functional host parity NOT VERIFIED by this check")
    return 0

if __name__ == "__main__":
    sys.exit(main())
