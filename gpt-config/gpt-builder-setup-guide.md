# GPT Builder-guide: Brädspelsdesigner

Denna guide beskriver hur kunskapspaketet från steg 9 används för att skapa GPT:n **Brädspelsdesigner** i GPT Builder.

## 1. Skapa ny GPT

Skapa en ny GPT och använd följande profil från:

```text
gpt-config/gpt-profile.md
```

Rekommenderat namn:

```text
Brädspelsdesigner
```

## 2. Lägg in instruktion

Använd instruktionen i:

```text
gpt-config/system-instructions-draft.md
```

Detta är fortfarande ett utkast. I steg 10 kan instruktionen förbättras och göras mer slutgiltig.

## 3. Ladda upp kunskapsfiler

Ladda upp alla filer i:

```text
gpt-builder-upload/
```

Prioritera särskilt:

```text
01-gpt-role-and-working-style.md
02-boardgame-project-standard.md
03-component-design-guide.md
04-game-category-patterns.md
05-print-and-play-production-guide.md
06-rulebook-structure-standard.md
07-playtest-and-balancing-guide.md
08-example-project-pattern.md
KNOWLEDGE_INDEX.md
```

## 4. Lägg in samtalsstarter

Använd samtalsstarterna i:

```text
gpt-config/conversation-starters.md
```

## 5. Rekommenderade capabilities

Aktivera helst:

- filuppladdning
- kodkörning/dataanalys
- bildgenerering om GPT:n ska kunna hjälpa till med visuell konceptdesign
- webbläsning om GPT:n ska kunna ge aktuella råd om material, verktyg eller priser

För arbetet med zip-projekt är filuppladdning och kodkörning/dataanalys viktigast.

## 6. Testa GPT:n

Använd testprompterna i:

```text
tests/all-test-prompts.md
```

Börja med dessa testområden:

1. nytt spel från idé
2. projektstruktur
3. komponentlista
4. spelkategori
5. print-and-play
6. regelbok
7. playtest och balans
8. analys av befintlig projektzip

## 7. Vad GPT:n bör klara efter steg 9

GPT:n bör kunna:

- hjälpa användaren starta ett nytt brädspelsprojekt
- analysera en befintlig projektzip
- föreslå spelkategori och kärnloop
- skapa komponentlista
- strukturera kort, markörer och spelbräde
- skapa regelbok och snabbstart
- skapa A6-förklaringskort/legend
- föreslå print-and-play-produktion
- skapa playtestplan och tolka testanteckningar
- skilja källfiler från output
- föreslå rensning av gamla output-spår
- arbeta iterativt mot uppdaterade zip-paket

## 8. Vad återstår till steg 10

Steg 10 bör skapa en mer färdig GPT-konfiguration:

- slutlig instruktion
- kort och lång beskrivning
- färdiga samtalsstarter
- rekommenderade capabilities
- testmatris
- eventuella gränser och beteenderegler
- första checklista för publicering/användning
