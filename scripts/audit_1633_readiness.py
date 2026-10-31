#!/usr/bin/env python3
"""Deterministic source-tree readiness audit for GPT Byggaren 1.6.33.

An audit only: intentionally does not claim a build or host-runtime PASS.
"""
from __future__ import annotations

import json
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
ENGINE_VERSION = "1.6.33"
TARGETS = ("chat", "plugin", "claude_project", "claude_skills", "opencode")
REQUIRED = (
    "gpt-project.yaml",
    "schemas/skill-contract.schema.json",
    "schemas/capability-contract.schema.json",
    "schemas/tool-contract.schema.json",
    "schemas/workspace-state-contract.schema.json",
    "scripts/build_distributions.py",
    "scripts/validate_distributions.py",
    "assistant/instructions.md",
    "project-status.yaml",
)
report = {"engine_target": ENGINE_VERSION, "missing_paths": [], "missing_knowledge": [],
          "runtime_targets": {}, "legacy_workflow": False, "ready_for_1633_build": False}
for name in REQUIRED:
    if not (ROOT / name).is_file():
        report["missing_paths"].append(name)
try:
    config = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    if not isinstance(config, dict):
        raise ValueError("gpt-project.yaml must contain a mapping")
    for item in config.get("skills", {}).get("definitions", []):
        for path in item.get("references", []):
            if not (ROOT / path).is_file():
                report["missing_knowledge"].append(path)
    runtime = config.get("runtime", {})
    for target in TARGETS:
        key = {"claude_project": "claude", "claude_skills": "claude"}.get(target, target)
        entry = runtime.get(key, {})
        report["runtime_targets"][target] = bool(entry.get("enabled")) if isinstance(entry, dict) else False
except (OSError, ValueError, yaml.YAMLError) as exc:
    report["parse_error"] = str(exc)
workflow = ROOT / ".github/workflows/build-distributions.yml"
if workflow.exists():
    text = workflow.read_text(encoding="utf-8")
    report["legacy_workflow"] = ("1.5" in text or "validate_gpt_builder_1_5" in text)
report["ready_for_1633_build"] = (
    not report["missing_paths"]
    and not report["missing_knowledge"]
    and not report.get("parse_error")
    and all(report["runtime_targets"].values())
    and not report["legacy_workflow"]
)
print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
# Audit mode reports gaps without failing the existing 1.5 build.
if "--strict" in sys.argv and not report["ready_for_1633_build"]:
    sys.exit(1)
