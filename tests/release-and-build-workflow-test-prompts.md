# Testprompter – release- och build-workflow

## Test 1: Release-struktur

```text
Här är ett brädspelsprojekt som zip. Inventera det och skapa en ren release med PDF- och SVG-mappar.
```

Godkänt om GPT:n hittar källor/output, skapar `release/vX.Y.Z/`, uppdaterar manifest/README och skapar ny zip.

## Test 2: Regelboks-PDF

```text
Skapa en professionell PDF av regelboken med Pandoc. Regelboken ska kännas som en spelarkomponent, inte som ett projektdokument.
```

Godkänt om GPT:n använder `docs/rulebook.md` som källa, avråder från projektdokumentation i spelarregelboken, skapar/kontrollerar PDF och uppdaterar status/changelog.

## Test 3: Output-rensning

```text
Det finns många gamla outputfiler. Rensa projektet utan att ta bort källor.
```

Godkänt om GPT:n identifierar källa kontra output, rensar/arkiverar output, bevarar källor och är tydlig med osäkerhet.

## Test 4: Ink-friendly

```text
Gör printmaterialet mer toner-snålt utan att förstöra styled-känslan.
```

Godkänt om GPT:n minskar stora färgfält, behåller tydlighet, regenererar PDF/SVG och dokumenterar stilbeslut.

## Test 5: New-chat-handoff

```text
Förbered projektet så jag kan fortsätta i en ny chat.
```

Godkänt om GPT:n skapar `docs/NEW_CHAT_HANDOFF.md`, `PROJECT_HANDOFF.json`, sammanfattar aktuell release, källor/output och nästa steg.

## Test 6: Simulering

```text
Simulera 1000 spelomgångar och säg om spelet är balanserat.
```

Godkänt om GPT:n anger antaganden och presenterar resultat som hypotes, inte facit.
