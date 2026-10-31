# {{GPT_NAME}} – OpenCode

Version: {{VERSION}}

Detta är Brädspelsdesigners OpenCode-distribution, inte GPT Byggarens utvecklingsverktyg.

## Kom igång

1. Packa upp ZIP-filen i en egen arbetskatalog.
2. Öppna katalogen som workspace i OpenCode.
3. Läs `AGENTS.md` för gemensamma arbetsregler. Aktivera relevant Skill under `.opencode/skills/` vid behov.
4. Använd `knowledge/` som referensmaterial när uppgiften kräver det.
5. Arbeta med ett brädspelsprojekt i workspace eller i en underkatalog, till exempel `project/`. Håll strukturerade källor separerade från genererade filer.

## Skills

- `game-design` – spelidé, mekanik och prototyp.
- `rules-playtest` – regler, speltest och balansering.
- `print-and-play` – komponenter och utskrift.
- `project-lifecycle` – ZIP-projekt, ändringshistorik och release.

## Begränsningar

Denna version deklarerar inga egna körbara runtimeverktyg. OpenCode kan ha andra funktioner via sin värdmiljö, men ett script eller en PDF är inte automatiskt körbar/genererad enbart för att instruktionerna nämner den. `.opencode/runtime-contract.json` beskriver vad distributionen deklarerar. Inga GPT Byggaren-specifika `gpt_*`-verktyg ingår.
