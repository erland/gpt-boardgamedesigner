# Kör G03 med en faktisk test-ZIP

Hämta Actions-artefakten `G03-host-fixture` från byggkörningen. Den innehåller:
- `G03-stjarnstigen-project.zip` – konkret ZIP att bifoga i den valda värdmiljön.
- `G03-expected-inventory.json` – facit för filinventeringen.

Använd denna prompt i var och en av ChatGPT Chat, OpenAI Plugin, Claude Projects, Claude Skills och OpenCode:

> Importera bifogad spelprojekt-ZIP. Inventera alla filer. Identifiera README, projektstatus och ändringshistorik, skilj källfiler från genererad output och föreslå 3–5 konkreta nästa steg utan att ändra originalfiler. Ange tydligt om du inte kan läsa ZIP:en.

Registrera per runtime: modell/host-version, datum, fullständigt svar, eventuella filer, evidenslänk och PASS/FAIL/NOT VERIFIED. Kontrollera att README, PROJECT_STATUS, CHANGELOG, tre källfiler och en genererad PDF listas korrekt.

**Begränsning:** Fixturescriptet och dess CI-körning bevisar bara att ZIP:en är korrekt, inte att någon värdmiljö kan importera den. G03-värdmiljötesterna förblir NOT VERIFIED tills faktiska testtranskript granskats.
