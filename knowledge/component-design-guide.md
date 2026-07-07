# Komponentstandard för Brädspelsdesigner

Detta dokument beskriver hur GPT:n **Brädspelsdesigner** bör tänka kring komponenter i brädspelsprojekt.

Syftet är att GPT:n ska kunna hjälpa användaren att skapa, strukturera och vidareutveckla fysiska spelkomponenter på ett sätt som fungerar för print-and-play, prototypande, speltest och senare produktion.

Komponenter ska inte bara bli snygga. De ska vara:

- spelbara
- tydliga
- utskrivbara
- lätta att klippa ut eller montera
- konsekvent namngivna
- möjliga att ändra i källfiler
- rimliga för målgruppen
- kopplade till spelets regler och kärnloop

---

## 1. Grundprinciper för komponentdesign

### 1.1 Komponenten ska lösa ett spelproblem

Varje komponent ska ha ett tydligt syfte.

Frågor GPT:n bör ställa eller besvara:

- Vad gör komponenten i spelet?
- När används den?
- Behöver spelaren hålla den i handen, läsa den på bordet eller bara se en symbol?
- Är informationen på komponenten nödvändig?
- Kan komponenten förenklas eller kombineras med en annan?
- Är komponenten rimlig att producera hemma?

### 1.2 Spelbarhet före grafik

Grafisk stil är viktig, men komponenten måste först fungera.

Prioritet:

1. informationen är korrekt
2. informationen går att läsa
3. komponenten går att skriva ut
4. komponenten går att använda vid bordet
5. komponenten är estetiskt konsekvent
6. komponenten är vacker

### 1.3 En komponent ska ha en källa

GPT:n bör skapa komponenter från källfiler när det är praktiskt.

Exempel:

- kort från `data/cards.yaml`
- markörer från `data/tokens.yaml`
- spelplan från `data/board.yaml`
- legendkort från `docs/legend-card.md` eller `data/legend-card.yaml`
- regelbok från `docs/rulebook.md`
- printark från `data/print-layouts.yaml`

PDF, PNG och SVG i `output/` ska normalt betraktas som genererad output.

### 1.4 Designa för iteration

Första versionen ska vara lätt att ändra.

Undvik tidigt:

- för mycket specialgrafik
- låsta layoutbeslut
- stora mängder text på små komponenter
- avancerade symbolsystem innan reglerna är stabila
- manuellt skapade printark som inte går att uppdatera

---

## 2. Standardlista över komponenttyper

GPT:n bör känna igen och kunna hjälpa till med följande komponenter:

- spelkort
- spelbräde
- platsbrickor eller tiles
- markörer/tokens
- spelarpjäser
- resursmarkörer
- poängspår
- spelarmattor
- referenskort
- A6-förklaringskort/legendkort
- regelbok
- snabbstart
- scenarioblad
- uppdragskort
- händelsekort
- tärningar eller tärningstabeller
- kuvert eller separationskort för kampanjer
- printark
- klipp- och monteringsguide

Alla spel behöver inte alla komponenter.

GPT:n ska hellre föreslå en liten komponentuppsättning för första prototypen än en stor “färdig låda”.

---

## 3. Komponentlista

Varje spelprojekt bör ha en tydlig komponentlista.

Den kan ligga i:

- `docs/design-brief.md`
- `docs/rulebook.md`
- `data/game.yaml`
- separat `docs/component-list.md` om projektet är stort

Exempel:

```markdown
# Komponentlista

## Första spelbara prototyp

- 1 spelbräde, A4
- 36 äventyrskort
- 12 händelsekort
- 4 spelarpjäser
- 20 energimarkörer
- 1 regelbok
- 1 A6-referenskort

## Senare produktion

- illustrerade kort
- dubbelsidigt spelbräde
- tjockare markörer
- separata spelarmattor
```

Komponentlistan bör skilja på:

- minimum för speltest
- rekommenderad print-and-play-version
- möjlig framtida premiumversion

---

## 4. Spelkort

Spelkort är en av de vanligaste komponenterna.

GPT:n bör hjälpa användaren att definiera:

- korttyp
- syfte
- information på kortet
- antal kopior
- balansvärden
- ikonbehov
- textlängd
- printstorlek
- baksida
- sortering/deck

### 4.1 Vanliga korttyper

Exempel:

- händelsekort
- föremålskort
- uppdragskort
- fiendekort
- platskort
- rollkort
- handlingskort
- resurskort
- attackkort
- belöningskort
- modifierarkort
- referenskort

### 4.2 Rekommenderad kortdata

Kort bör beskrivas i `data/cards.yaml`.

Exempel:

```yaml
cards:
  - id: card_001
    name: Hitta en stig
    type: event
    deck: adventure
    count: 2
    cost: 0
    value: 1
    effect: Flytta 1 steg och dra 1 kort.
    flavor: Du hittar en smal stig mellan träden.
    tags: [movement, forest]
    icon: path
```

### 4.3 Fält för kort

Rekommenderade basfält:

```yaml
id: unik stabil identifierare
name: kortets namn
type: korttyp
deck: vilken kortlek kortet tillhör
count: antal kopior
effect: speleffekt
tags: sökbara/balanserbara etiketter
```

Valfria fält:

```yaml
cost: kostnad
value: värde
attack: attackvärde
defense: försvarsvärde
range: räckvidd
duration: varaktighet
flavor: stämningstext
icon: ikon
art_prompt: bildprompt
rarity: om spelet använder sällsynthet
target: mål för effekten
timing: när kortet får spelas
```

### 4.4 Textlängd på kort

Korttext ska vara kort.

Riktlinjer:

- barnspel: helst 1 enkel mening
- familjespel: 1–2 korta meningar
- hobbyspel: 2–4 rader om layouten tillåter
- referenssymboler bör användas när effekter återkommer

Dåligt:

```text
När du spelar detta kort får du omedelbart välja en annan spelare som befinner sig på samma ruta eller en angränsande ruta och tvinga den spelaren att kasta ett kort från handen, såvida inte den spelaren har en skyddsmarkör...
```

Bättre:

```text
Välj en spelare på din ruta eller intill. Den spelaren kastar 1 kort.
```

### 4.5 Kortstorlekar

Vanliga riktvärden för print-and-play:

- pokerstorlek: cirka 63 × 88 mm
- mini-kort: cirka 44 × 68 mm
- små referenskort: anpassade efter A4-layout
- barnspel kan gärna använda större kort om de ska vara lätta att läsa

GPT:n bör inte låsa sig vid exakt standardstorlek om användaren vill skriva ut många kort på A4, men bör vara tydlig med kompromissen mellan antal kort per ark och läsbarhet.

### 4.6 Kortlayout

Ett vanligt kort kan ha:

```text
[ Titel ]
[ Ikon / typ ]
[ Illustration eller symbolyta ]
[ Effekttext ]
[ Värden / kostnad / taggar ]
```

För första prototyp kan illustration ersättas av:

- ikon
- färgfält
- typmarkering
- enkel symbol
- tom bildruta

### 4.7 Kortbaksidor

Kortbaksidor bör användas när spelare inte ska se korttyp eller innehåll.

GPT:n bör tänka på:

- olika baksidor för olika kortlekar
- tonerförbrukning
- dubbelsidig utskrift kan vara svår hemma
- alternativ: skriv ut framsidor och använd sleeves med ogenomskinlig baksida

### 4.8 Balans av kort

GPT:n bör kunna gruppera kort efter:

- typ
- kostnad
- effektstyrka
- frekvens
- timing
- mål
- risk/belöning
- positiv/negativ effekt

Första kortuppsättningen bör vara liten.

Exempel:

- 12 kort för första mikrotest
- 24–36 kort för första prototyp
- 48–72 kort när systemet börjar stabiliseras

---

## 5. Spelbräde

Spelbrädet ska stödja spelets beslut, inte bara vara en dekorativ karta.

GPT:n bör identifiera vilken funktion brädet har:

- rörelsebana
- positionsstrid
- områdekontroll
- utforskning
- resursplacering
- karta
- poängspår
- rutnät
- nodkarta
- modulär tile-struktur

### 5.1 Vanliga brädetyper

#### Linjär bana

Bra för:

- barnspel
- race-spel
- enkla äventyr

Risk:

- få beslut om spelaren bara slår och går

#### Nätverk/nodkarta

Bra för:

- äventyr
- utforskning
- ruttval

Risk:

- otydliga kopplingar om grafiken är rörig

#### Rutnät

Bra för:

- taktisk rörelse
- strid
- placering

Risk:

- kan kännas mekaniskt om temat inte stöder det

#### Zonkarta

Bra för:

- områdekontroll
- samarbets- och äventyrsspel
- förenklad position

Risk:

- zoners relationer måste vara tydliga

#### Modulära tiles

Bra för:

- återspelbarhet
- utforskning
- dungeon crawl

Risk:

- fler komponenter och mer setup

### 5.2 Spelplansdata

Spelplan kan beskrivas i `data/board.yaml`.

Exempel:

```yaml
board:
  id: main_board
  name: Äventyrskartan
  format: A4
  type: node_map
  spaces:
    - id: start
      label: Start
      type: start
      x: 10
      y: 80
      connections: [forest_1]
    - id: forest_1
      label: Skog
      type: forest
      x: 25
      y: 65
      connections: [start, river_1, hill_1]
```

### 5.3 Information på spelbrädet

Ett spelbräde bör visa:

- startplats
- mål eller slutplats om relevant
- rutor/noder/zoner
- kopplingar
- terrängtyp
- specialsymboler
- poängspår om det används
- eventuell kortplacering
- eventuell discard-hög
- kort legend eller symbolnyckel om plats finns

### 5.4 A4 och flersidigt bräde

För print-and-play bör GPT:n tänka på:

- A4 som standard
- A3 kan skapas genom två A4
- marginaler för hemmaskrivare
- tydliga skär-/tejplinjer för flersidiga bräden
- att små rutor inte blir för små för pjäser och markörer

### 5.5 Bräde i första prototyp

För första speltest räcker ofta:

- enkla cirklar/noder
- enkel linje eller bana
- textetiketter
- enklare symboler
- inga detaljerade illustrationer

GPT:n bör hellre föreslå ett testbart bräde än en avancerad färdig karta.

---

## 6. Markörer och tokens

Markörer används för tillstånd, resurser, poäng, skador, energi, uppdrag eller objekt på brädet.

### 6.1 Vanliga markörtyper

- resursmarkörer
- skademarkörer
- energimarkörer
- poängmarkörer
- statusmarkörer
- målmarkörer
- låsta/öppna-markörer
- uppdragsmarkörer
- fiendemarkörer
- miljömarkörer
- runda/fasmarkörer

### 6.2 Token-data

Markörer bör beskrivas i `data/tokens.yaml`.

Exempel:

```yaml
tokens:
  - id: token_energy
    name: Energi
    type: resource
    shape: circle
    count: 24
    print_size_mm: 22
    icon: lightning
    color_hint: yellow
    notes: Används för att betala specialhandlingar.
```

### 6.3 Storlek

Riktvärden:

- små resurser: 15–18 mm
- standardmarkörer: 20–25 mm
- viktiga markörer: 25–30 mm
- barnspel: gärna större än 22 mm

GPT:n bör ta hänsyn till hur markörerna ska klippas ut. Runda markörer är snygga men svårare att klippa än fyrkantiga.

### 6.4 Form

Vanliga former:

- cirkel
- kvadrat
- hexagon
- hjärta
- stjärna
- enkel silhuett

För hemmaproduktion är kvadratiska eller avrundade fyrkantiga markörer ofta enklare än perfekta cirklar.

### 6.5 Text på markörer

Undvik mycket text.

Bra markörer använder:

- ikon
- siffra
- färg
- enkel bokstav
- form

Om text behövs bör den vara mycket kort.

---

## 7. Spelarpjäser

Spelarpjäser kan vara:

- vanliga pjäser från andra spel
- utskrivna standees
- färgade markörer
- mynt
- träkuber
- plastfigurer
- klippta papperspjäser

GPT:n bör inte alltid försöka skapa egna pjäser. För prototyp är det ofta bättre att använda befintliga föremål.

### 7.1 Standees

Om standees skapas bör GPT:n tänka på:

- tydlig fram- och baksida
- enkel silhuett
- fot/stöd
- inte för små detaljer
- utskrift på tjockare papper
- möjlighet att använda pappersklämma eller plastfot

---

## 8. Referenskort och spelarhjälp

Referenskort används för information som spelaren behöver ofta.

De bör innehålla:

- turordning
- handlingar
- symbolförklaring
- viktiga kostnader
- vinstvillkor
- korta påminnelser

De bör inte innehålla hela regelboken.

### 8.1 Referenskort-data

För mindre projekt kan referenskort beskrivas i markdown:

```markdown
# Spelarhjälp

## Din tur

1. Dra 1 kort.
2. Gör 2 handlingar.
3. Lös rutan du står på.

## Handlingar

- Flytta
- Spela kort
- Vila
```

För större projekt kan det ligga i `data/reference-cards.yaml`.

---

## 9. A6-förklaringskort / legendkort

A6-förklaringskortet ska kännas som ett spelhjälpmedel, inte som en manual.

Det ska vara:

- kompakt
- visuellt
- lätt att ha bredvid spelplanen
- fokuserat på symboler och turordning
- användbart under spel
- utskriftsvänligt

### 9.1 Innehåll

Ett A6-kort kan innehålla:

- spelets turordning
- de vanligaste symbolerna
- korta handlingar
- terrängförklaring
- vinstvillkor i en rad
- påminnelse om handgräns/resurser

### 9.2 Bra struktur

```markdown
# Snabbreferens

## Din tur

1. Dra kort
2. Gör 2 handlingar
3. Lös ruta
4. Nästa spelare

## Symboler

- ⚔ Strid
- ★ Belöning
- 🌲 Skog
- 💧 Vatten

## Kom ihåg

- Max 5 kort på hand.
- Du vinner när du har 3 stjärnor.
```

### 9.3 Dålig struktur

Ett A6-kort ska inte innehålla:

- långa regelavsnitt
- fullständig setup
- många undantag
- bakgrundshistoria
- detaljerade exempelrundor
- all korttext

### 9.4 Designprincip

A6-kortet ska svara på frågan:

> “Vad behöver spelaren påminnas om medan spelet pågår?”

Inte:

> “Hur lär jag mig hela spelet från början?”

---

## 10. Regelbok

Regelboken är en komponent, även om den är text.

GPT:n bör behandla regelboken som en spelkomponent med funktion:

- lära ut spelet
- lösa regelfrågor
- minska missförstånd
- stödja första spelomgången
- dokumentera variantregler

Regelboken bör ligga i:

```text
docs/rulebook.md
```

Genererade versioner bör ligga i:

```text
output/rulebooks/
```

### 10.1 Regelbok kontra snabbstart

Regelbok:

- komplett
- mer detaljerad
- innehåller exempel
- hanterar undantag

Snabbstart:

- kort
- hjälper spelaren börja spela
- hoppar över ovanliga undantag
- hänvisar till regelboken

---

## 11. Snabbstart

Snabbstarten bör vara 1–2 sidor.

Den bör svara på:

- Vad är målet?
- Vad behöver jag lägga fram?
- Vad gör jag på min tur?
- Hur vinner jag?
- Vad kan jag ignorera första gången?

Fil:

```text
docs/quickstart.md
```

---

## 12. Spelarmattor

Spelarmattor används när spelaren behöver organisera:

- kort
- resurser
- utrustning
- status
- karaktär
- handlingar
- byggnader
- poäng

GPT:n bör föreslå spelarmattor först när de verkligen hjälper.

Risk:

- ökar mängden utskrift
- kräver mer bordsyta
- kan kännas överproducerat i första prototyp

---

## 13. Tiles och modulära delar

Tiles kan användas för:

- utforskning
- rum
- landskap
- banbygge
- varierad setup

Data kan ligga i:

```text
data/tiles.yaml
```

Exempel:

```yaml
tiles:
  - id: tile_forest_crossing
    name: Skogskorsning
    type: forest
    connections: [north, east, south]
    effect: När du går in här, dra 1 händelsekort.
```

GPT:n bör vara försiktig med tiles i barnspel om setup blir för stor.

---

## 14. Tärningar

Tärningar kan vara:

- vanliga D6
- flera D6
- specialtärningar
- tärningstabeller
- digital slump
- kort som ersätter tärning

För print-and-play är vanliga D6 oftast enklast.

GPT:n bör undvika specialtärningar om de inte går att ersätta med:

- tabell
- kortlek
- klistermärken
- symbolkort
- vanlig D6 med översättning

Exempel:

```markdown
Slå en D6:

1–2: Miss
3–4: Träff
5: Stark träff
6: Bonus
```

---

## 15. Poängspår och mätare

Poängspår kan ligga på:

- spelbrädet
- separat ark
- spelarmatta
- regelblad
- kort

Används för:

- poäng
- runda
- hotnivå
- tid
- gemensam hälsa
- progression

GPT:n bör föreslå poängspår om det minskar behovet av lösa markörer.

---

## 16. Scenarier och uppdrag

Scenario- eller uppdragsblad passar för:

- äventyrsspel
- kampanjer
- coop
- barnspel med berättelse
- spel med målvariation

Filstruktur:

```text
docs/scenarios/
data/scenarios.yaml
```

Exempel:

```yaml
scenarios:
  - id: scenario_001
    name: Den försvunna nyckeln
    setup: Placera nyckelmarkören på Skogsgläntan.
    objective: Hämta nyckeln och återvänd till start.
    special_rules:
      - När en spelare går in i Grottan dras ett extra händelsekort.
```

---

## 17. Ikoner och symbolsystem

Ikoner bör användas för återkommande begrepp.

Bra användning:

- handlingstyper
- resurser
- terräng
- korttyp
- status
- mål
- fara
- belöning

Risker:

- för många ikoner
- ikoner utan legend
- ikoner som liknar varandra
- symboler som inte går att förstå i svartvitt
- symboler som blir för små vid utskrift

GPT:n bör föreslå en liten ikonuppsättning först.

Exempel:

```yaml
icons:
  movement: arrow
  battle: crossed_swords
  reward: star
  danger: warning
  forest: tree
```

---

## 18. Färgkodning

Färg är användbart men ska inte vara enda informationsbärare.

GPT:n bör tänka på:

- svartvit utskrift
- färgblindhet
- tonerförbrukning
- kontrast
- läsbarhet
- barn som snabbt ska tolka komponenter

Bra:

- färg + ikon + text
- färg + form
- färg + symbol

Sämre:

- bara färg för att skilja korttyper

---

## 19. Printark

Printark är output som samlar komponenter för utskrift.

Exempel:

```text
output/print/cards-a4.pdf
output/print/tokens-a4.pdf
output/print/board-a4.pdf
output/print/legend-card-a6.pdf
```

Printlayout bör beskrivas i:

```text
data/print-layouts.yaml
```

eller dokumenteras i:

```text
docs/production-guide.md
```

### 19.1 Kortark

Typiska upplägg:

- 3 × 3 kort per A4 för större kort
- 4 × 4 små kort per A4
- 2 × 4 större referenskort
- 1 eller 2 A6-kort per A4

### 19.2 Markörark

Markörark bör ha:

- tydliga skärlinjer
- lagom mellanrum
- gärna fyrkantiga ytterkanter för enkel klippning
- möjlighet till runda markörer om användaren har stans

---

## 20. Produktionsnivåer

GPT:n bör skilja på olika produktionsnivåer.

### 20.1 Nivå 1: Rå prototyp

- textkort
- enkla rutor
- inga illustrationer
- vanligt papper
- lånade pjäser
- handklippt

Syfte: testa om spelet fungerar.

### 20.2 Nivå 2: Spelbar print-and-play

- tydliga kort
- enkel grafisk layout
- skärlinjer
- regelbok
- A6-referenskort
- utskrivbara markörer
- färre manuella moment

Syfte: spela hemma flera gånger.

### 20.3 Nivå 3: Snygg prototyp

- konsekvent visuell stil
- bättre illustrationer
- förbättrade PDF:er
- tydligare komponentkvalitet
- mer professionell regelbok

Syfte: dela med andra och speltesta externt.

### 20.4 Nivå 4: Produktionsnära version

- stabila regler
- korrekt balanserade komponenter
- färdiga print-filer
- korrekt bleed/säkerhetszon om relevant
- genomarbetad grafisk profil
- tydlig licens- och källhantering

Syfte: publicering eller seriös distribution.

---

## 21. Komponentbeslut per målgrupp

### 21.1 Barnspel

Rekommendationer:

- få komponenttyper
- stora kort
- stora markörer
- tydliga symboler
- kort text
- enkel turordning
- gärna fysisk feedback

Undvik:

- många korttyper
- små ikoner
- långa effekter
- dolda undantagsregler
- mycket setup

### 21.2 Familjespel

Rekommendationer:

- tydlig komponentlista
- enkel setup
- referenskort
- lagom många kort
- visuellt stöd
- kort regelbok

Undvik:

- för mycket administration
- för många små markörer
- otydliga korttimingar

### 21.3 Hobbyspel

Rekommendationer:

- tydligare datafiler
- separata korttyper
- balansvärden
- referenskort
- scenariofiler
- playtestlogg

Undvik:

- att börja med för stor komponentmängd
- för många specialfall innan kärnloopen fungerar

---

## 22. Komponentgranskning

När GPT:n granskar ett projekt bör den kontrollera:

### 22.1 Fullständighet

- Finns alla komponenter som reglerna nämner?
- Nämner komponentlistan något som saknas i data/output?
- Finns antal för varje komponent?
- Finns printbar version?

### 22.2 Konsekvens

- Används samma namn i regler och data?
- Har korttyper samma stavning överallt?
- Matchar symboler legendkortet?
- Stämmer versioner i README, game.yaml och changelog?

### 22.3 Läsbarhet

- Är korttexten för lång?
- Är markörtexten för liten?
- Är symbolerna begripliga?
- Är referenskortet användbart under spel?

### 22.4 Produktion

- Får komponenterna plats på A4?
- Finns skärlinjer?
- Är det rimligt att klippa ut?
- Är tonerförbrukningen rimlig?
- Behövs dubbelsidig utskrift?

---

## 23. Vanliga misstag

GPT:n bör hjälpa användaren undvika:

- för många komponenter i första versionen
- för mycket korttext
- ikonförvirring
- flera parallella källor för samma komponent
- att bara ändra PDF utan att ändra källfil
- att göra grafiken färdig innan reglerna är testade
- att använda färg som enda informationsbärare
- för små markörer för barn
- spelbräde som bara är dekoration
- referenskort som blir en mini-regelbok
- zippar med gammal output som förväxlas med aktuell version

---

## 24. Rekommenderat arbetssätt när komponenter skapas

När användaren ber GPT:n skapa komponenter bör GPT:n arbeta så här:

1. Identifiera vilken spelmekanik komponenten stödjer.
2. Definiera minsta spelbara komponentuppsättning.
3. Skapa eller uppdatera källfil i `data/` eller `docs/`.
4. Säkerställ att reglerna nämner komponenten korrekt.
5. Föreslå print-layout.
6. Skapa output om användaren ber om det.
7. Uppdatera `PROJECT_STATUS.md`.
8. Uppdatera `CHANGELOG.md`.

---

## 25. Mall: komponentlista i markdown

```markdown
# Komponentlista

## Första spelbara prototyp

| Komponent | Antal | Källa | Kommentar |
|---|---:|---|---|
| Spelbräde | 1 | `data/board.yaml` | A4 |
| Äventyrskort | 36 | `data/cards.yaml` | 3×3 per A4 |
| Energimarkörer | 20 | `data/tokens.yaml` | Fyrkantiga för enkel klippning |
| Regelbok | 1 | `docs/rulebook.md` | Markdown, kan exporteras till PDF |
| Referenskort | 1 | `docs/legend-card.md` | A6 |
```

---

## 26. Mall: komponentdata i `data/game.yaml`

```yaml
components:
  - id: board_main
    name: Spelbräde
    type: board
    count: 1
    source: data/board.yaml
    output: output/board/main-board.pdf

  - id: deck_adventure
    name: Äventyrskort
    type: cards
    count: 36
    source: data/cards.yaml
    output: output/print/adventure-cards-a4.pdf

  - id: tokens_energy
    name: Energimarkörer
    type: tokens
    count: 20
    source: data/tokens.yaml
    output: output/print/energy-tokens-a4.pdf
```

---

## 27. Definition of Done för steg 3

Steg 3 är klart när kunskapspaketet innehåller en komponentstandard som beskriver:

- spelkort
- spelbräden
- markörer
- spelarpjäser
- referenskort
- A6-förklaringskort
- regelbok och snabbstart som komponenter
- spelarmattor
- tiles
- tärningar
- poängspår
- scenarier
- ikoner och färgkodning
- printark
- produktionsnivåer
- komponentgranskning
- vanliga misstag
- rekommenderat arbetssätt för komponentändringar
