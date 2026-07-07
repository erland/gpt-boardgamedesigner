# Print-and-play-produktionsguide för Brädspelsdesigner

Detta dokument beskriver hur GPT:n **Brädspelsdesigner** bör tänka kring fysisk produktion av brädspel som skrivs ut hemma eller i enkel kopierings-/tryckmiljö.

Syftet är att GPT:n ska kunna hjälpa användaren skapa komponenter som faktiskt går att skriva ut, klippa, laminera, montera och använda vid spelbordet.

Print-and-play är inte bara en export till PDF. Det är ett produktionssätt med egna begränsningar, kompromisser och designbeslut.

---

## 1. Grundprinciper

### 1.1 Designa för hemmaskrivare

Utgå från att användaren kan ha:

- A4-skrivare
- begränsade marginaler
- vanlig färglaserskrivare eller bläckstråleskrivare
- A4-lamineringsfickor
- sax
- enkel pappersskärare
- skärmatta och hobbykniv ibland
- begränsad möjlighet till dubbelsidig exakt passning

GPT:n ska inte anta att användaren har professionell printshop-utrustning.

### 1.2 Källfil och output ska skiljas åt

Printfiler ska normalt ligga i `output/print/`.

Källor ska ligga i exempelvis:

- `data/cards.yaml`
- `data/tokens.yaml`
- `data/board.yaml`
- `data/print-layouts.yaml`
- `docs/rulebook.md`
- `docs/legend-card.md`
- `templates/`

När en printfil ändras bör GPT:n i första hand uppdatera källan eller mallen.

### 1.3 Snyggt men praktiskt

En print-and-play-komponent ska vara:

- läsbar
- enkel att skära ut
- robust nog efter laminering
- rimlig i tonerförbrukning
- tydlig även om utskriften inte blir perfekt
- möjlig att producera i rimlig tid

### 1.4 Testa i låg kvalitet först

GPT:n bör rekommendera:

1. skriv ut en testsida
2. kontrollera storlek och läsbarhet
3. kontrollera marginaler
4. kontrollera skärlinjer
5. justera layout
6. skriv ut slutversion

---

## 2. Standardformat

### 2.1 A4 som bas

A4 bör vara standard om användaren inte säger annat.

A4-mått:

```text
210 × 297 mm
```

GPT:n bör tänka på att många skrivare inte kan skriva hela vägen ut till kanten.

Rekommenderad säker marginal:

```text
10 mm
```

Minsta rimliga marginal vid hemmaskrivare:

```text
5 mm
```

Men 5 mm kan vara riskabelt på vissa skrivare.

### 2.2 A6 som referenskort

A6-mått:

```text
105 × 148 mm
```

A6 är lämpligt för:

- förklaringslegend
- turöversikt
- symbolnyckel
- snabb referens
- liten spelarhjälp

På ett A4 får man plats med fyra A6-sidor, men vid hemmaklippning kan det vara bättre med något större marginal mellan dem.

### 2.3 Kortstorlekar

Vanliga riktvärden:

| Typ | Cirka mått | Kommentar |
|---|---:|---|
| Pokerkort | 63 × 88 mm | Vanlig och bekant storlek |
| Bridge-kort | 57 × 89 mm | Smalare, mer plats per ark |
| Mini-kort | 44 × 68 mm | Bra för små effekter, sämre läsbarhet |
| Små prototypkort | ca 50 × 70 mm | Praktiskt för A4 |
| A6-referens | 105 × 148 mm | Bra för spelarhjälp |

GPT:n bör inte låsa sig till standardmått om A4-layouten kräver anpassning, men ska tydligt beskriva kompromissen.

---

## 3. A4-layout för kort

### 3.1 Vanliga upplägg

#### 3 × 3 kort per A4

Passar för större kort.

Fördelar:

- bättre läsbarhet
- närmare pokerstorlek
- mer plats för ikon och text
- bra för barn/familjespel

Nackdelar:

- färre kort per ark
- mer papper

#### 4 × 4 kort per A4

Passar för små kort eller prototypkort.

Fördelar:

- många kort per ark
- kompakt
- bra för testkort med lite text

Nackdelar:

- liten text
- sämre för barn
- svårare att få snyggt om korten har mycket information

#### 2 × 4 kort per A4

Passar för stora kort, rollkort eller referenskort.

### 3.2 Riktlinje

GPT:n bör rekommendera:

- barnspel: hellre större kort, exempelvis 3 × 3
- familjespel: 3 × 3 eller 4 × 4 beroende på textmängd
- prototyp med väldigt lite text: 4 × 4
- referenskort/rollkort: 2 × 2, 2 × 3 eller A6

### 3.3 Kortmarginaler

Mellan kort bör det finnas lite mellanrum eller tydliga skärlinjer.

Rekommenderat:

```text
2–4 mm mellan kort
```

Om kort ska lamineras efter att de klippts ut behövs mer marginal runt varje kort.

---

## 4. Skärlinjer, bleed och säkerhetszon

### 4.1 Skärlinjer

Skärlinjer hjälper användaren att klippa eller skära rakt.

GPT:n bör föreslå skärlinjer för:

- kortark
- markörark
- tiles
- A6-kort
- flersidiga spelbräden

Skärlinjer ska vara tunna och inte störa komponenterna.

### 4.2 Säkerhetszon

Viktig text och symboler bör inte ligga nära kanten.

Rekommendation:

```text
Minst 3 mm från komponentkant
```

För barnkomponenter eller handklippning:

```text
4–5 mm
```

### 4.3 Bleed

Bleed innebär att bakgrund/grafik fortsätter utanför skärlinjen så att inga vita kanter uppstår vid skärning.

För hemmabruk är full bleed ofta svårt eftersom skrivare har marginaler.

GPT:n bör tänka så här:

- För prototyp: undvik full bleed.
- För snygg PnP: använd ljus bakgrund och tydliga ramar.
- För professionell tryckfil: bleed kan behövas, men det är ett senare steg.

### 4.4 Cut-safe design

För hemmaklippning bör komponenter helst ha:

- tydlig ram
- ljus eller neutral kant
- inte viktig grafik ända ut till kanten
- text långt från kanten
- tolerans för sned klippning

---

## 5. Laminering

### 5.1 Två huvudmetoder

#### Metod A: Laminera hela A4 och klipp efteråt

Fördelar:

- snabbt
- enkelt
- kräver få moment
- bra för spelplaner, referensark och temporära komponenter

Nackdelar:

- varje enskilt kort får inte förseglad plastkant
- kan separera vid kanten om korten hanteras mycket
- mindre robust för lösa kort

#### Metod B: Klipp först, laminera med mellanrum, klipp igen

Fördelar:

- varje kort får plastkant
- mer hållbart
- bättre för kort och markörer som blandas ofta

Nackdelar:

- mer arbete
- kräver noggrann placering i lamineringsficka
- fler klippmoment

### 5.2 GPT:ns rekommendation

För prototyp:

```text
Skriv ut på lite tjockare papper och laminera hela A4 om du vill testa snabbt.
```

För mer hållbara kort:

```text
Klipp ut korten först, laminera med 3–5 mm mellanrum och klipp sedan ut med plastkant.
```

### 5.3 Markörer

För markörer kan GPT:n föreslå:

- laminera hela arket och klipp fyrkantigt
- använd tjockare papper innan laminering
- montera på kartong före laminering om de ska kännas stadigare
- använd cirkelstans om användaren vill ha runda markörer

### 5.4 Undvik för små delar

Mycket små laminerade delar blir svåra att hantera.

Riktvärden:

- undvik tokens under 15 mm
- barnspel: helst minst 22 mm
- runda markörer: 20–25 mm eller större

---

## 6. Papper och tjocklek

### 6.1 Vanligt kopieringspapper

Bra för:

- testutskrifter
- regelblad
- snabba prototyper

Nackdel:

- tunt
- genomskinligt
- dålig kortkänsla

### 6.2 120–160 g/m²

Bra för:

- prototypkort
- referenskort
- markörark
- enklare spelbräden

### 6.3 200–250 g/m²

Bra för:

- stabilare kort
- tiles
- markörer
- spelplaner

Nackdel:

- alla skrivare klarar inte tjockt papper
- laminering blir stelare

### 6.4 Rekommendation

GPT:n bör ofta rekommendera:

- regler: vanligt eller 100–120 g/m²
- kort: 160–200 g/m² om skrivaren klarar det
- markörer: 160–250 g/m² eller montera på kartong
- spelbräde: 160–200 g/m², eventuellt laminera
- A6-referenskort: 160–200 g/m² + laminering

---

## 7. Kortproduktion

### 7.1 Snabb prototyp

1. Skriv ut kortark.
2. Klipp eller skär ut.
3. Lägg eventuellt korten i sleeves med vanliga spelkort bakom.

Fördelar:

- snabbt
- lätt att ändra
- ingen laminering krävs

### 7.2 Hållbar PnP-version

1. Skriv ut på tjockare papper.
2. Klipp ut korten grovt.
3. Laminera med mellanrum.
4. Klipp ut med plastkant.
5. Runda hörn om möjligt.

### 7.3 Sleeves

Sleeves är ofta bättre än laminering för kort som ska blandas.

GPT:n kan föreslå:

- skriv ut framsidor på vanligt papper
- klipp ut
- stoppa i sleeve framför ett vanligt spelkort
- använd ogenomskinliga sleeves om baksidan spelar roll

Fördelar:

- lätt att byta ut kort efter balansändringar
- bättre blandningskänsla
- mindre arbete än individuell laminering

---

## 8. Markörproduktion

### 8.1 Fyrkantiga markörer

Fördelar:

- enkla att klippa
- passar pappersskärare
- lätt att laminera
- bra för första prototyp

Nackdel:

- kan kännas mindre “speliga” än runda

### 8.2 Runda markörer

Fördelar:

- ser mer färdiga ut
- bra för resurser och poäng

Nackdel:

- svårare att klippa
- bäst med cirkelstans
- kräver exakt placering om motivet ska centreras

### 8.3 Rekommendation

GPT:n bör rekommendera fyrkantiga eller avrundade fyrkantiga markörer i första versionen, och runda markörer först när användaren har stans eller vill lägga mer arbete på produktionen.

### 8.4 Tokenark

Ett tokenark bör ha:

- tydlig markörform
- lite mellanrum
- skärlinjer
- symbol + eventuell kort text
- inte för mycket färgyta
- grupperade markörer efter typ

---

## 9. Spelbrädesproduktion

### 9.1 Enkelt A4-bräde

Bra för:

- första prototyp
- barnspel
- kortare spel
- enkel bana eller nodkarta

Fördelar:

- lätt att skriva ut
- lätt att laminera
- lätt att ersätta

### 9.2 Flersidigt bräde

Om brädet kräver mer yta kan GPT:n föreslå:

- 2 × A4 som tejpas ihop
- 4 × A4 för större karta
- vikbar konstruktion senare

Men GPT:n bör varna för:

- passningsproblem
- mer klippning/tejping
- svårare laminering
- större bordsyta

### 9.3 Bräde som ska lamineras

För A4-bräde:

- skriv ut på 160–200 g/m²
- laminera hela arket
- klipp inte för nära kanten
- låt gärna A4-formatet vara kvar om möjligt

### 9.4 Bräde med mycket färg

GPT:n bör föreslå tonerbesparande alternativ:

- ljus bakgrund
- dekorativa detaljer runt kanter
- tydliga noder/rutor
- illustrationer som inte täcker hela arket
- utskriftsvänlig variant med mindre färg

---

## 10. Tiles

Tiles kräver mer precision än kort.

### 10.1 Fyrkantiga tiles

Rekommenderas för första PnP-version.

Fördelar:

- lätt att skära
- lätt att lägga kant mot kant
- bra för rutnät och kartbygge

### 10.2 Hex-tiles

Fördelar:

- snyggt för kartor
- naturligare riktningar

Nackdel:

- svårare att klippa
- kräver mer precision
- kan bli ojämnt på hemmaskrivare

### 10.3 Rekommendation

GPT:n bör föreslå:

- börja med fyrkantiga tiles
- använd tydliga kanter
- undvik full bleed
- ha id eller diskret markering i hörn om tiles behöver identifieras

---

## 11. Regelbok och dokument

### 11.1 Regelbok

Regelboken kan produceras som:

- markdown
- PDF
- häfte
- A4-sidor
- A5-häfte senare

För första version bör GPT:n oftast föreslå:

```text
A4 PDF med tydliga rubriker och exempel.
```

### 11.2 Snabbstart

Snabbstart bör vara:

- 1 sida A4
- eller 2 sidor A5
- enkel att skriva ut separat

### 11.3 Referenskort

Referenskort bör vara:

- A6
- eller 2–4 per A4
- gärna laminerat
- kort nog att användas under spel

---

## 12. Färg, kontrast och tonerförbrukning

### 12.1 Färg ska inte bära all information

Använd:

- färg + ikon
- färg + text
- färg + form
- färg + placering

### 12.2 Kontrast

Viktig text ska ha hög kontrast.

Undvik:

- mörk text på mörk bakgrund
- tunn text på mönstrad bakgrund
- liten vit text på färgade fält
- för långa textblock på illustration

### 12.3 Tonerbesparing

GPT:n bör föreslå:

- ljus bakgrund
- färgade ramar i stället för helfärgade kort
- ikoner i stället för stora färgfält
- separat “ink friendly”-version
- undvika fotobakgrunder på alla kort i prototyp

---

## 13. Dubbelsidig utskrift

Dubbelsidig utskrift hemma är ofta svår att passa exakt.

### 13.1 Risker

- framsida och baksida hamnar snett
- skrivaren skalar olika
- fel vändning
- kortbaksidor avslöjar korttyp
- skärlinjer matchar inte

### 13.2 Alternativ

GPT:n bör föreslå:

- sleeves med gemensam baksida
- enkelsidig utskrift med ogenomskinliga sleeves
- separata baksidor som inte behöver exakt passning
- vikbara kort om lämpligt
- kort utan hemlig baksida om spelet tillåter

### 13.3 När dubbelsidigt är rimligt

Dubbelsidigt kan vara rimligt för:

- regelblad
- referenskort
- spelarmattor
- kort där baksidan inte måste passa exakt
- professionell print senare

---

## 14. PDF-export

### 14.1 Outputstruktur

Rekommenderad output:

```text
output/
  print/
    cards-a4.pdf
    tokens-a4.pdf
    board-a4.pdf
    legend-card-a6.pdf
    rulebook.pdf
  preview/
    cards-preview.png
    board-preview.png
```

### 14.2 PDF-krav

Print-PDF bör ha:

- korrekt sidstorlek
- inga oväntade skalningar
- tydliga marginaler
- skärlinjer
- inbäddade eller standardsäkra typsnitt
- tillräcklig upplösning på bilder
- tydlig filnamngivning

### 14.3 Filnamn

Bra filnamn:

```text
cards-a4-v0.2.pdf
tokens-a4-v0.2.pdf
rulebook-v0.2.pdf
```

Om versionering redan sker i mappar/changelog kan enklare namn användas:

```text
cards-a4.pdf
tokens-a4.pdf
rulebook.pdf
```

GPT:n bör vara konsekvent.

---

## 15. Print-layoutdata

Större projekt bör ha `data/print-layouts.yaml`.

Exempel:

```yaml
print_layouts:
  - id: cards_adventure_a4_3x3
    name: Äventyrskort A4 3x3
    component_type: cards
    source: data/cards.yaml
    output: output/print/adventure-cards-a4.pdf
    paper: A4
    columns: 3
    rows: 3
    card_width_mm: 63
    card_height_mm: 88
    cut_lines: true
    safe_margin_mm: 3

  - id: tokens_resources_a4
    name: Resursmarkörer A4
    component_type: tokens
    source: data/tokens.yaml
    output: output/print/resource-tokens-a4.pdf
    paper: A4
    token_shape: square
    token_size_mm: 22
    cut_lines: true
```

GPT:n bör använda detta när projektet har flera komponenttyper eller flera printark.

---

## 16. Produktionsguide i projektet

Varje seriöst print-and-play-projekt bör ha:

```text
docs/production-guide.md
```

Den bör innehålla:

- vad som ska skrivas ut
- rekommenderat papper
- om något bör lamineras
- hur kort ska skäras
- hur markörer ska skäras
- om sleeves rekommenderas
- vilka filer som är printklara
- vilka filer som bara är preview
- monteringsordning

Exempelstruktur:

```markdown
# Produktionsguide

## Skriv ut

- `output/print/cards-a4.pdf`
- `output/print/tokens-a4.pdf`
- `output/print/board-a4.pdf`
- `output/print/rulebook.pdf`

## Rekommenderat material

- Kort: 160–200 g/m² eller sleeves
- Markörer: 200 g/m² eller monteras på kartong
- Spelbräde: 160–200 g/m² och laminering

## Montering

1. Skriv ut kortarken.
2. Skär längs skärlinjerna.
3. Stoppa korten i sleeves eller laminera.
4. Skriv ut och laminera spelbrädet.
```

---

## 17. Kontroll före utskrift

GPT:n bör föreslå en printchecklista.

### 17.1 PDF-kontroll

- Är sidstorleken A4?
- Är “skala till sida” avstängt om exakt storlek behövs?
- Finns marginaler?
- Är skärlinjer synliga?
- Är text läsbar?
- Är all viktig information innanför säkerhetszonen?
- Är filen rätt version?

### 17.2 Komponentkontroll

- Matchar antal kort komponentlistan?
- Matchar markörantal reglerna?
- Finns spelbrädet?
- Finns referenskortet?
- Finns regelbok/snabbstarter?
- Finns alla symboler i legend?

### 17.3 Testutskrift

GPT:n bör ofta rekommendera att först skriva ut:

- en sida kort
- en sida markörer
- ett utsnitt av spelbrädet
- A6-referenskortet

---

## 18. Hemmaproduktion med få verktyg

När användaren vill producera med få verktyg bör GPT:n föreslå:

### Minsta verktyg

- skrivare
- sax
- linjal
- A4-lamineringsfickor om laminering önskas
- eventuell pappersskärare

### Bättre men fortfarande enkelt

- enkel rullskärare/pappersskärare
- hörnrundare
- skärmatta
- hobbykniv
- sleeves
- cirkelstans för markörer

### Praktiskt råd

GPT:n bör inte förutsätta att användaren köper nya verktyg, men kan föreslå vad som ger mest förbättring per insats.

Ofta mest värdefullt:

1. pappersskärare
2. sleeves
3. hörnrundare
4. cirkelstans om spelet har många runda markörer

---

## 19. Vanliga produktionsproblem

### 19.1 Kort blir för små

Lösning:

- minska antal kort per A4
- korta texten
- använd större typsnitt
- flytta detaljer till regelbok eller referenskort

### 19.2 Laminering släpper i kanten

Orsak:

- kort klippt efter helarks-laminering
- ingen plastkant runt komponenten

Lösning:

- klipp först, laminera med mellanrum, klipp sedan med plastkant
- använd sleeves för kort

### 19.3 Dubbelsidigt passar inte

Lösning:

- undvik exakt passning
- använd sleeves
- använd enkelsidiga kort
- gör baksidan utan viktig kantgrafik

### 19.4 För mycket färg går åt

Lösning:

- skapa ink-friendly-version
- ljusa bakgrunder
- färgade ramar i stället för helfärg
- färre fotobakgrunder

### 19.5 Markörer är svåra att klippa

Lösning:

- gör dem fyrkantiga
- öka storlek
- lämna mer mellanrum
- använd cirkelstans om runda behövs

---

## 20. Rekommendation per komponent

| Komponent | Första prototyp | Snyggare PnP |
|---|---|---|
| Spelkort | Enkelsidigt, text/ikon | Sleeves eller individuell laminering |
| Spelbräde | A4, enkel karta | Laminerat A4 eller 2×A4 |
| Markörer | Fyrkantiga, 20–25 mm | Tjockare papper, ev. cirkelstans |
| Referenskort | A6, enkel layout | Laminerat A6 |
| Regelbok | A4 PDF/Markdown | Snygg PDF, ev. häfteslayout |
| Tiles | Kvadratiska | Tjockare papper/kartong |
| Pjäser | Lånade pjäser | Standees eller egna markörer |

---

## 21. När GPT:n ska föreslå print-output

GPT:n bör föreslå print-output när:

- reglerna är tillräckligt stabila för speltest
- komponentlistan är definierad
- kortdata eller markördata finns
- användaren ber om nedladdningsbara filer
- användaren vill testspela fysiskt

GPT:n bör vänta med avancerad grafisk output när:

- kärnloopen är oklar
- kortlistan ändras kraftigt
- målgruppen inte är bestämd
- komponentmängden är osäker
- reglerna inte är spelbara ännu

---

## 22. Print-and-play och zip-struktur

Printrelaterade filer bör organiseras så här:

```text
data/
  print-layouts.yaml

docs/
  production-guide.md

templates/
  print-sheets/
  cards-a4.html
  tokens-a4.html
  legend-a6.html

scripts/
  build_printables.py

output/
  print/
    cards-a4.pdf
    tokens-a4.pdf
    board-a4.pdf
    legend-card-a6.pdf
  preview/
    cards-preview.png
    tokens-preview.png
```

GPT:n ska undvika att blanda gamla printspår med aktuella printspår.

Om flera spår finns bör GPT:n föreslå rensning eller tydlig märkning.

---

## 23. Rekommenderat arbetssätt för printproduktion

När användaren ber om printbara komponenter bör GPT:n:

1. kontrollera komponentkällor
2. kontrollera komponentantal
3. välja lämpligt A4-upplägg
4. skapa eller uppdatera `data/print-layouts.yaml`
5. skapa eller uppdatera mallar om relevant
6. generera output i `output/print/`
7. skapa preview om relevant
8. uppdatera `docs/production-guide.md`
9. uppdatera `PROJECT_STATUS.md`
10. uppdatera `CHANGELOG.md`
11. paketera zip om användaren ber om det

---

## 24. A6-förklaringskort som produktionsfil

A6-förklaringskort bör ha två nivåer:

### Källa

```text
docs/legend-card.md
```

eller

```text
data/legend-card.yaml
```

### Output

```text
output/print/legend-card-a6.pdf
```

Eventuellt även:

```text
output/print/legend-cards-a4.pdf
```

där flera A6-kort ligger på ett A4.

GPT:n ska tänka på att A6-kortet ska vara ett spelhjälpmedel vid bordet, inte en komprimerad regelbok.

---

## 25. Ink-friendly-läge

Större projekt bör överväga två printvarianter:

```text
output/print/color/
output/print/ink-friendly/
```

Ink-friendly bör ha:

- vit eller ljus bakgrund
- mindre stora färgfält
- tydliga svarta linjer
- ikoner och text som fungerar i gråskala
- samma komponentstorlekar som färgversionen

GPT:n bör föreslå detta om spelet har mycket färg eller många sidor.

---

## 26. Kvalitetsnivåer för print-output

### 26.1 Draft

- snabb
- enkel layout
- kan ha enklare typografi
- fokus på speltest

### 26.2 Playtest

- tydliga komponenter
- korrekta antal
- skärlinjer
- tillräckligt snyggt för flera spelomgångar

### 26.3 Shareable

- snyggare layout
- bättre regelbok
- konsekvent grafisk stil
- enklare produktionsguide
- rimlig balans

### 26.4 Production-like

- stabila regler
- genomarbetad layout
- högupplösta bilder
- noggrann marginal/bleed
- färdig produktionsguide
- noggrant korrekturläst

GPT:n bör hjälpa användaren välja rätt nivå.

---

## 27. Definition of Done för steg 5

Steg 5 är klart när kunskapspaketet innehåller en print-and-play-guide som beskriver:

- A4 som basformat
- A6-förklaringskort
- kortstorlekar
- kortlayout på A4
- skärlinjer
- säkerhetszon
- bleed
- laminering
- papperstjocklek
- kortproduktion
- markörproduktion
- spelbrädesproduktion
- tiles
- regelbok och dokument
- färg, kontrast och tonerförbrukning
- dubbelsidig utskrift
- PDF-export
- print-layoutdata
- produktionsguide
- kontroll före utskrift
- hemmaproduktion med få verktyg
- vanliga produktionsproblem
- zip-struktur för printoutput
- arbetssätt för printproduktion
- ink-friendly-läge
- kvalitetsnivåer för print-output
