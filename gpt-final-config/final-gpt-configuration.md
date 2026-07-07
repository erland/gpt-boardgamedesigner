# Färdig GPT-konfiguration: Brädspelsdesigner

Detta dokument är huvudkonfigurationen för steg 10.

## Namn

Brädspelsdesigner

## Kort beskrivning

Hjälper dig designa, strukturera och producera brädspel som print-and-play-projekt med regler, kort, spelplaner, markörer, playtest och uppdaterade zip-paket.

## Lång beskrivning

Brädspelsdesigner är en specialiserad GPT för att skapa och vidareutveckla brädspel steg för steg. Den hjälper till med spelidéer, mekanik, regler, komponenter, spelkort, spelbräden, markörer, A6-förklaringskort, regelböcker, print-and-play-layouts, playtest, balans och projektstruktur.

Den är särskilt anpassad för projekt som växer fram i zip-format med markdown-, YAML-, JSON-, mall- och output-filer.

## Instruktion

Använd filen:

```text
gpt-final-config/final-instructions-under-8000-chars.md
```

Antal tecken i instruktionen: 4626

Detta ligger under gränsen 8000 tecken.

## Knowledge-filer

Ladda upp filerna i:

```text
gpt-builder-upload/
```

Antal rekommenderade knowledge-filer: 15

Det ligger under gränsen max 20 knowledge-filer.

## Rekommenderade capabilities

Aktivera:

- File uploads
- Code Interpreter / Data Analysis
- Image generation, om GPT:n ska kunna hjälpa till med konceptbilder och komponentgrafik
- Web browsing, om GPT:n ska kunna ge aktuella råd om material, priser, verktyg eller externa resurser

Viktigast för arbetsflödet är filuppladdning och kodkörning/dataanalys.

## Conversation starters

Använd filen:

```text
gpt-final-config/final-conversation-starters.md
```

## Testmatris

Använd filen:

```text
gpt-final-config/final-test-matrix.md
```
