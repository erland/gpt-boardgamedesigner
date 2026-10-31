# Knowledge-paketering och migration till GPT Byggaren 1.6.33

Datum: 2026-10-31. Projektversion: 1.0.0.

## Genomförd korrigering
Projektets Skill `boardgame-design` refererar nu explicit till de 15 kanoniska Knowledge-filerna under `knowledge/`. Tidigare var listan tom. Källfilerna har inte modifierats.

## Verifierat i lokal, fullständig migrerad projektkopia
- Originalbyggare 1.6.33: PASS (alla fem distributioner och projektarkiv).
- Kanonisk distributionsvalidator: PASS.
- Kanonisk lint: 0 errors, 207 warnings.
- Plugin: 15/15 referenser finns och är SHA-256-identiska med originalen, ZIP CRC PASS.
- Claude Skills: 15/15 referenser finns och är SHA-256-identiska med originalen, ZIP CRC PASS.
- Chat, Claude Projects, OpenCode: ZIP CRC PASS.
- Funktionella värdmiljötester: NOT VERIFIED.

## Repository-status och begränsning
**Denna PR är ännu inte hela projektmigreringen.** Den innehåller den kanoniska Knowledge-korrigeringen i `gpt-project.yaml`, men repo saknar fortfarande genererade/migrerade stödresurser som `schemas/skill-contract.schema.json` och motorns nya projektprofil, build- och CI-anpassning. Komplett byggt projekt och distributionerna levereras som ZIP separat i ChatGPT-konversationen.

Denna PR är därför **DRAFT / NOT READY TO MERGE**. Komplettera med alla saknade migrationsfiler, kör samma verifieringskommandon i ren checkout och gör värdmiljötester innan release.

### Exakta verifieringskommandon (med separat originalmotor)
```sh
python /path/to/engine/scripts/lint_gpt_project.py --project-root .
python /path/to/engine/scripts/build_distributions.py --project-root . --version 1.0.0
python /path/to/engine/scripts/validate_distributions.py --project-root .
```
