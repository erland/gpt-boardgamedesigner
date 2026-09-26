# Claude Projects och OpenCode – runtime compatibility

Projekt: **Brädspelsdesigner**  
GPT Byggaren: **1.5.0**

## Slutsats

Claude Projects och OpenCode bedöms olika.

- **OpenCode** bedöms som **equivalent candidate** eftersom dess workspace-/filorienterade arbetssätt kan matcha projekt-zip, strukturerad källredigering, validering och paketering.
- **Claude Projects** bedöms som **reduced candidate** eftersom instruktioner, Knowledge, analys och dokumentation kan mappas väl, men full parity för deterministisk filredigering, zip-paketering och build/validation-flöde inte kan antas.

Båda lämnas **not active** i denna migrering tills faktiska distributioner/adapterspecifikationer och regressionstester finns.

## Parity-bedömning

| Område | Claude Projects | OpenCode |
|---|---|---|
| Behavior | equivalent candidate | equivalent candidate |
| Capability | reduced | equivalent candidate |
| Artifact | reduced | equivalent candidate |
| Workspace/state | reduced | equivalent candidate |
| Tool | reduced | equivalent candidate |

## Kritiska regler som måste bevaras

Varje runtime måste så långt den aktiveras bevara:
- inventering av projekt-zip före ändring,
- källfiler framför genererad output,
- uppdatering av `PROJECT_STATUS.md` och `CHANGELOG.md`,
- print-and-play-principer,
- regelboksstruktur,
- playtest- och balansarbete,
- guidat nybörjarläge,
- release/build-arbetsflöde,
- 16/16 Knowledge-filer eller verifierat equivalent representation.

## Claude Projects

Styrkor:
- kan bära instruktioner, Knowledge och långvarigt projektunderlag,
- kan analysera regler, mekanik, komponenter och dokumentation.

Begränsning:
- full parity för att faktiskt ändra ett helt projektträd, köra validering/build och paketera en uppdaterad zip kan inte tas för given.

Beslut:
- compatibility: `reduced`
- activation: `not_active`
- blocker: `deterministic_file_edit_build_and_zip_parity_not_guaranteed`

## OpenCode

Workspace-, fil- och kodorienteringen matchar projektets kärnflöde väl:
- inventera projekt,
- redigera markdown/YAML/JSON/scripts,
- köra validering,
- generera output,
- uppdatera status/changelog,
- paketera projekt.

Beslut:
- compatibility: `equivalent`
- activation: `not_active`
- blocker: `distribution_and_regression_not_implemented`

## Aktiveringsregel

En runtime får aktiveras först när:
1. canonical instruktion paketeras deterministiskt,
2. 16/16 Knowledge-filer eller verifierat equivalent representation ingår,
3. projekt-zip-inventering verifieras,
4. source-vs-output-regeln regressionstestas,
5. status/changelog-uppdatering verifieras,
6. print-and-play, regelbok och playtestregler verifieras,
7. faktisk filändring, validering och paketering testas för den runtime som ska få full parity,
8. distributionen byggs och valideras i CI.

Ingen canonical produktregel ändras av denna bedömning.
