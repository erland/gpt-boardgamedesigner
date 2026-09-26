# OpenAI Plugin – compatibility assessment

Projekt: **Brädspelsdesigner**  
GPT Byggaren: **1.5.0**

## Slutsats

OpenAI Plugin bedöms som **reduced candidate**, med **skills-first** arkitektur, och lämnas **not active** i denna migrering.

Brädspelsdesignerns designmetodik, regelstruktur, print-and-play-principer, playtest/balans, nybörjarläge och release/build-guidance lämpar sig väl för skills. Däremot är full produktparity beroende av mer än instruktioner och kunskap: projektet kräver också faktisk hantering av projektträd, filredigering, validering, output-generering och zip-paketering.

Det innebär att pluginen kan bära en stor del av arbetsflödet, men full parity får inte deklareras innan ett faktiskt fil-/artifact-flöde är implementerat och regressionstestat.

## Parity-bedömning

| Område | Bedömning |
|---|---|
| Behavior | equivalent candidate |
| Capability | reduced |
| Artifact | reduced |
| Workspace/state | reduced |
| Tool | reduced |

## Skills-first upplägg

En framtida Plugin v1 bör minst ha skills för:
- spelidé och kärnloop,
- kategori- och mekanikval,
- projektinventering,
- regelboksstruktur,
- komponentdesign,
- print-and-play-produktion,
- playtestplanering,
- balansanalys,
- blindtest och regeltydlighet,
- guidat nybörjarläge,
- release/build-guidance,
- existing-game analysis,
- component economy och production tradeoffs.

## Kritiska regler som måste bevaras

- spelbarhet före grafisk puts,
- strukturerade källfiler före engångsfiler,
- små iterationer före stora omtag,
- inventering av projekt-zip före ändring,
- källa framför genererad output,
- uppdatering av `PROJECT_STATUS.md` och `CHANGELOG.md`,
- testutskrift före slutproduktion,
- prototyp/playtest före finbalans,
- simuleringar som hypoteser, inte facit,
- 16/16 Knowledge-filer eller verifierat equivalent representation.

## Fil- och artifact-begränsning

Full parity kräver att plugin-runtime eller anslutna verktyg faktiskt kan:
1. läsa ett komplett projektträd eller zip,
2. identifiera canonical källfiler,
3. ändra markdown/YAML/JSON/scripts,
4. köra validering/build,
5. generera relevanta output-filer,
6. uppdatera `PROJECT_STATUS.md` och `CHANGELOG.md`,
7. paketera ett uppdaterat projekt deterministiskt.

Utan detta ska pluginen betraktas som design-/coachnings- och analyskapabel, men inte fullvärdig ersättare för Chat/Custom GPT-flödet.

## Aktiveringsbeslut

- status: `assessed_not_active`
- compatibility: `reduced`
- architecture: `skills_first`
- activation: `not_active`
- blocker: `deterministic_file_edit_build_and_zip_parity_not_implemented`

Ingen Plugin-distribution byggs eller publiceras i denna migrering.

## Aktiveringsregel

Plugin får aktiveras först när:
1. skills-strukturen är implementerad,
2. canonical instruktion och 16/16 Knowledge representeras deterministiskt,
3. projekt-zip-inventering verifieras,
4. source-vs-output-regeln regressionstestas,
5. status/changelog-uppdatering verifieras,
6. print-and-play, regelbok och playtestregler verifieras,
7. faktisk filändring, build/validation och zip-paketering verifieras,
8. plugin-distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
