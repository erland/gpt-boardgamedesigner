# Modulär Skill-uppdelning – Brädspelsdesigner 1.0.0

Originalbeteendet finns oförändrat i `assistant/instructions.md`. Ingen ny beteendekälla införs utöver `canonical/core.md` och fyra `canonical/skills/*/behavior.md`. Varje ursprungligt textstycke är tilldelat exakt en plats.

| Modul | Aktiviering och ansvar | Originalstycken (0-baserat) |
|---|---|---|
| core | Identitet, allmän metod, språk, övergripande förmågor, sanningsenlighet | 0, 1, 2, 3, 10, 16 |
| game-design | Aktiveras för spelidéer, spelkategori, kärnloop, mekanikkritik och nybörjarprototyper. | 4, 5, 17, 18 |
| rules-playtest | Aktiveras för regelbok, blindtest, speltest, balans och regeltydlighet. | 11, 14 |
| print-and-play | Aktiveras för komponentdesign, grafisk produktion och utskriftsunderlag. | 12, 13 |
| project-lifecycle | Aktiveras för ZIP-import, projektändring, käll-/outputhantering, versionshantering och release. | 6, 7, 8, 9, 15, 19 |

## Gränser
- **game-design:** idéval, spelmekanik och första prototyp; inte produktionslayout eller projektversioner.
- **rules-playtest:** spelregler, observationer och balans; inte tryckproduktion.
- **print-and-play:** komponentform, A4/A6 och tryck; inte speltestets beslut.
- **project-lifecycle:** ZIP, källor, status, versionshantering och release; inte själva speldesignbeslutet.

Kunskapsfiler är fördelade med explicit referenslista per Skill. Ingen separat runtime-skriptfunktion deklareras.

## Spårbarhets- och testkrav
1. De 20 originalstyckena motsvaras av 20 oförändrade stycken i core + Skills, exakt en gång.
2. Hela den historiska instruktionen bevaras byte-identiskt i `assistant/instructions.md`.
3. Originalmotorn 1.6.33 ska bygga och validera sex arkiv (projekt + fem distributioner); otestad host-paritet får inte markeras PASS.
4. Release förblir blockerad via `project-status.yaml`.

Detta är en arkitekturändring som måste verifieras i ren GitHub-checkout före merge.