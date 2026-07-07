# Projektstandard för Brädspelsdesigner

Detta dokument beskriver hur GPT:n **Brädspelsdesigner** bör strukturera, analysera och vidareutveckla brädspelsprojekt som zip-paket.

Syftet är att varje spelprojekt ska vara:

- tydligt att förstå
- enkelt att fortsätta arbeta med
- möjligt att återgenerera
- lätt att rensa
- redo för print-and-play-produktion
- robust nog att byggas vidare på i många iterationer

---

## 1. Grundprincip

Ett brädspelsprojekt ska inte bara bestå av färdiga PDF:er eller bilder.

Projektet bör innehålla:

1. **källor** som beskriver spelets regler och komponenter
2. **datafiler** som går att validera och återanvända
3. **mallar** för layout
4. **script/generatorer** när output skapas automatiskt
5. **genererad output** som kan skrivas ut eller förhandsgranskas
6. **status och changelog** så att projektet går att fortsätta i senare chattar

GPT:n ska alltid försöka förstå vilken fil som är källan och vilken fil som är genererad output.

---

## 2. Rekommenderad projektstruktur

När GPT:n skapar ett nytt brädspelsprojekt bör den använda denna struktur som utgångspunkt:

```text
boardgame-project/
  README.md
  PROJECT_STATUS.md
  CHANGELOG.md
  TODO.md

  docs/
    design-brief.md
    game-overview.md
    rulebook.md
    quickstart.md
    legend-card.md
    playtest-guide.md
    playtest-log.md
    balancing-notes.md
    production-guide.md

  data/
    game.yaml
    cards.yaml
    tokens.yaml
    board.yaml
    variants.yaml
    print-layouts.yaml

  schemas/
    game.schema.json
    cards.schema.json
    tokens.schema.json
    board.schema.json
    variants.schema.json
    print-layouts.schema.json

  assets/
    README.md
    backgrounds/
    icons/
    illustrations/
    photos/
    source/
    fonts-not-included.md

  templates/
    cards/
    board/
    tokens/
    rulebook/
    legend-card/
    print-sheets/

  scripts/
    build_cards.py
    build_board.py
    build_tokens.py
    build_rulebook.py
    build_legend_card.py
    build_printables.py
    validate_project.py

  output/
    cards/
    board/
    tokens/
    rulebooks/
    print/
    preview/

  archive/
    README.md
```

Alla projekt behöver inte alla mappar. Mindre projekt kan börja enklare, men strukturen bör vara kompatibel med att växa.

---

## 3. Minsta rimliga projektstruktur

För ett nytt enkelt spel räcker ofta:

```text
boardgame-project/
  README.md
  PROJECT_STATUS.md
  CHANGELOG.md

  docs/
    design-brief.md
    rulebook.md
    quickstart.md
    production-guide.md

  data/
    game.yaml

  output/
    preview/
```

Om spelet har kort läggs till:

```text
data/cards.yaml
docs/card-list.md
```

Om spelet har markörer läggs till:

```text
data/tokens.yaml
```

Om spelet har spelplan läggs till:

```text
data/board.yaml
```

---

## 4. Filernas ansvar

### 4.1 `README.md`

README är projektets startsida.

Den bör innehålla:

- spelets namn
- kort beskrivning
- målgrupp
- antal spelare
- speltid
- aktuell status
- hur projektet är strukturerat
- hur output genereras
- vilka filer som är viktigast

Exempel:

```markdown
# Skogsäventyret

Ett print-and-play-äventyrsspel för 2–4 spelare från 7 år.

## Status

Första spelbara prototyp.

## Viktiga filer

- `docs/rulebook.md` – huvudregler
- `data/cards.yaml` – kortdata
- `data/board.yaml` – spelplansdata
- `docs/production-guide.md` – utskrifts- och monteringsguide
```

### 4.2 `PROJECT_STATUS.md`

Projektstatus ska beskriva nuläget så att en ny chat snabbt kan fortsätta.

Den bör innehålla:

- aktuell version
- vad spelet är
- vad som är klart
- vad som är pågående
- vad som saknas
- kända problem
- rekommenderat nästa steg
- viktiga designbeslut

Föreslagen struktur:

```markdown
# Projektstatus

## Version

v0.1

## Kort beskrivning

...

## Klart

- ...

## Pågående

- ...

## Saknas

- ...

## Kända problem

- ...

## Viktiga beslut

- ...

## Rekommenderat nästa steg

1. ...
2. ...
3. ...
```

### 4.3 `CHANGELOG.md`

Changelog ska visa vad som har ändrats mellan versioner.

Föreslagen struktur:

```markdown
# Changelog

## v0.2 – 2026-07-06

### Tillagt

- ...

### Ändrat

- ...

### Rensat

- ...

### Fixat

- ...

### Kommentar

- ...
```

GPT:n bör uppdatera changelog när den gör en faktisk projektändring.

### 4.4 `TODO.md`

TODO används för öppna arbetsuppgifter.

Den bör vara enkel:

```markdown
# TODO

## Nästa

- [ ] ...

## Senare

- [ ] ...

## Kanske

- [ ] ...
```

TODO ska inte ersätta `PROJECT_STATUS.md`, utan komplettera det.

---

## 5. `docs/` – mänskligt läsbar dokumentation

`docs/` innehåller dokument som användaren kan läsa och redigera.

Typiska filer:

### 5.1 `docs/design-brief.md`

Spelets designunderlag.

Bör innehålla:

- titel
- pitch
- målgrupp
- spelupplevelse
- antal spelare
- speltid
- komplexitet
- kärnloop
- huvudkomponenter
- inspirationskällor
- designrisker

### 5.2 `docs/game-overview.md`

Kortare översikt över spelet.

Användbar när regelboken är lång.

### 5.3 `docs/rulebook.md`

Huvudregelbok.

Ska vara primär källa för regler om det inte finns mer strukturerade regeldata.

### 5.4 `docs/quickstart.md`

Snabbstart för första spelomgången.

Ska vara kortare än regelboken.

### 5.5 `docs/legend-card.md`

Underlag för A6-förklaringskort eller referenskort.

Ska vara kort, visuellt och användbart vid bordet.

### 5.6 `docs/playtest-guide.md`

Beskriver hur spelet ska testas.

### 5.7 `docs/playtest-log.md`

Logg över speltester.

### 5.8 `docs/balancing-notes.md`

Anteckningar om balans, kortvärden, svårighetsgrad och justeringar.

### 5.9 `docs/production-guide.md`

Beskriver hur spelet skrivs ut, skärs, lamineras och monteras.

---

## 6. `data/` – strukturerade källfiler

`data/` innehåller maskinläsbar eller tydligt strukturerad speldata.

GPT:n bör föreslå YAML som standard eftersom det är lättläst, men JSON kan användas när validering eller verktyg gör det mer lämpligt.

### 6.1 `data/game.yaml`

Övergripande metadata.

Exempel:

```yaml
game:
  id: skogsaventyret
  title: Skogsäventyret
  version: 0.1
  players:
    min: 2
    max: 4
  age: 7+
  play_time_minutes: 25
  complexity: low
  format: print-and-play
  status: first_playable_prototype
```

### 6.2 `data/cards.yaml`

Kortdata.

Exempel:

```yaml
cards:
  - id: card_001
    name: Hitta en stig
    type: event
    count: 2
    effect: Flytta 1 steg.
    tags: [movement, forest]
```

### 6.3 `data/tokens.yaml`

Markörer och tokens.

Exempel:

```yaml
tokens:
  - id: token_energy
    name: Energi
    shape: circle
    count: 20
    print_size_mm: 25
    icon: lightning
```

### 6.4 `data/board.yaml`

Spelplansdata.

Exempel:

```yaml
board:
  id: main_board
  name: Äventyrskartan
  format: A4
  spaces:
    - id: start
      label: Start
      type: start
    - id: forest_1
      label: Skog
      type: forest
```

### 6.5 `data/variants.yaml`

Spellägen och varianter.

Exempel:

```yaml
variants:
  - id: basic
    name: Grundspel
    recommended_age: 7+
    notes: Enkel version med färre specialregler.
  - id: adventure
    name: Äventyrsläge
    recommended_age: 9+
    notes: Lägger till uppdrag och händelser.
```

### 6.6 `data/print-layouts.yaml`

Beskriver printark.

Exempel:

```yaml
print_layouts:
  - id: cards_a4_3x3
    component_type: cards
    paper: A4
    columns: 3
    rows: 3
    cut_lines: true
```

---

## 7. `schemas/` – validering

`schemas/` innehåller JSON Schema-filer eller annan dokumentation som beskriver hur datafiler ska se ut.

Syftet är att:

- fånga fel tidigt
- göra projektet begripligt för nya chattar
- säkerställa att generatorer kan lita på data
- undvika att kort och markörer får olika fält av misstag

GPT:n ska inte skapa komplicerade schemafiler i onödan, men bör göra det när projektet börjar få många kort, markörer, varianter eller print-layouts.

---

## 8. `assets/` – bilder och grafiskt material

`assets/` innehåller källbilder och grafik.

Föreslagen struktur:

```text
assets/
  README.md
  backgrounds/
  icons/
  illustrations/
  photos/
  source/
  fonts-not-included.md
```

### Regler för assets

- Original/källbilder ska sparas separat från genererade output-filer.
- Stora historiska bilder ska inte ligga kvar om de inte behövs.
- Fonts ska normalt inte delas om licensen är oklar.
- Om fontfiler inte ingår bör `fonts-not-included.md` förklara vilka typsnitt projektet förväntar sig.

---

## 9. `templates/` – layoutmallar

`templates/` innehåller mallar som används för att generera output.

Exempel:

```text
templates/
  cards/
    card-front.html
    card-back.html
  rulebook/
    rulebook.css
  legend-card/
    a6-legend.html
  print-sheets/
    a4-card-sheet.html
```

GPT:n bör använda mallar när flera output-filer ska ha samma layout.

---

## 10. `scripts/` – generatorer och validering

`scripts/` innehåller bygg- och valideringsscript.

Exempel:

```text
scripts/
  validate_project.py
  build_cards.py
  build_tokens.py
  build_board.py
  build_rulebook.py
  build_legend_card.py
  build_printables.py
```

Script ska ha tydliga namn och helst kunna köras lokalt.

Om projektet är enkelt kan script utelämnas tills de behövs.

---

## 11. `output/` – genererade filer

`output/` innehåller genererade filer.

Exempel:

```text
output/
  cards/
  board/
  tokens/
  rulebooks/
  print/
  preview/
```

### Regler för output

- Output ska kunna återskapas från källfiler.
- Output ska inte vara primär källa om det finns motsvarande markdown/YAML/mallar.
- Output kan rensas om den är gammal och kan genereras igen.
- Produktionsfärdig output bör ligga tydligt separerat från förhandsvisningar.

---

## 12. `archive/` – historik

`archive/` används sparsamt.

Det får inte bli en slaskmapp där stora gamla filer samlas utan syfte.

Om `archive/` används bör den ha en README:

```markdown
# Archive

Denna mapp innehåller äldre filer som sparats för referens.

Filer här ska inte användas som aktuell källa om inte annat anges.
```

GPT:n bör hellre rensa bort onödig output än flytta allt till archive.

---

## 13. Namngivning och versionering

### 13.1 Filnamn

Använd:

- små bokstäver
- bindestreck
- tydliga namn
- inga datum i filnamn om versionering redan hanteras i changelog

Bra:

```text
rulebook.md
legend-card.md
cards.yaml
print-layouts.yaml
```

Mindre bra:

```text
Regler NY SLUTLIG v3 test FINAL.md
kort_backup_gammal2.yaml
```

### 13.2 Versioner

Använd enkel versionering:

- `v0.1` första prototyp
- `v0.2` efter första större ändring
- `v0.3` efter speltestjustering
- `v1.0` första stabila version

Versionen bör synas i:

- `data/game.yaml`
- `PROJECT_STATUS.md`
- `CHANGELOG.md`

---

## 14. Hur GPT:n ska analysera en befintlig zip

När användaren bifogar en zip bör GPT:n följa denna ordning:

### Steg 1: Inventera

Lista:

- mappar
- centrala filer
- output-mappar
- datafiler
- script
- stora filer

### Steg 2: Hitta projektets sannolika källa

Prioritera:

1. `PROJECT_STATUS.md`
2. `README.md`
3. `CHANGELOG.md`
4. `docs/`
5. `data/`
6. `schemas/`
7. `scripts/`
8. `templates/`
9. `output/`

### Steg 3: Bedöm aktualitet

Titta på:

- filnamn
- changelog
- versionsnummer
- om output verkar genererad från data
- om flera parallella spår finns
- om gamla mappar verkar övergivna

### Steg 4: Sammanfatta

Svara med:

- vad spelet verkar vara
- vad som verkar klart
- vad som verkar pågående
- vad som saknas
- vilka filer som verkar viktigast
- vilka risker som finns

### Steg 5: Föreslå nästa steg

Ge max 3–5 praktiska nästa steg.

---

## 15. Hur GPT:n ska ändra ett projekt

När användaren ber GPT:n att ändra ett projekt ska GPT:n:

1. identifiera relevanta källfiler
2. göra ändringen i källan
3. uppdatera eventuell output om det ingår
4. uppdatera `PROJECT_STATUS.md`
5. uppdatera `CHANGELOG.md`
6. validera rimligt att projektet hänger ihop
7. paketera en ny zip om användaren bett om det

GPT:n ska undvika att bara ändra genererade PDF:er eller bilder om det finns en källa som borde ändras i stället.

---

## 16. Rensning av projekt

När användaren vill minska zip-storlek eller rensa projektet ska GPT:n skilja på:

### 16.1 Säkert att rensa

Ofta säkert:

- gamla preview-filer
- gamla output-versioner
- temporära filer
- cache-mappar
- dubbla genererade PDF:er
- oanvända gamla print-spår
- systemfiler som `.DS_Store`

### 16.2 Riskabelt att rensa

Var försiktig med:

- `data/`
- `docs/`
- `templates/`
- `scripts/`
- originalbilder i `assets/source/`
- filer som nämns i README, changelog eller scripts

### 16.3 Rensningsrapport

Vid rensning bör GPT:n skapa eller uppdatera dokumentation:

```markdown
## Rensning v0.4

### Borttaget

- ...

### Bevarat

- ...

### Motiv

- ...
```

---

## 17. Rekommenderat projektstatusformat

GPT:n bör använda detta format när den skapar `PROJECT_STATUS.md`:

```markdown
# Projektstatus

## Projekt

Namn: ...
Version: ...
Status: ...

## Kort beskrivning

...

## Målgrupp

...

## Spelupplägg

...

## Komponenter

- ...

## Klart

- ...

## Pågående

- ...

## Saknas

- ...

## Kända problem

- ...

## Viktiga beslut

- ...

## Genererad output

- ...

## Rekommenderat nästa steg

1. ...
2. ...
3. ...
```

---

## 18. Rekommenderat changelogformat

GPT:n bör använda detta format när den skapar `CHANGELOG.md`:

```markdown
# Changelog

## v0.1 – YYYY-MM-DD

### Tillagt

- ...

### Ändrat

- ...

### Fixat

- ...

### Rensat

- ...

### Kommentar

- ...
```

Om datum är okänt kan GPT:n använda dagens datum om verktygsmiljön ger det, eller lämna datumfältet utan att gissa.

---

## 19. Rekommenderat README-format

GPT:n bör använda detta format när den skapar `README.md`:

```markdown
# Projektnamn

Kort beskrivning.

## Snabbfakta

- Spelare:
- Ålder:
- Speltid:
- Format:
- Status:

## Viktiga filer

- `docs/rulebook.md`
- `docs/quickstart.md`
- `data/game.yaml`

## Projektstruktur

...

## Bygga/generera output

...

## Nästa steg

...
```

---

## 20. När projektet växer

När projektet blir större bör GPT:n föreslå att lägga till:

- schemafiler
- valideringsscript
- separat print-layoutdata
- separat dokumentation för varianter
- playtestlogg
- produktionsguide
- rensningsregler
- tydligare output-struktur

---

## 21. Definition of Done för steg 2

Steg 2 är klart när kunskapspaketet innehåller en tydlig projektstandard som beskriver:

- rekommenderad mappstruktur
- minsta projektstruktur
- ansvar för centrala filer
- hur `docs/`, `data/`, `schemas/`, `assets/`, `templates/`, `scripts/` och `output/` ska användas
- hur README, PROJECT_STATUS och CHANGELOG ska skrivas
- hur GPT:n ska analysera zippar
- hur GPT:n ska ändra projekt
- hur GPT:n ska rensa projekt utan att tappa källmaterial
