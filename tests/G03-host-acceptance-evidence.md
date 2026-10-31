# G03 – värdmiljöacceptans med faktisk fixture

## Verifierad utgångspunkt
PR #15 mergad. GitHub Actions run #53 (2026-10-31) är **SUCCESS**. Stegen `G03 project ZIP inventory fixture tests`, `Export G03 host-test ZIP fixture` och `G01/G03 offline distribution preflight` är godkända.

Den faktiska testfixturen finns som Actions-artefakt:
https://github.com/erland/gpt-boardgamedesigner/actions/runs/41234713713/artifacts/13054493350

Hämta `G03-stjarnstigen-project.zip` och `G03-expected-inventory.json` ur artefakten. Facit är baserat på fixturens faktiska filer.

## Test i respektive värd
Installera den aktuella distributionen (Chat, Plugin, Claude Projects, Claude Skills eller OpenCode). Kör samma prompt och bifoga ZIP-filen utan modifiering:

> Importera den bifogade spelprojekt-ZIP:en. Inventera exakt vilka filer som finns och identifiera README.md, PROJECT_STATUS.md och CHANGELOG.md. Skilj källfiler från genererad output. Redovisa projektets status, osäkerheter och föreslå 3–5 konkreta nästa steg. Ändra inga originalfiler. Om du inte kan öppna ZIP:en ska du säga det explicit.

## Bedömning (G03)
För **PASS** måste faktisk modellrespons med evidens visa:
1. Alla 7 filer korrekt inventerade utan påhittade filer.
2. `README.md`, `PROJECT_STATUS.md` och `CHANGELOG.md` korrekt identifierade.
3. `docs/rules.md`, `data/cards.json`, `assets/board.svg` som källfiler, och `output/board.pdf` som genererad output.
4. Prototypstatus korrekt återgiven från `PROJECT_STATUS.md`.
5. 3–5 praktiska nästa steg, utan att förändra originalfiler.
6. Begränsning rapporterad om värden inte kan läsa ZIP-filer.

Om ett krav inte uppfylls: **FAIL** med konkret fel. Om test inte körts eller transkript saknas: **NOT VERIFIED**. En väl beskriven begränsning är inte ett PASS på faktisk ZIP-import.

## Evidens
Registrera ett utfall per runtime i `tests/evidence/G03-host-results.csv`, och länka transkript, modellversion, eventuella artefakter och bedömning. Länkar till befintliga filer ska vara verifierbara. Skapa aldrig fiktiva PASS-resultat.

Releasebeslutet kvarstår `migration.runtime_host_parity: not_verified` och `migration.release_ready: false` tills tester på riktigt genomförts och granskats.
