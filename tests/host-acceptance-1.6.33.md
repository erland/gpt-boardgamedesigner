# Funktionell acceptans – Brädspelsdesigner 1.0.0 (motor 1.6.33)

## Omfattning
Fem aktiva distributioner: Chat, OpenAI Plugin, Claude Projects, Claude Skills och OpenCode.

Bygge och lint är **inte** funktionella tester. Kör testerna i en faktisk värdmiljö och bifoga fullständiga transkript, genererade filer och eventuella felmeddelanden. Resultatet är NOT VERIFIED tills evidens har granskats.

## Sex kärnscenarier
| ID | Prompt / uppgift | Acceptanskriterier |
| --- | --- | --- |
| G01 | Skapa ett enkelt print-and-play-brädspel för 7–10-åringar, 2–4 spelare, 20 minuter, A4. | Sammanhängande spelloop, materiallista, spelplan/komponenter, regelutkast och speltestförslag; inga falska påståenden om färdiga filer. |
| G02 | Jämför ett kortspel och ett kartbaserat brädspel för samma idé. | Redovisa avvägningar kring komponentantal, kostnad, komplexitet och återspelbarhet, med rekommendation. |
| G03 | Importera ett befintligt spelprojekt som ZIP, inventera innehåll och föreslå nästa steg. | Bevarar källor och status; skiljer saknade från befintliga filer; förklarar värdmiljöns begränsningar. |
| G04 | Skriv kompletta regler för ett spel med 3 spelare, turordning, resurser och poäng. | Uppställning, turflöde, avslut, vinstvillkor och specialfall täcks. |
| G05 | Analysera speltestresultat: en strategi vinner 8 av 10 provomgångar. | Motiverade hypoteser, förbättringsförslag och plan för omtest; inga oberättigade säkerhetsanspråk. |
| G06 | Gör en produktionskandidat av ett prototypspel. | Kontroll av komponenter, utskriftsmått, regler, versioner och manifest; ingen Production Ready utan fullständig evidens. |

## Protokoll
För varje kombination av runtime och scenario (30 testfall):
- Lagra datum, värd/version, prompt, fullständigt svar och skapade artefakter.
- Granska varje kriterium, inklusive korrekta uppgifter om filverktyg och begränsningar.
- Sätt PASS, FAIL eller NOT VERIFIED med en konkret evidensreferens.
- Markera eventuella värdberoende begränsningar och dokumentera fallback.

## Releasebeslut
Den tekniska CI-kedjan är godkänd enligt GitHub Actions #45. Funktionsparitet är **NOT VERIFIED** tills testen ovan utförts. Uppdatera inte `migration.runtime_host_parity` eller `migration.release_ready` enbart på grund av denna testplan.

Pröva först G01 och G03 i varje värd. De testar kärnbeteende samt fil-/ZIP-stöd och kan avslöja större skillnader tidigt.
