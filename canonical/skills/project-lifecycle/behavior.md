När projekt skapas eller uppdateras ska du tänka i projekt-zip:
- `docs/` för mänskligt läsbar dokumentation
- `data/` för strukturerade källfiler
- `schemas/` för validering vid behov
- `templates/` för layoutmallar
- `scripts/` för generatorer/validering
- `assets/` för källgrafik
- `output/` för genererade filer
- `README.md`, `PROJECT_STATUS.md` och `CHANGELOG.md` för överblick

Skilj alltid mellan källa och output. Ändra i första hand markdown, YAML, JSON, mallar eller script. Behandla PDF, PNG och SVG i `output/` som genererade filer om det finns en källa.

När användaren bifogar en zip ska du först inventera struktur, hitta README/PROJECT_STATUS/CHANGELOG, identifiera källfiler och output, bedöma varianter/spellägen, komponenter, printstatus och risker. Föreslå sedan 3–5 praktiska nästa steg.

När användaren ber dig göra en ändring i ett projekt ska du:
1. uppdatera relevanta källfiler
2. uppdatera regler, data, legend eller printlayout som påverkas
3. uppdatera `PROJECT_STATUS.md` och `CHANGELOG.md`
4. generera output om det är relevant och möjligt
5. paketera uppdaterad zip när användaren ber om det
6. sammanfatta ändringarna kort

När projektet blir stort ska du rekommendera validering: unika id:n, komponentantal, symboler i legend, platstyper på bräde, varianter, printlayout och att output inte är enda källa.

När projektet är mer moget ska du hantera release och build: skilj `output/` från `release/vX.Y.Z/`, skapa PDF som rekommenderat printformat när relevant, behåll markdown/YAML/script som källor, verifiera genererad output, uppdatera release-manifest/status/changelog och skapa new-chat-handoff vid större projekt. Simuleringar ska alltid presenteras som hypoteser, inte facit.
