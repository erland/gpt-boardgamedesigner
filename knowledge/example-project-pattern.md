# Exempelprojektmönster: print-and-play-brädspel

Detta dokument beskriver ett generellt projektmönster som GPT:n **Brädspelsdesigner** kan använda som inspiration när den analyserar eller bygger brädspelsprojekt.

Mönstret är inspirerat av ett befintligt print-and-play-projekt med kort, spelbräde, markörer, regelvarianter, print-output och uppdaterade zip-paket. Dokumentet ska däremot inte göra GPT:n beroende av ett visst tema, varumärke, filnamn eller exakt mappstruktur.

Syftet är att extrahera arbetsformen:

- projektet växer stegvis
- zippen uppdateras efter hand
- markdown/YAML fungerar som källor
- PDF/SVG/PNG fungerar som genererad output
- regler, komponenter och printproduktion hålls ihop
- gamla output-spår kan rensas när de inte längre behövs
- legendkort och regelböcker ska vara tydliga spelhjälpmedel

---

## 1. Vad GPT:n ska lära av exempelprojektet

GPT:n ska lära sig följande generella mönster:

1. Ett brädspelsprojekt bör kunna fortsätta i många chattar.
2. Projektstatus och changelog är viktiga för kontinuitet.
3. Regler, komponenter och print-output ska inte utvecklas isolerat.
4. En zip kan innehålla både källor och genererad output, och GPT:n måste skilja dem åt.
5. PDF-filer är ofta resultatet av markdown, YAML, HTML, SVG eller script.
6. Spelvarianter bör ha tydlig struktur, inte bara spridda dokument.
7. Förklaringskort/legendkort bör behandlas som egna spelkomponenter.
8. Print-and-play-produktion kräver praktiska beslut om A4, A6, skärlinjer, laminering och marginaler.
9. När projektet växer behöver gamla output-spår rensas eller märkas tydligt.
10. GPT:n ska hellre skapa återgenererbara källor än bara en färdig PDF.

---

## 2. Observerad projektkaraktär

Det analyserade exempelprojektet är ett print-and-play-spelprojekt med flera vanliga byggdelar:

- regler
- flera spellägen/varianter
- kort
- spelbräde
- markörer/tokens
- förklaringskort/legend
- print-output
- PDF-versioner
- bild-/layoutoutput
- scripts eller byggsteg
- iterativa zip-versioner

Det är därför ett bra exempel på ett spelprojekt som behöver en tydlig arbetsmetod.

### Teknisk observation från exempelzippen

Följande är en automatisk översikt av den analyserade zippen. Detta är bara strukturinformation, inte en mall som måste kopieras exakt.

```json
{
  "available": true,
  "total_files": 327,
  "top_dirs": [
    [
      "output",
      140
    ],
    [
      "assets",
      72
    ],
    [
      "docs",
      65
    ],
    [
      "data",
      18
    ],
    [
      "tests",
      13
    ],
    [
      "scripts",
      11
    ],
    [
      "templates",
      5
    ],
    [
      "PLAN-pokemon-mini-battle.md",
      1
    ],
    [
      "README.md",
      1
    ],
    [
      "pytest.ini",
      1
    ]
  ],
  "extensions": {
    ".png": 89,
    ".svg": 77,
    ".md": 69,
    ".pdf": 24,
    ".py": 24,
    ".html": 18,
    ".yaml": 18,
    ".css": 3,
    "[no extension]": 3,
    ".ini": 1,
    ".txt": 1
  },
  "notable_files": [
    "README.md",
    "docs/game-rules.md",
    "docs/card-standard.md",
    "docs/changelog.md",
    "docs/project-status.md",
    "docs/effect-cards.md",
    "docs/print-layout.md",
    "docs/print-sets.md",
    "docs/icon-reference.pdf",
    "docs/step14t-stable-pdf-export.md",
    "docs/damage-markers.md",
    "docs/step14w-damage-marker-colors-and-sizes.md",
    "docs/energy-markers.md",
    "docs/step14y-rectangular-energy-markers.md",
    "docs/adventure-board-format.md",
    "docs/adventure-board-visual-style.md",
    "docs/adventure-board-layout-rules.md",
    "docs/rules/rules-reservduell.md",
    "docs/rules/rules-alla-mot-alla.md",
    "docs/rules/rules-boss-strid.md",
    "docs/rules/README.md",
    "docs/rules/rules-aventyrslage.md",
    "docs/printables/adventure-explanation-card.md",
    "docs/adventure-board-print-layouts.md",
    "docs/adventure-board-deluxe-background.md",
    "data/types.yaml",
    "data/attacks.yaml",
    "data/pokemon.yaml",
    "data/effect-cards.yaml",
    "data/print-sets.yaml",
    "data/validation-rules.yaml",
    "data/pokemon.schema.yaml",
    "data/pokemon.examples.yaml",
    "data/balance-notes.yaml",
    "data/print-layouts.yaml",
    "data/playtest-decks.yaml",
    "data/damage-markers.yaml",
    "data/energy-markers.yaml",
    "data/boards/adventure-board-01.yaml",
    "data/boards/adventure-board.schema.yaml",
    "data/boards/adventure-board-legend.yaml",
    "data/boards/themes/forest-adventure.yaml",
    "data/boards/adventure-board-print-layouts.yaml",
    "templates/pokemon-card.html",
    "templates/effect-card.html",
    "templates/print.css",
    "templates/rulebook.css",
    "scripts/generate_cards.py",
    "scripts/export_pdfs.py",
    "scripts/export_rulebook_pdfs.py",
    "scripts/generate_adventure_board.py",
    "scripts/generate_adventure_legend_pdf.py",
    "scripts/generate_adventure_print_layouts.py",
    "scripts/generate_adventure_deluxe_board.py",
    "output/README.md",
    "output/pdf/.gitkeep",
    "output/pdf/core-pokemon-a4-01.pdf",
    "output/pdf/core-pokemon-a4-02.pdf",
    "output/pdf/core-pokemon-a4-03.pdf",
    "output/pdf/effect-cards-beginner-deck-a4-01.pdf",
    "output/pdf/eevee-branching-preview-a4-01.pdf",
    "output/pdf/damage-markers-a4-01.pdf",
    "output/pdf/energy-markers-a4-01.pdf",
    "output/pdf/rules/rules-reservduell.pdf",
    "output/pdf/rules/rules-alla-mot-alla.pdf",
    "output/pdf/rules/rules-boss-strid.pdf",
    "output/pdf/rules/rules-aventyrslage.pdf",
    "output/pdf/boards/adventure-board-01-overview.pdf",
    "output/pdf/boards/adventure-board-legend.pdf",
    "output/pdf/boards/adventure-board-legend-a6.pdf",
    "output/pdf/boards/adventure-board-legend-a6-on-a4.pdf",
    "output/pdf/boards/print/adventure-board-a4-overview.pdf",
    "output/pdf/boards/print/adventure-board-a4-plain.pdf",
    "output/pdf/boards/print/adventure-board-2xa4-plain-tiled.pdf",
    "output/pdf/boards/print/adventure-board-a4-deluxe-plain.pdf",
    "output/pdf/boards/adventure-board-01-plain.pdf",
    "output/pdf/boards/adventure-board-01-transparent-overlay.pdf",
    "output/pdf/boards/adventure-board-01-transparent-overlay-plain.pdf",
    "output/pdf/printables/adventure-explanation-card-a6-on-a4.pdf",
    "output/previews/damage-markers-a4-01.png",
    "output/previews/energy-markers-a4-01.png",
    "output/previews/adventure-explanation-card-a6-on-a4.png",
    "output/previews/boards/print/adventure-board-a4-overview.png",
    "output/previews/boards/print/adventure-board-a4-plain.png",
    "output/previews/boards/print/adventure-board-2xa4-plain-assembled-preview.png",
    "output/previews/boards/print/adventure-board-2xa4-plain-page-1.png",
    "output/previews/boards/print/adventure-board-2xa4-plain-page-2.png",
    "output/previews/boards/print/adventure-board-2xa4-plain-placement.txt",
    "output/previews/boards/print/adventure-board-a4-deluxe-plain.png",
    "output/boards/adventure-board-01-overview.svg",
    "output/boards/adventure-board-01-overview.png",
    "output/boards/README.md",
    "output/boards/legend-icons/start.png",
    "output/boards/legend-icons/grass.png",
    "output/boards/legend-icons/danger_grass.png",
    "output/boards/legend-icons/rest.png",
    "output/boards/legend-icons/bonus_glade.png",
    "output/boards/legend-icons/boss_gate.png",
    "output/boards/legend-icons/boss.png",
    "output/boards/adventure-board-01-plain.svg",
    "output/boards/adventure-board-01-plain.png",
    "output/boards/adventure-board-01-transparent-overlay-plain.svg",
    "output/boards/adventure-board-01-transparent-overlay-plain.png",
    "output/boards/adventure-board-01-deluxe-plain.png",
    "output/html/print.css",
    "output/html/assets/board-icons/start.svg",
    "output/html/assets/board-icons/grass.svg",
    "output/html/assets/board-icons/danger-grass.svg",
    "output/html/assets/board-icons/rest.svg",
    "output/html/assets/board-icons/bonus-glade.svg",
    "output/html/assets/board-icons/boss-gate.svg",
    "output/html/assets/board-icons/boss.svg",
    "output/html/assets/board-icons/README.md",
    "output/html/assets/icons/effects/status.svg",
    "output/html/assets/icons/effects/status.png",
    "output/html/assets/printables/adventure-explanation-card.png",
    "output/html/effect-cards-a4-01.html",
    "output/html/effect-cards-beginner-deck-a4-01.html",
    "output/html/damage-markers-a4-01.html",
    "output/html/energy-markers-a4-01.html"
  ],
  "sample_paths": [
    "PLAN-pokemon-mini-battle.md",
    "README.md",
    "pytest.ini",
    "docs/game-rules.md",
    "docs/card-standard.md",
    "docs/data-model.md",
    "docs/balancing-notes.md",
    "docs/copyright-and-design-notes.md",
    "docs/changelog.md",
    "docs/project-status.md",
    "docs/type-data.md",
    "docs/attack-data.md",
    "docs/pokemon-data.md",
    "docs/pokemon-selection.md",
    "docs/attack-selection.md",
    "docs/step7-validation-summary.md",
    "docs/step8-validation-summary.md",
    "docs/effect-cards.md",
    "docs/step9-validation-summary.md",
    "docs/print-layout.md",
    "docs/step10-validation-summary.md",
    "docs/generator.md",
    "docs/step11-validation-summary.md",
    "docs/validation-report.md",
    "docs/validation.md",
    "docs/step12-validation-summary.md",
    "docs/print-sets.md",
    "docs/step13-validation-summary.md",
    "docs/quickstart.md",
    "docs/first-playable-version.md",
    "docs/playtest-readiness.md",
    "docs/step14-validation-summary.md",
    "docs/step14b-design-adjustment-summary.md",
    "docs/step14c-svg-icons-summary.md",
    "docs/step14d-icon-redesign-summary.md",
    "docs/icon-reference.html",
    "docs/icon-reference.pdf",
    "docs/step14f-icon-refinement-summary.md",
    "docs/step14g-png-icons-summary.md",
    "docs/step14h-transparent-icons-summary.md",
    "docs/step14i-normalized-png-icons-summary.md",
    "docs/step14j-layout-adjustment-summary.md",
    "docs/step14k-dice-indicator-adjustment.md",
    "docs/step14l-attack-row-alignment.md",
    "docs/step14m-128-icons-summary.md",
    "docs/step14n-separate-dice-column.md",
    "docs/step14o-dice-vertical-centering.md",
    "docs/step14p-attack-row-height.md",
    "docs/step14q-attack-descenders.md",
    "docs/step14r-compact-attacks-header-hp.md",
    "docs/step14s-icon-scale-and-vertical-family.md",
    "docs/step14t-stable-pdf-export.md",
    "docs/step14u-branching-evolutions.md",
    "docs/damage-markers.md",
    "docs/step14w-damage-marker-colors-and-sizes.md",
    "docs/energy-markers.md",
    "docs/step14y-rectangular-energy-markers.md",
    "docs/adventure-board-format.md",
    "docs/adventure-board-visual-style.md",
    "docs/adventure-board-layout-rules.md"
  ],
  "large_files": [
    [
      "output/pdf/boards/print/adventure-board-a4-deluxe-plain.pdf",
      20023907
    ],
    [
      "output/previews/boards/print/adventure-board-a4-deluxe-plain.png",
      8415825
    ],
    [
      "output/pdf/boards/print/adventure-board-2xa4-plain-tiled.pdf",
      3026565
    ],
    [
      "output/html/assets/backgrounds/forest-painted-creek-cliff.png",
      2832401
    ],
    [
      "assets/backgrounds/forest-painted-creek-cliff.png",
      2832401
    ],
    [
      "output/boards/adventure-board-01-deluxe-plain.png",
      2803302
    ],
    [
      "output/pdf/boards/print/adventure-board-a4-overview.pdf",
      2392060
    ],
    [
      "output/pdf/printables/adventure-explanation-card-a6-on-a4.pdf",
      2339529
    ],
    [
      "output/pdf/boards/print/adventure-board-a4-plain.pdf",
      2154224
    ],
    [
      "output/previews/boards/print/adventure-board-2xa4-plain-assembled-preview.png",
      2099968
    ],
    [
      "output/html/assets/source-sheets/type-icon-tileset.png",
      2035662
    ],
    [
      "assets/source-sheets/type-icon-tileset.png",
      2035662
    ],
    [
      "docs/icon-reference.pdf",
      1943028
    ],
    [
      "output/html/assets/source-sheets/effect-icon-tileset.png",
      1835232
    ],
    [
      "assets/source-sheets/effect-icon-tileset.png",
      1835232
    ],
    [
      "output/previews/boards/print/adventure-board-a4-overview.png",
      1734861
    ],
    [
      "output/previews/adventure-explanation-card-a6-on-a4.png",
      1563333
    ],
    [
      "output/previews/boards/print/adventure-board-a4-plain.png",
      1535730
    ],
    [
      "output/html/assets/printables/adventure-explanation-card.png",
      1498070
    ],
    [
      "assets/printables/adventure-explanation-card.png",
      1498070
    ]
  ]
}
```

GPT:n ska använda denna typ av observation för att förstå hur ett befintligt projekt är organiserat, men inte låsa nya projekt till samma detaljer.

---

## 3. Rekommenderat generellt projektmönster

Ett nytt projekt som liknar detta i arbetsform kan struktureras så här:

```text
boardgame-project/
  README.md
  PROJECT_STATUS.md
  CHANGELOG.md
  TODO.md

  docs/
    design-brief.md
    rulebook.md
    quickstart.md
    legend-card.md
    playtest-log.md
    production-guide.md

  docs/rulebooks/
    basic-rules.md
    variant-1-rules.md
    variant-2-rules.md

  data/
    game.yaml
    cards.yaml
    tokens.yaml
    board.yaml
    variants.yaml
    legend-card.yaml
    print-layouts.yaml

  schemas/
    cards.schema.json
    tokens.schema.json
    board.schema.json
    variants.schema.json

  assets/
    backgrounds/
    icons/
    illustrations/
    source/

  templates/
    cards/
    board/
    tokens/
    rulebook/
    legend-card/
    print-sheets/

  scripts/
    validate_project.py
    build_cards.py
    build_board.py
    build_tokens.py
    build_rulebooks.py
    build_legend_card.py
    build_printables.py

  output/
    print/
    preview/
    cards/
    board/
    tokens/
    rulebooks/

  archive/
    README.md
```

Alla mappar behövs inte från början. GPT:n ska skala strukturen efter projektets storlek.

---

## 4. Viktiga källor i ett iterativt spelprojekt

GPT:n bör i första hand leta efter och uppdatera dessa filer:

| Syfte | Rekommenderad fil |
|---|---|
| Projektöversikt | `README.md` |
| Aktuellt nuläge | `PROJECT_STATUS.md` |
| Ändringshistorik | `CHANGELOG.md` |
| Öppen arbetslista | `TODO.md` |
| Designmål | `docs/design-brief.md` |
| Huvudregler | `docs/rulebook.md` |
| Separata varianter | `docs/rulebooks/*.md` |
| Snabbstart | `docs/quickstart.md` |
| Legend/förklaringskort | `docs/legend-card.md` eller `data/legend-card.yaml` |
| Kortdata | `data/cards.yaml` |
| Markördata | `data/tokens.yaml` |
| Spelplansdata | `data/board.yaml` |
| Variantdata | `data/variants.yaml` |
| Printlayout | `data/print-layouts.yaml` |
| Produktionsinstruktion | `docs/production-guide.md` |
| Speltest | `docs/playtest-log.md` |

När dessa filer saknas kan GPT:n föreslå att skapa dem.

---

## 5. Regler och varianter

Exempelprojektet visar att ett spel lätt får flera varianter.

GPT:n bör skilja mellan:

1. **Grundspel** – minsta stabila spelupplevelse.
2. **Utökad variant** – lägger till fler regler eller komponenter.
3. **Äventyrs-/scenarioläge** – ändrar mål, progression eller spelplan.
4. **Barn-/familjevariant** – förenklar regler eller kortar speltid.
5. **Coop-/solo-/duellvariant** – ändrar interaktion och vinstvillkor.

### Rekommenderat arbetssätt

När varianter är små:

```text
docs/rulebook.md
data/variants.yaml
```

När varianter är stora:

```text
docs/rulebooks/basic-rules.md
docs/rulebooks/adventure-mode-rules.md
docs/rulebooks/coop-rules.md
data/variants.yaml
```

Varje separat regelbok ska vara spelbar fristående.

GPT:n ska undvika att skapa varianter som bara är spridda kommentarer i flera filer.

---

## 6. Komponenter som bör hållas ihop

I den här typen av projekt hänger flera komponenter ihop:

| Komponent | Källa | Output |
|---|---|---|
| Regelbok | `docs/rulebook.md` | `output/rulebooks/rulebook.pdf` |
| Variantregelbok | `docs/rulebooks/*.md` | `output/rulebooks/*.pdf` |
| Kort | `data/cards.yaml` | `output/print/cards-a4.pdf` |
| Markörer | `data/tokens.yaml` | `output/print/tokens-a4.pdf` |
| Spelbräde | `data/board.yaml` / assets/templates | `output/print/board-a4.pdf` |
| Legendkort | `docs/legend-card.md` / `data/legend-card.yaml` | `output/print/legend-card-a6.pdf` |
| Produktionsguide | `docs/production-guide.md` | eventuell PDF |
| Preview | källor + script | `output/preview/*.png` |

När GPT:n ändrar en komponent ska den kontrollera om andra komponenter också påverkas.

Exempel:

- Om en ny symbol läggs till på korten bör legendkortet uppdateras.
- Om en ny markör nämns i reglerna bör `data/tokens.yaml` uppdateras.
- Om spelbrädet får nya platstyper bör regelbok och legendkort uppdateras.
- Om en variant får egna regler bör `data/variants.yaml` och regelboksindex uppdateras.
- Om output genereras om bör changelog/projektstatus uppdateras.

---

## 7. Förklaringskort / legendkort

Ett återkommande mönster är behovet av ett litet referenskort som hjälper spelare under spelet.

GPT:n bör hantera detta som en förstaklasskomponent.

### Syfte

Legendkortet ska hjälpa spelare under pågående spel.

Det ska inte vara:

- en komprimerad regelbok
- en fullständig manual
- en lista över alla undantag

Det ska vara:

- kort
- visuellt
- A6-vänligt
- kopplat till symboler
- kopplat till turordning
- lätt att laminera
- användbart vid bordet

### Rekommenderad källa

För enkla projekt:

```text
docs/legend-card.md
```

För mer datadrivna projekt:

```text
data/legend-card.yaml
```

### Rekommenderad output

```text
output/print/legend-card-a6.pdf
output/print/legend-cards-a4.pdf
```

### Innehåll

```markdown
# Snabbreferens

## Din tur

1. ...
2. ...
3. ...

## Symboler

| Symbol | Betydelse |
|---|---|

## Kom ihåg

- ...
```

---

## 8. Printspår och output

Exempelprojektet visar att ett projekt kan få flera output-spår över tid, exempelvis äldre printables, nya printmappar, previewfiler och PDF-versioner.

GPT:n bör alltid fråga:

- Vilken output är aktuell?
- Kan outputen genereras igen?
- Finns det flera parallella spår?
- Är gamla PDF:er historik eller förvirrande?
- Finns källor för allt viktigt?

### Rekommendation

Aktuell print-output bör ligga samlat:

```text
output/print/
```

Preview bör ligga separat:

```text
output/preview/
```

Regelboks-PDF:er kan ligga i:

```text
output/rulebooks/
```

eller i `output/print/` om de är del av printpaketet.

Gamla spår bör antingen rensas eller flyttas till `archive/` med tydlig README.

---

## 9. Rensning av stora projektzippar

När zippen blir stor bör GPT:n göra en strukturerad rensningsanalys.

### Säkrare att rensa

- gamla previewbilder
- äldre PDF-output som kan genereras igen
- dubbletter av printark
- tidigare misslyckade output-spår
- temporära filer
- cache-mappar
- `.DS_Store`
- gamla testexporter

### Riskabelt att rensa

- `docs/`
- `data/`
- `schemas/`
- `templates/`
- `scripts/`
- originalfiler i `assets/source/`
- den enda versionen av en bild eller spelplan
- filer som nämns i README, changelog eller scripts

### Rensningsrapport

GPT:n bör skapa en kort rapport:

```markdown
# Rensningsrapport

## Borttaget

- ...

## Bevarat

- ...

## Motiv

- ...

## Kontroll

- ...
```

Och uppdatera `CHANGELOG.md`.

---

## 10. Byggsteg och generatorer

Ett mognare print-and-play-projekt kan ha script som genererar output.

GPT:n bör uppmuntra generatorer när:

- korten är många
- markörer ska skapas från data
- flera regelböcker ska genereras
- printark ska kunna återskapas
- layouten ändras ofta
- projektet ska fortsätta i många iterationer

Exempel:

```text
scripts/validate_project.py
scripts/build_cards.py
scripts/build_tokens.py
scripts/build_rulebooks.py
scripts/build_printables.py
```

GPT:n bör också skapa dokumentation för hur script används:

```markdown
## Bygga output

Kör:

```bash
python scripts/validate_project.py
python scripts/build_printables.py
```
```

---

## 11. Validering

Exempelprojekt med flera komponenter behöver validering.

GPT:n bör föreslå validering som kontrollerar:

- att alla kort har id
- att kort-id:n är unika
- att alla tokens har count
- att komponentlistan matchar datafiler
- att alla symboler som används finns i legend
- att alla platstyper på brädet är definierade
- att alla varianter har namn och beskrivning
- att README/PROJECT_STATUS/CHANGELOG finns
- att outputfiler inte är den enda källan

Validering kan först vara en checklista i markdown och senare bli script.

---

## 12. Rekommenderad arbetscykel

GPT:n bör driva projekt enligt denna cykel:

```text
1. Definiera eller uppdatera källor
2. Uppdatera regler och komponentdata
3. Uppdatera legend/referens
4. Uppdatera print-layout
5. Generera output
6. Kontrollera output
7. Uppdatera projektstatus/changelog
8. Paketera zip
9. Speltesta
10. Dokumentera test
11. Justera källor
```

Viktigt: hoppa inte direkt till snygg output utan att källorna är stabila nog.

---

## 13. Hur GPT:n bör analysera en liknande zip

När användaren bifogar ett projekt liknande exempelprojektet bör GPT:n svara enligt detta mönster:

```markdown
## Projektets nuläge

...

## Sannolika källfiler

- ...

## Genererad output

- ...

## Varianter/spellägen

- ...

## Komponenter

- ...

## Print-and-play-status

- ...

## Risker

- flera output-spår
- saknad källa för viss PDF
- legendkort inte kopplat till symboler
- regelbok och kortdata verkar inte matcha

## Rekommenderade nästa steg

1. ...
2. ...
3. ...
```

GPT:n ska inte börja ändra utan att först förstå vilka filer som är källa.

---

## 14. Exempel på generisk projektstatus

När GPT:n skapar eller förbättrar `PROJECT_STATUS.md` kan detta mönster användas:

```markdown
# Projektstatus

## Projekt

Namn: ...
Version: v0.x
Status: Första spelbara prototyp / Print-and-play-prototyp / Under balansarbete

## Kort beskrivning

...

## Aktuella spellägen

- Grundspel
- Variant: ...
- Variant: ...

## Komponenter

- Spelbräde
- Kort
- Markörer
- Regelbok
- A6-referenskort

## Källfiler

- `docs/rulebook.md`
- `data/cards.yaml`
- `data/tokens.yaml`
- `data/board.yaml`
- `docs/legend-card.md`

## Genererad output

- `output/print/cards-a4.pdf`
- `output/print/tokens-a4.pdf`
- `output/print/board-a4.pdf`
- `output/print/legend-card-a6.pdf`

## Klart

- ...

## Pågående

- ...

## Saknas

- ...

## Kända problem

- ...

## Rekommenderat nästa steg

1. ...
2. ...
3. ...
```

---

## 15. Exempel på generisk changelogpost

```markdown
## v0.8 – YYYY-MM-DD

### Tillagt

- Lade till A6-förklaringskort som egen källa i `docs/legend-card.md`.
- Lade till printlayout för legendkort i `data/print-layouts.yaml`.

### Ändrat

- Uppdaterade regelboken så symbolerna matchar legendkortet.

### Rensat

- Tog bort äldre preview-PDF:er som ersatts av `output/print/`.

### Kommentar

- Print-output kan återskapas från källfiler och mallar.
```

---

## 16. Exempel på datadriven legend

```yaml
legend_card:
  id: main_legend
  format: A6
  title: Snabbreferens
  sections:
    - id: turn_order
      title: Din tur
      items:
        - Dra 1 kort.
        - Gör upp till 2 handlingar.
        - Lös rutan där du stannar.
    - id: symbols
      title: Symboler
      symbols:
        - icon: battle
          label: Utmaning
        - icon: reward
          label: Belöning
        - icon: forest
          label: Skog
    - id: remember
      title: Kom ihåg
      items:
        - Max 5 kort på hand.
        - Kontrollera vinst i slutet av din tur.
```

Detta är ett exempel på hur en återkommande komponent kan göras återgenererbar.

---

## 17. Exempel på datadrivna varianter

```yaml
variants:
  - id: basic
    name: Grundspel
    rulebook: docs/rulebooks/basic-rules.md
    recommended_age: 7+
    play_time_minutes: 20
    components:
      - board_main
      - deck_basic
      - tokens_energy

  - id: adventure
    name: Äventyrsläge
    rulebook: docs/rulebooks/adventure-mode-rules.md
    recommended_age: 9+
    play_time_minutes: 30
    components:
      - board_main
      - deck_adventure
      - deck_events
      - tokens_energy
      - tokens_reward
```

GPT:n bör använda variantdata för att undvika att spellägen blandas ihop.

---

## 18. Exempel på print-layoutdata

```yaml
print_layouts:
  - id: cards_a4
    name: Spelkort A4
    component_type: cards
    source: data/cards.yaml
    output: output/print/cards-a4.pdf
    paper: A4
    columns: 3
    rows: 3
    cut_lines: true
    safe_margin_mm: 3

  - id: legend_a6
    name: A6-förklaringskort
    component_type: legend_card
    source: docs/legend-card.md
    output: output/print/legend-card-a6.pdf
    paper: A6
    cut_lines: true

  - id: tokens_a4
    name: Markörer A4
    component_type: tokens
    source: data/tokens.yaml
    output: output/print/tokens-a4.pdf
    paper: A4
    token_size_mm: 22
    cut_lines: true
```

---

## 19. Saker GPT:n inte ska kopiera från exempelprojektet

GPT:n ska inte:

- låsa alla projekt till samma tema
- återanvända varumärkesspecifika namn
- anta att alla spel behöver samma mappar
- anta att alla spel behöver samma antal PDF:er
- kopiera historiska output-spår
- betrakta gamla filer som standard
- skapa flera parallella printmappar utan tydlig orsak
- göra A6-kortet till en manual
- prioritera snygg output före spelbarhet
- skapa stora zippar med onödig historik

---

## 20. Saker GPT:n bör återanvända som arbetsmetod

GPT:n bör återanvända dessa principer:

- iterativ zip-leverans
- tydlig projektstatus
- changelog efter ändringar
- markdown som källa för regler
- YAML/JSON som källa för komponenter
- separerad output
- print-and-play som praktiskt produktionsmål
- rensning när gamla output-spår inte behövs
- legendkort som egen komponent
- separata regelböcker när varianter skiljer sig mycket
- små körningar i stället för stora omtag

---

## 21. Definition of Done för steg 8

Steg 8 är klart när kunskapspaketet innehåller ett exempelprojektmönster som:

- extraherar generella lärdomar från ett befintligt projekt
- inte låser GPT:n till Pokémon eller något annat specifikt tema
- beskriver projektstruktur
- beskriver relation mellan källfiler och output
- beskriver hur varianter kan hanteras
- beskriver legendkort som komponent
- beskriver print-output och rensning
- beskriver byggsteg/generatorer
- beskriver validering
- ger exempel på projektstatus, changelog, legenddata, variantdata och print-layoutdata
- tydligt säger vad GPT:n inte ska kopiera
- tydligt säger vilka arbetsmetoder GPT:n bör återanvända
