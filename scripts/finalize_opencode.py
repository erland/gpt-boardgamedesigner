#!/usr/bin/env python3
"""Project-specific OpenCode projection after the pinned canonical engine build.

The canonical engine remains the builder. Rewrites only OpenCode AGENTS.md, then
reconciles the deterministic ZIP and the canonical delivery hashes.
"""
import hashlib
import json
from pathlib import Path
import zipfile

import yaml

ROOT = Path(__file__).resolve().parents[1]
FIXED_DATE = (2020, 1, 1, 0, 0, 0)

def sha(data):
    return hashlib.sha256(data).hexdigest()

def run():
    cfg = yaml.safe_load((ROOT / "gpt-project.yaml").read_text(encoding="utf-8"))
    assert cfg["instructions"]["mode"] == "modular_skills"
    core = (ROOT / cfg["instructions"]["core"]).read_text(encoding="utf-8").strip()
    definitions = cfg["skills"]["definitions"]
    build = ROOT / "build/opencode"
    agents = build / "AGENTS.md"
    old = agents.read_text(encoding="utf-8")
    # Refuse to patch an unknown build, or silently remove instructions.
    for skill in definitions:
        body = (ROOT / skill["source"]).read_text(encoding="utf-8").strip()
        assert body in old, f"original projection missing {skill['id']}"
        assert (build / ".opencode/skills" / skill["id"] / "SKILL.md").is_file()
    assert core in old, "original projection missing core"
    index = "\n".join(
        f"- \`{s['id']}\`: {s['description']} Läs \`.opencode/skills/{s['id']}/SKILL.md\` vid relevant uppgift."
        for s in definitions
    )
    new = (
        core + "\n\n## OpenCode – modulära Skills\n\n"
        "Detta workspace använder Brädspelsdesigner. Behåll gemensamma regler här och hämta endast relevant specialistbeteende från installerade Skills. "
        "Påstå inte att en Skill är aktiverad om värden inte exponerar den.\n\n"
        + index + "\n\n"
        "Arbeta i aktuell workspace; ange sökväg till underkatalog när ett separat spelprojekt bearbetas. "
        "Endast deklarerade runtimeverktyg får antas existera.\n"
    )
    agents.write_text(new, encoding="utf-8")
    assert all((ROOT / s["source"]).read_text(encoding="utf-8").strip() not in new for s in definitions), "duplicated Skill behavior"
    manifest_path = build / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entries = {item["path"]: item for item in manifest["files"]}
    assert "AGENTS.md" in entries
    agents_bytes = agents.read_bytes()
    entries["AGENTS.md"]["sha256"] = sha(agents_bytes)
    entries["AGENTS.md"]["size"] = len(agents_bytes)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    version = (build / "VERSION").read_text(encoding="utf-8").strip()
    zip_path = ROOT / "dist" / f"{cfg['project']['id']}-opencode-{version}.zip"
    assert zip_path.is_file(), f"canonical OpenCode ZIP missing: {zip_path}"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file in sorted(p for p in build.rglob("*") if p.is_file()):
            rel = file.relative_to(build).as_posix()
            info = zipfile.ZipInfo(rel, FIXED_DATE)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, file.read_bytes())
    sums_path = ROOT / "dist/SHA256SUMS.txt"
    archives = sorted((ROOT / "dist").glob("*.zip"))
    sums_path.write_text("".join(f"{sha(p.read_bytes())}  {p.name}\n" for p in archives), encoding="utf-8")
    delivery = ROOT / "dist/DELIVERY-MANIFEST.json"
    if delivery.exists():
        payload = json.loads(delivery.read_text(encoding="utf-8"))
        for item in payload.get("artifacts", []):
            path = ROOT / "dist" / item["file"]
            if path.is_file():
                item["sha256"] = sha(path.read_bytes())
                item["size"] = path.stat().st_size
        delivery.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    with zipfile.ZipFile(zip_path) as archive:
        assert archive.testzip() is None
        assert archive.read("AGENTS.md") == agents_bytes
    print(f"OpenCode: core + {len(definitions)} Skill pointers, no duplicate Skill body; ZIP and checksums updated")

if __name__ == "__main__":
    run()
