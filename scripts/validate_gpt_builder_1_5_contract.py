#!/usr/bin/env python3
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]

def main() -> int:
    errors=[]
    contract=yaml.safe_load((ROOT/"gpt-builder-1.5-contract.yaml").read_text(encoding="utf-8"))
    project=yaml.safe_load((ROOT/"gpt-project.yaml").read_text(encoding="utf-8"))
    canonical=(ROOT/project["instructions"]["canonical"]).read_bytes()
    legacy=(ROOT/project["instructions"]["legacy_source"]).read_bytes()
    text=canonical.decode("utf-8")
    version=(ROOT/"VERSION").read_text(encoding="utf-8").strip()

    if contract["builder"]["target_version"]!="1.5.0":
        errors.append("target builder version must be 1.5.0")
    if contract["builder"]["behavior_preserving"] is not True:
        errors.append("migration must remain behavior-preserving")
    if canonical!=legacy:
        errors.append("canonical instruction diverges from legacy instruction")
    if version!="1.0.0":
        errors.append(f"VERSION changed during migration: {version!r}")

    actual=sorted(p.name for p in (ROOT/"gpt-builder-upload").glob("*.md") if p.name!="README.md")
    if len(actual)!=16:
        errors.append(f"expected exactly 16 GPT Builder Knowledge files, found {len(actual)}")

    markers=[
        "spelbarhet före grafisk puts",
        "strukturerade källfiler före engångsfiler",
        "När användaren bifogar en zip ska du först inventera struktur",
        "uppdatera `PROJECT_STATUS.md` och `CHANGELOG.md`",
        "Föreslå testutskrift innan slutproduktion.",
        "Avråd från finbalans om kärnloop, mål eller regler ännu är oklara.",
        "Simuleringar ska alltid presenteras som hypoteser, inte facit.",
    ]
    for marker in markers:
        if marker not in text:
            errors.append(f"canonical instruction missing behavior marker: {marker}")

    b=contract["behavior"]
    checks={
        "iterative_workflow_required": True,
        "playability_before_graphic_polish": True,
        "structured_sources_before_one_off_outputs": True,
        "inventory_zip_before_editing": True,
        "source_first_editing": True,
        "update_status_and_changelog_on_project_changes": True,
        "prototype_before_fine_balance": True,
        "simulations_are_hypotheses_not_ground_truth": True,
        "beginner_mode_minimize_choices": True,
    }
    for key,value in checks.items():
        if b.get(key) is not value:
            errors.append(f"{key} must be {value}")

    if errors:
        print("GPT BUILDER 1.5 CONTRACT: FAIL")
        for e in errors: print("-",e)
        return 1
    print("GPT BUILDER 1.5 CONTRACT: PASS")
    print("VERSION 1.0.0; 16/16 Knowledge; zip/source/output/status/playtest behavior preserved")
    return 0

if __name__=="__main__":
    raise SystemExit(main())
