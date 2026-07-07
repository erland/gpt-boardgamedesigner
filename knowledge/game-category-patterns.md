# Spelkategori-guide för Brädspelsdesigner

Detta dokument beskriver hur GPT:n **Brädspelsdesigner** bör känna igen, resonera kring och ge råd för olika typer av brädspel.

Syftet är att GPT:n ska kunna anpassa designråd, komponentförslag, regelstruktur, balansfrågor och print-and-play-produktion efter vilken typ av spel användaren vill skapa.

En spelidé kan ofta fungera i flera olika kategorier. GPT:n ska därför inte låsa användaren för tidigt, utan hjälpa till att välja den mest praktiska riktningen för målgrupp, speltid, material och produktionsnivå.

---

## 1. Grundprincip: kategori styr designbeslut

Spelkategorin påverkar nästan allt:

- vilka komponenter som behövs
- hur reglerna bör struktureras
- hur mycket text som är rimligt
- hur mycket slump spelet tål
- hur balans bör testas
- hur print-and-play-vänligt projektet blir
- hur lång utvecklingstiden blir
- hur lätt spelet är att förklara

GPT:n bör alltid försöka identifiera spelets huvudsakliga kategori eller hybridkategori tidigt.

Exempel:

```text
Det här verkar främst vara ett äventyrsspel med spelbräde och kortdrivna händelser.
```

eller:

```text
Idén kan fungera både som kortspel och som brädspel med rörelse. För första prototyp rekommenderar jag kortspel eftersom det kräver färre komponenter.
```

---

## 2. Hur GPT:n bör välja kategori

När användaren har en lös idé bör GPT:n bedöma:

1. målgrupp
2. önskad speltid
3. antal spelare
4. tema
5. typ av beslut spelaren ska fatta
6. önskad slumpnivå
7. materialbegränsningar
8. om spelet ska vara lätt att skriva ut hemma
9. om det ska gå snabbt att prototypa
10. om användaren vill ha berättelse, taktik, strategi eller enkel familjekänsla

GPT:n bör sedan föreslå 1–3 lämpliga kategorier.

För varje kategori bör GPT:n beskriva:

- varför den passar
- vilka komponenter som behövs
- vilka risker som finns
- hur första prototypen kan göras
- varför GPT:n rekommenderar eller avråder

---

## 3. Kategorier i korthet

| Kategori | Passar när | Typiska komponenter | Vanlig risk |
|---|---|---|---|
| Kortspel | Man vill ha liten komponentmängd | Kort, regelblad | För mycket korttext |
| Tärningsspel | Man vill ha snabb slump och enkelhet | Tärningar, tabeller, markörer | För lite spelarval |
| Bana/race | Man vill ha enkel rörelse | Spelbräde, pjäser, kort/tärning | Blir bara slå-och-gå |
| Nodkarta/äventyr | Man vill ha utforskning och vägval | Karta, kort, markörer | Otydliga regler och lång setup |
| Dungeon crawl | Man vill ha strid, rum och progression | Tiles, fiender, kort, markörer | För många komponenter |
| Worker placement | Man vill ha strategiska val om resurser | Bräde, arbetare, resurser | För tungt för enkel PnP |
| Deck-building | Man vill ha progression via kortlek | Många kort, markörer | Kräver många balanserade kort |
| Tile placement | Man vill bygga karta/mönster | Tiles, poängregler | Svår scoring |
| Area control | Man vill tävla om områden | Karta, pjäser, majoritetsmarkörer | Kan bli konfliktintensivt |
| Coop | Man vill att spelare samarbetar | Hotspår, eventkort, mål | Alfa-spelare styr alla |
| Barnspel | Man vill ha enkel, tydlig upplevelse | Få komponenter, stora symboler | För mycket text/regler |
| Familjespel | Man vill ha bred tillgänglighet | Lagom kort/bräde/markörer | För svag interaktion |
| Duellspel | Man vill ha 1 mot 1-konflikt | Kort, spelplan, resurser | Balans mellan sidor |
| Solo-spel | Man vill spela ensam | Automaregler, kort, tabeller | Administration tar över |

---

## 4. Kortspel

Kortspel passar när användaren vill ha:

- liten komponentmängd
- lätt print-and-play
- snabb prototyp
- kombinationer och effekter
- variation mellan omgångar
- möjlighet att bygga ut spelet senare

### 4.1 Typiska komponenter

- kortlek
- eventuellt separata korttyper
- regelblad
- referenskort
- markörer om spelet har resurser eller skada

### 4.2 Vanliga mekaniker

- dra kort
- spela kort
- samla set
- betala resurser
- bygga motor
- attack/försvar
- hand management
- push your luck
- trick-taking
- tableau building

### 4.3 Print-and-play-konsekvenser

Kortspel är ofta lätt att skriva ut, men kan snabbt kräva många kort.

GPT:n bör tänka på:

- antal kort per A4
- om korten behöver baksidor
- om korten kan sleeveas med vanliga spelkort bakom
- om korttexten är läsbar
- om första prototypen kan ha färre kort

### 4.4 Vanliga risker

- för många unika kort
- för mycket text
- obalanserade kortkombinationer
- för mycket blandning i leken
- för få meningsfulla val
- för svår regeltext för målgruppen

### 4.5 Bra första prototyp

Första prototyp:

- 18–36 kort
- 2–4 korttyper
- få nyckelord
- ingen avancerad grafik
- tydliga balansvärden

Exempel på första kortstruktur:

```yaml
cards:
  - id: card_001
    name: Samla ved
    type: action
    count: 3
    effect: Få 1 resurs.
    tags: [resource]
```

---

## 5. Tärningsspel

Tärningsspel passar när användaren vill ha:

- snabbhet
- enkel spänning
- fysisk känsla
- låga komponentkrav
- barn- eller familjevänlig slump

### 5.1 Typiska komponenter

- vanliga D6
- regelblad
- resultat-/poängark
- markörer
- eventuellt spelbräde

### 5.2 Vanliga mekaniker

- slå och välj
- slå om tärningar
- Yahtzee-liknande kombinationer
- risk/belöning
- tabeller
- rörelse
- attack/försvar

### 5.3 Print-and-play-konsekvenser

Vanliga D6 är bra eftersom de inte behöver skrivas ut.

Specialtärningar bör undvikas i första version om de inte kan ersättas av:

- tabell
- kort
- ikonöversättning
- färgade vanliga tärningar
- klistermärken

### 5.4 Vanliga risker

- spelaren har för få beslut
- resultat blir för slumpiga
- svårighetsgrad svänger för mycket
- tärningstabeller blir långsamma

### 5.5 Bra första prototyp

En bra första prototyp har:

- 1–3 D6
- kort tärningstabell
- tydligt val efter slaget
- enkel poäng eller progression

---

## 6. Spel med bana eller race

Denna kategori passar när spelet handlar om att ta sig från start till mål eller runt en bana.

Passar särskilt för:

- barnspel
- familjespel
- enkla äventyr
- lättförklarade print-and-play-spel

### 6.1 Typiska komponenter

- spelbräde
- pjäser
- tärning eller rörelsekort
- händelsekort
- markörer
- regelblad

### 6.2 Vanliga mekaniker

- slå och gå
- dra kort för rörelse
- välj väg
- specialrutor
- samla objekt
- undvik hinder
- först till mål
- uppfyll mål och återvänd

### 6.3 Risk: slå-och-gå

Den största risken är att spelaren inte fattar meningsfulla beslut.

GPT:n bör föreslå minst ett av följande:

- vägval
- handlingsval på turen
- resurser att spendera
- risk/belöning-rutor
- kort som modifierar rörelse
- uppdrag som gör att spelare vill olika saker

### 6.4 Bra första prototyp

Första prototyp:

- A4-bräde
- 20–35 rutor/noder
- 3–5 typer av rutor
- enkla händelsekort
- tydligt mål

---

## 7. Nodkarta och äventyrsspel

Nodkarta passar när spelet ska kännas som utforskning med vägval.

Passar för:

- äventyr
- skattjakt
- monsterjakt
- resa genom värld
- barn/familjeäventyr
- kampanj i lätt format

### 7.1 Typiska komponenter

- karta med noder
- pjäser
- eventkort
- uppdragskort
- resurser
- fiende- eller hinderkort
- referenskort
- regelbok

### 7.2 Vanliga mekaniker

- flytta längs kopplingar
- dra händelse på plats
- samla resurser
- lösa uppdrag
- slåss eller undvika faror
- hitta objekt
- låsa upp områden

### 7.3 Print-and-play-konsekvenser

Nodkartor är ofta mer utskriftsvänliga än rutnät eftersom kartan kan vara dekorativ men ändå tydlig.

GPT:n bör tänka på:

- tydliga linjer mellan noder
- lagom stora noder
- symboler för plats typer
- legendkort
- inte för många små texter på brädet

### 7.4 Vanliga risker

- för många platsregler
- för mycket text på kartan
- otydliga kopplingar
- för lång setup
- händelsekort gör att spelaren saknar kontroll

### 7.5 Bra första prototyp

Första prototyp:

- 10–18 noder
- 3–4 platstyper
- 20–30 händelsekort
- 3 enkla uppdrag
- en tydlig vinstförutsättning

---

## 8. Dungeon crawl

Dungeon crawl passar när spelet ska handla om rum, fiender, skatt och progression.

Passar för:

- äventyrsspel
- fantasy
- sci-fi
- taktisk strid
- solo/coop
- kampanj

### 8.1 Typiska komponenter

- tiles eller karta
- hjältekort
- fiendekort
- föremålskort
- tärningar
- skademarkörer
- statusmarkörer
- scenarier
- regelbok

### 8.2 Vanliga mekaniker

- utforska rum
- avslöja tiles
- turbaserad strid
- hitta loot
- levla upp
- slutföra scenario
- hantera hotnivå

### 8.3 Print-and-play-konsekvenser

Dungeon crawl kan bli komponenttungt.

GPT:n bör föreslå att första prototypen begränsas kraftigt:

- få rum
- få fiender
- få hjälteförmågor
- enkla standees eller markörer
- en karta i stället för många tiles om målet är snabb prototyp

### 8.4 Vanliga risker

- för många regler
- för mycket administration
- för lång speltid
- för många komponenter
- balansproblem mellan hjältar och fiender
- mycket jobb innan första speltest

### 8.5 Bra första prototyp

Första prototyp:

- 1 scenario
- 6–8 rum
- 2 hjälteroller
- 3 fiendetyper
- 10 föremålskort
- enkel strid
- max 30 minuter

---

## 9. Worker placement

Worker placement passar när spelare placerar arbetare på platser för att samla resurser och utföra handlingar.

Passar för:

- strategiska familjespel
- hobbyspel
- resurshantering
- byggspel
- ekonomiska spel

### 9.1 Typiska komponenter

- central spelplan
- arbetarpjäser
- resurser
- byggkort eller utvecklingskort
- poängspår
- regelbok
- referenskort

### 9.2 Vanliga mekaniker

- placera arbetare
- blockera platser
- samla resurser
- omvandla resurser
- bygga kort/byggnader
- poängmotor
- rundstruktur

### 9.3 Print-and-play-konsekvenser

Kan fungera bra print-and-play, men kräver tydligt bräde och ofta många små markörer.

GPT:n bör föreslå:

- få resurstyper
- få arbetsplatser i första prototyp
- enkla pjäser från annat spel
- tydligt referenskort

### 9.4 Vanliga risker

- för torr känsla
- för många resurser
- svår balans
- lång väntetid
- analysförlamning
- för tungt för yngre barn

### 9.5 Bra första prototyp

Första prototyp:

- 4–6 platser
- 2–3 resurser
- 2 arbetare per spelare
- 6 rundor
- enkel poängräkning

---

## 10. Deck-building

Deck-building passar när spelare börjar med svaga kort och gradvis bygger starkare kortlekar.

Passar för:

- progression
- motorbygge
- fantasy/sci-fi/äventyr
- duell eller coop
- spelare som gillar kombinationer

### 10.1 Typiska komponenter

- startkort
- marknadskort
- resurskort
- poängkort eller mål
- eventuellt spelbräde
- regelbok
- referenskort

### 10.2 Vanliga mekaniker

- dra hand
- spela kort
- få valuta
- köpa kort
- blanda discard till ny lek
- bygga motor
- attack eller målprogression

### 10.3 Print-and-play-konsekvenser

Deck-building kräver ofta många kort.

GPT:n bör föreslå:

- liten marknad i första prototyp
- få unika kort
- flera kopior
- tydlig kortmall
- sleeves om möjligt

### 10.4 Vanliga risker

- för många kort behövs innan spelet fungerar
- svår balans
- långa texter
- startlekar känns tråkiga
- dominanta kombinationer

### 10.5 Bra första prototyp

Första prototyp:

- 10 startkort per spelare
- 12 marknadskorttyper
- 3–5 kopior av varje
- enkel valuta
- tydligt vinstmål

---

## 11. Tile placement

Tile placement passar när spelare bygger en karta, stad, mönster eller nätverk.

Passar för:

- pusselkänsla
- spatiala beslut
- familjespel
- vackra print-and-play-komponenter
- återspelbarhet

### 11.1 Typiska komponenter

- tiles
- poängmarkörer
- spelarpjäser ibland
- poängblad
- regelbok
- referenskort

### 11.2 Vanliga mekaniker

- dra tile
- placera enligt regler
- matcha kanter
- skapa områden
- bygga rutter
- poäng för mönster
- blockera motståndare

### 11.3 Print-and-play-konsekvenser

Tiles kan vara mycket print-and-play-vänliga, men kräver noggrann klippning.

GPT:n bör tänka på:

- kvadratiska tiles är enklast
- hexar är snygga men svårare att klippa
- tjockare papper eller laminering hjälper
- tydliga kanter är viktiga

### 11.4 Vanliga risker

- scoring blir för svår
- tiles blir för lika
- setup tar lång tid
- felklippta tiles påverkar känslan
- svårt att blanda papperskomponenter

### 11.5 Bra första prototyp

Första prototyp:

- 16–24 tiles
- 3–4 tiletyper
- enkel poängregel
- inga specialundantag

---

## 12. Area control

Area control passar när spelare tävlar om kontroll över områden på en karta.

Passar för:

- konfliktspel
- strategispel
- politiskt/territoriellt tema
- fantasykrig i lätt form
- majoritetsmekanik

### 12.1 Typiska komponenter

- karta med områden
- pjäser/kuber
- kontrollmarkörer
- kort eller handlingar
- poängspår
- regelbok

### 12.2 Vanliga mekaniker

- placera enheter
- flytta enheter
- majoritet i områden
- konflikt
- områdesbonus
- runda-poäng
- allianser eller blockering

### 12.3 Print-and-play-konsekvenser

Fungerar bra om spelare kan använda kuber eller markörer från annat spel.

GPT:n bör tänka på:

- tydliga områdesgränser
- färger + symboler
- utrymme för många pjäser
- enkel konfliktlösning

### 12.4 Vanliga risker

- för aggressivt för familjespel
- kingmaking
- lång speltid
- otydlig kontroll
- svårt att balansera startpositioner

### 12.5 Bra första prototyp

Första prototyp:

- 6–10 områden
- 3 spelare eller 2 spelare med neutral mekanik
- enkel majoritetspoäng
- begränsat antal rundor

---

## 13. Co-op-spel

Co-op passar när spelare samarbetar mot spelet.

Passar för:

- äventyr
- familjespel
- barnspel utan direkt förlorarkänsla
- problemlösning
- gemensam berättelse
- solo-kompatibla spel

### 13.1 Typiska komponenter

- gemensamt mål
- hotspår
- eventkort
- rollkort
- gemensamma resurser
- karta eller uppdrag
- regelbok
- referenskort

### 13.2 Vanliga mekaniker

- gemensamt hot
- eventfas
- spelarfaser
- specialroller
- begränsad tid
- gemensam förlust
- delmål

### 13.3 Print-and-play-konsekvenser

Co-op kan vara komponentlätt eller komponenttungt beroende på hotsystemet.

GPT:n bör föreslå enkel hotmekanik i början:

- hotspår
- eventkort
- timer
- begränsat antal rundor
- få roller

### 13.4 Vanliga risker

- alfa-spelare styr alla
- spelet spelar sig själv
- svårighetsgrad svänger mycket
- för mycket administration
- för många undantag

### 13.5 Motverka alfa-spelare

GPT:n kan föreslå:

- dolda kort
- samtidiga val
- personlig information
- tidsgräns
- unika roller med egna beslut
- barnvänligt: “alla får bestämma sin egen handling”

### 13.6 Bra första prototyp

Första prototyp:

- 1 gemensamt mål
- 1 hotspår
- 20 eventkort
- 2–4 roller
- max 30 minuter

---

## 14. Barnspel

Barnspel är inte bara enklare vuxenspel. Det kräver egen designlogik.

Passar när målgruppen är ungefär 4–10 år, men reglerna måste anpassas efter ålder.

### 14.1 Designprinciper

- korta turer
- få val åt gången
- tydliga symboler
- lite text
- fysisk tydlighet
- snabb setup
- låg straffnivå
- gärna framåtrörelse
- spänning utan hård eliminering

### 14.2 Komponenter

- stora kort
- stora markörer
- tydlig spelplan
- få korttyper
- enkla pjäser
- kort regelblad
- referenskort för vuxen/läsande barn

### 14.3 Vanliga risker

- för mycket text
- långa väntetider
- negativ feedback
- för många undantag
- minnessystem som är för krävande
- symboler utan tydlig legend
- för små komponenter

### 14.4 Åldersriktlinjer

#### 4–6 år

- mycket enkel tur
- en handling i taget
- färg/form/symbol
- vuxen kan hjälpa till
- kort speltid, 5–15 min

#### 7–10 år

- enklare korttext fungerar
- 2–3 handlingstyper
- lätt strategi
- 15–30 min
- tydliga mål

#### 10–12 år

- mer taktik
- fler korttyper
- enkel progression
- 20–45 min

### 14.5 Bra första prototyp

Första prototyp:

- 1 A4-bräde
- 20 kort
- 3–4 symboler
- 4 pjäser
- 1 enkel vinstregel
- 10–20 minuter

---

## 15. Familjespel

Familjespel ska vara lätta att komma in i men ändå ge meningsfulla val.

Passar när spelet ska fungera för blandade åldrar och erfarenheter.

### 15.1 Designprinciper

- snabb setup
- tydligt mål
- enkel turstruktur
- lagom slump
- lagom strategi
- spelare ska känna att de påverkar
- reglerna ska kunna läras ut muntligt

### 15.2 Komponenter

- måttligt antal kort
- enkelt bräde eller central yta
- få markörtyper
- referenskort
- kort regelbok
- tydlig ikonografi

### 15.3 Vanliga risker

- för mycket hobbyspelskomplexitet
- för få val
- för lång speltid
- för mycket text
- för svag interaktion
- otydlig poängräkning

### 15.4 Bra första prototyp

Första prototyp:

- 20–40 minuter
- 2–4 spelare
- 2–4 handlingar per tur
- 3–5 komponenttyper
- enkel sluträkning

---

## 16. Duellspel

Duellspel är spel för två spelare med direkt konkurrens.

Passar för:

- strid
- kortkombinationer
- taktisk position
- snabb konflikt
- asymmetriska sidor

### 16.1 Typiska komponenter

- kortlekar
- liten spelplan
- enheter eller markörer
- hälsomätare
- resurser
- referenskort

### 16.2 Vanliga mekaniker

- attack/försvar
- positionering
- resurshantering
- bluff
- simultana val
- bygg egen strategi

### 16.3 Vanliga risker

- ena sidan är starkare
- förstaspelarfördel
- dominant strategi
- för hård snöbollseffekt
- mycket korttext

### 16.4 Bra första prototyp

Första prototyp:

- symmetriska startvillkor
- 12–20 kort per spelare
- få resurstyper
- tydlig vinst: reducera hälsa, nå mål eller samla poäng

---

## 17. Solo-spel

Solo-spel kräver att spelet ger motstånd utan mänsklig motspelare.

Passar för:

- pussel
- äventyr
- kampanj
- resursoptimering
- överlevnad
- high score

### 17.1 Typiska komponenter

- eventkort
- automaregler
- hotspår
- mål
- tabeller
- karta
- spelarbräde
- regelbok

### 17.2 Vanliga mekaniker

- automa
- slumpade händelser
- begränsat antal rundor
- målpoäng
- överlev så länge som möjligt
- scenarier

### 17.3 Vanliga risker

- för mycket administration
- ingen variation
- svårighetsgrad ojämn
- spelet känns som matteövning
- spelaren saknar meningsfulla val

### 17.4 Bra första prototyp

Första prototyp:

- tydligt mål
- enkel eventlek
- 1 hotspår
- 10–20 minuter
- få specialregler

---

## 18. Memory och spatiala barnspel

Denna kategori passar för yngre spelare och enkla familjespel.

### 18.1 Typiska komponenter

- brickor
- kort
- spelplan
- symboler
- enkla pjäser

### 18.2 Vanliga mekaniker

- hitta par
- komma ihåg plats
- vända brickor
- bygga mönster
- matcha symboler
- sortera färger/former

### 18.3 Vanliga risker

- för få beslut
- vuxna får för stor fördel
- för lång setup
- otydliga symboler
- komponenter blir små

### 18.4 Bra första prototyp

- 12–24 brickor
- 4–6 symboltyper
- enkel vinstregel
- kort speltid

---

## 19. Set collection

Set collection passar när spelare samlar kombinationer av kort, symboler eller resurser.

Passar för:

- familjespel
- kortspel
- äventyr
- handels-/samlartema
- barnspel med symboler

### 19.1 Typiska komponenter

- kort
- resurser
- mål- eller uppdragskort
- poängkort
- referens

### 19.2 Vanliga mekaniker

- samla tre lika
- samla olika symboler
- byta resurser
- uppfylla mål
- poäng för kombinationer

### 19.3 Risker

- för passivt spel
- för slumpigt drag
- otydlig poängräkning
- för mycket väntan

### 19.4 Bra första prototyp

- 4–6 symboler
- 30–50 kort
- enkla mål
- begränsad handstorlek

---

## 20. Push your luck

Push your luck passar när spelaren får välja mellan att säkra vinst eller riskera mer för större belöning.

Passar för:

- tärningsspel
- kortspel
- barn/familjespel
- skattjakt
- äventyr

### 20.1 Typiska komponenter

- kortlek
- tärningar
- belöningsmarkörer
- riskkort
- poängspår

### 20.2 Vanliga mekaniker

- dra ett kort till eller stanna
- slå igen eller säkra resultat
- samla belöning men riskera förlust
- fara ökar över tid

### 20.3 Risker

- ren slump utan strategi
- för hårda straff
- barn blir frustrerade
- optimal strategi blir självklar

### 20.4 Bra första prototyp

- enkel riskregel
- tydlig belöning
- korta rundor
- möjlighet att återhämta sig

---

## 21. Roll-and-write / flip-and-write

Passar när spelare fyller i ett ark baserat på tärningsslag eller kort.

### 21.1 Typiska komponenter

- spelblad
- penna
- tärningar eller kort
- regelblad

### 21.2 Fördelar

- mycket print-and-play-vänligt
- få komponenter
- lätt att distribuera
- bra för solo/familj

### 21.3 Risker

- kan kännas abstrakt
- kräver bra poängsystem
- spelbladet måste vara tydligt
- svårt att ändra ofta om många skriver ut

### 21.4 Bra första prototyp

- 1 A4-spelblad
- 2 D6
- 10–20 min
- enkel scoring

---

## 22. Hybridspel

Många bra spel är hybrider.

Exempel:

- äventyrsspel + kortdrivna händelser
- bana + set collection
- coop + dungeon crawl
- kortspel + deck-building
- tile placement + area control
- barnspel + memory
- roll-and-write + push your luck

GPT:n bör hjälpa användaren att identifiera huvudkategori och stödkategori.

Exempel:

```text
Jag skulle behandla detta som ett äventyrsspel med nodkarta som huvudkategori och kortdrivna händelser som stödsystem.
```

Det gör designbesluten tydligare.

---

## 23. Kategorival för första prototyp

När flera kategorier är möjliga bör GPT:n prioritera den som ger snabbast speltest.

Rangordning för enkel prototyp, generellt:

1. kortspel
2. tärningsspel
3. roll-and-write
4. enkelt bana/race-spel
5. nodkarta med händelsekort
6. tile placement
7. duellspel
8. coop med enkelt hotspår
9. worker placement
10. deck-building
11. dungeon crawl
12. större area control

Detta är inte en kvalitetsranking, utan en bedömning av prototypinsats.

---

## 24. Kategorival för print-and-play

Generellt mest print-and-play-vänligt:

- kortspel med få kort
- roll-and-write
- tärningsspel med vanliga D6
- enkel nodkarta
- enkel bana
- tile placement med kvadratiska tiles

Mer krävande print-and-play:

- dungeon crawl
- stora deck-builders
- många standees
- stora area control-kartor
- spel med många små tokens
- spel med dubbelsidiga kort/tiles

---

## 25. Kategorival för barnspel

För barn 7–10 år är ofta bäst:

- bana med meningsfulla val
- nodkarta med enkla händelser
- kortspel med kort text
- memory/spatial
- push your luck med milda straff
- enkelt coop

Var försiktig med:

- deck-building
- worker placement
- tung area control
- dungeon crawl med många statusar
- långa korttexter

---

## 26. Kategorival för familjespel

För familjespel är ofta bäst:

- set collection
- push your luck
- kortdrivet äventyr
- enkel worker placement
- tile placement
- bana/nodkarta med val
- roll-and-write
- coop med enkel hotmekanik

Viktigt:

- snabb setup
- tydlig turordning
- korta regler
- begripliga komponenter
- inga långa väntetider

---

## 27. Kategorival för hobbyspel

För hobbyspel kan GPT:n föreslå mer avancerade system:

- worker placement
- deck-building
- area control
- dungeon crawl
- asymmetriskt duellspel
- campaign/adventure
- engine building
- taktiskt rutnät

Men GPT:n bör fortfarande börja med en smal prototyp.

---

## 28. Balansfrågor per kategori

### Kortspel

- Är vissa kort alltid bättre?
- Är handstorleken lagom?
- Är draghastigheten lagom?
- Får spelarna meningsfulla val varje tur?
- Finns det för många specialfall?

### Tärningsspel

- Har spelaren val efter slaget?
- Är straff för dåliga slag rimliga?
- Är sannolikheter begripliga?
- Blir rundorna snabba?

### Bana/race

- Finns vägval?
- Kan spelaren påverka rörelse?
- Är specialrutor varierade men inte röriga?
- Blir någon spelare hopplöst efter?

### Nodkarta/äventyr

- Är alla vägar intressanta?
- Är händelser för slumpiga?
- Finns tydligt mål?
- Tar setup för lång tid?

### Dungeon crawl

- Är strid snabb nog?
- Behövs alla statusar?
- Är fiender olika utan att bli röriga?
- Är scenariot lagom långt?

### Worker placement

- Är alla platser användbara?
- Finns en dominant strategi?
- Är resursflödet lagom?
- Är väntetiden rimlig?

### Deck-building

- Är startleken tråkig?
- Är marknaden balanserad?
- Går spelet för långt eller kort?
- Finns för starka kombinationer?

### Coop

- Kan en spelare styra alla?
- Är hotnivån lagom?
- Skalar svårigheten med antal spelare?
- Är spelarnas roller meningsfulla?

### Barnspel

- Förstår barnen turen?
- Behöver de läsa för mycket?
- Är komponenterna tydliga?
- Är förlusten för hård?

### Familjespel

- Kan spelet läras ut på några minuter?
- Får både barn och vuxna meningsfulla val?
- Är speltiden rimlig?
- Finns lagom slump?

---

## 29. Frågor GPT:n kan använda vid start av nytt spel

GPT:n bör inte alltid fråga alla frågor, men kan använda dem vid behov.

```text
1. Vem ska spelet vara för?
2. Hur lång speltid vill du ha?
3. Hur många spelare?
4. Ska spelet vara tävling, samarbete eller båda?
5. Vill du ha mest kort, spelbräde, tärningar, markörer eller något annat?
6. Ska det gå att skriva ut hemma på A4?
7. Vill du ha låg komponentmängd?
8. Ska spelet vara mest tur, strategi, taktik, berättelse eller problemlösning?
9. Ska första målet vara snabb prototyp eller snygg print-and-play?
```

Om användaren redan gett tillräckligt med information ska GPT:n inte överfråga.

---

## 30. Rekommenderat svarsmönster vid kategorival

När användaren beskriver en idé bör GPT:n svara ungefär så här:

```markdown
Jag ser tre möjliga riktningar:

## Alternativ A: Kortdrivet äventyr
Passar om du vill ha snabb prototyp och få komponenter.
Komponenter: ...
Risk: ...

## Alternativ B: Nodkarta med händelsekort
Passar om du vill ha mer äventyrskänsla och vägval.
Komponenter: ...
Risk: ...

## Alternativ C: Enkel coop
Passar om spelarna ska samarbeta.
Komponenter: ...
Risk: ...

## Rekommendation

Jag skulle börja med Alternativ B eftersom ...
Första prototypen bör innehålla ...
```

GPT:n bör alltid ge en tydlig rekommendation, inte bara alternativ.

---

## 31. Definition of Done för steg 4

Steg 4 är klart när kunskapspaketet innehåller en spelkategori-guide som beskriver:

- hur GPT:n väljer kategori
- jämförelse mellan vanliga speltyper
- kortspel
- tärningsspel
- bana/race
- nodkarta/äventyr
- dungeon crawl
- worker placement
- deck-building
- tile placement
- area control
- coop
- barnspel
- familjespel
- duellspel
- solo
- memory/spatial
- set collection
- push your luck
- roll-and-write
- hybridspel
- kategorival för prototyp, print-and-play, barnspel, familjespel och hobbyspel
- balansfrågor per kategori
- startfrågor och svarsmönster
