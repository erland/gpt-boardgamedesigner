#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")
KNOWLEDGE_DIR = ROOT / "gpt-builder-upload"
FINAL_DIR = ROOT / "gpt-final-config"
PREFLIGHT_DIR = ROOT / "preflight"

EXPECTED_KNOWLEDGE = [
    "01-gpt-role-and-working-style.md",
    "02-boardgame-project-standard.md",
    "03-component-design-guide.md",
    "04-game-category-patterns.md",
    "05-print-and-play-production-guide.md",
    "06-rulebook-structure-standard.md",
    "07-playtest-and-balancing-guide.md",
    "08-example-project-pattern.md",
    "09-mechanics-and-balance-patterns.md",
    "10-blindtest-and-rule-clarity-guide.md",
    "11-component-economy-and-production-tradeoffs.md",
    "12-llm-boardgame-design-workflow.md",
    "13-existing-game-analysis-framework.md",
    "14-first-time-designer-guided-workflow.md",
    "15-release-and-build-workflow.md",
    "KNOWLEDGE_INDEX.md",
]


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--output-dir", default="dist")
    p.add_argument("--version", help="Explicit package version, e.g. 1.1.0. Defaults to VERSION file.")
    return p.parse_args()


def resolve_version(explicit: str | None) -> str:
    version = explicit or (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if version.startswith("v"):
        version = version[1:]
    if not SEMVER.fullmatch(version):
        raise SystemExit(f"Invalid version: {version!r}. Expected SemVer without leading v.")
    return version


def validate_sources() -> None:
    required = [
        FINAL_DIR / "final-instructions-under-8000-chars.md",
        FINAL_DIR / "final-conversation-starters.md",
        FINAL_DIR / "final-gpt-configuration.md",
        FINAL_DIR / "recommended-capabilities.md",
        PREFLIGHT_DIR / "COPY_TO_GPT_BUILDER.md",
        ROOT / "portable" / "START-HERE.md",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.is_file()]
    actual = sorted(p.name for p in KNOWLEDGE_DIR.glob("*.md") if p.name != "README.md")
    if sorted(EXPECTED_KNOWLEDGE) != actual:
        raise SystemExit(f"Knowledge set mismatch. Expected {EXPECTED_KNOWLEDGE}, got {actual}")
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_manifest(base: Path, version: str) -> None:
    files = []
    for p in sorted(base.rglob("*")):
        if p.is_file() and p.name != "MANIFEST.json":
            files.append({"path": p.relative_to(base).as_posix(), "sha256": sha256(p), "size": p.stat().st_size})
    manifest = {
        "package": "bradspelsdesigner",
        "format": "portable-chat-assistant",
        "version": version,
        "entrypoint": "START-HERE.md",
        "instructions": "assistant/instructions.md",
        "knowledge_index": "knowledge/KNOWLEDGE_INDEX.md",
        "files": files,
    }
    (base / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def zip_tree(src: Path, dest: Path) -> None:
    # Deterministic ZIP: fixed timestamps, modes and sorted path order.
    with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in sorted(src.rglob("*")):
            if not p.is_file():
                continue
            rel = p.relative_to(src).as_posix()
            info = zipfile.ZipInfo(rel, (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            zf.writestr(info, p.read_bytes())


def build_custom(stage: Path, version: str) -> None:
    (stage / "VERSION").write_text(version + "\n", encoding="utf-8")
    copy_file(ROOT / "README.md", stage / "README.md")
    copy_file(PREFLIGHT_DIR / "COPY_TO_GPT_BUILDER.md", stage / "COPY_TO_GPT_BUILDER.md")
    for name in [
        "final-instructions-under-8000-chars.md",
        "final-conversation-starters.md",
        "final-gpt-configuration.md",
        "recommended-capabilities.md",
    ]:
        copy_file(FINAL_DIR / name, stage / "gpt-final-config" / name)
    for name in EXPECTED_KNOWLEDGE + ["README.md"]:
        copy_file(KNOWLEDGE_DIR / name, stage / "gpt-builder-upload" / name)


def build_portable(stage: Path, version: str) -> None:
    (stage / "VERSION").write_text(version + "\n", encoding="utf-8")
    copy_file(ROOT / "portable" / "START-HERE.md", stage / "START-HERE.md")
    copy_file(FINAL_DIR / "final-instructions-under-8000-chars.md", stage / "assistant" / "instructions.md")
    copy_file(FINAL_DIR / "final-conversation-starters.md", stage / "assistant" / "conversation-starters.md")
    for name in EXPECTED_KNOWLEDGE:
        copy_file(KNOWLEDGE_DIR / name, stage / "knowledge" / name)
    write_manifest(stage, version)


def main() -> int:
    args = parse_args()
    version = resolve_version(args.version)
    validate_sources()
    out = (ROOT / args.output_dir).resolve() if not Path(args.output_dir).is_absolute() else Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)
    for old in out.glob("bradspelsdesigner-*-v*.zip"):
        old.unlink()
    with tempfile.TemporaryDirectory() as td:
        temp = Path(td)
        custom = temp / "custom"
        portable = temp / "portable"
        custom.mkdir(); portable.mkdir()
        build_custom(custom, version)
        build_portable(portable, version)
        custom_zip = out / f"bradspelsdesigner-custom-gpt-v{version}.zip"
        portable_zip = out / f"bradspelsdesigner-chat-v{version}.zip"
        zip_tree(custom, custom_zip)
        zip_tree(portable, portable_zip)
    print(f"Built {custom_zip}")
    print(f"Built {portable_zip}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
