# Regelboksstandard för Brädspelsdesigner

Detta dokument beskriver hur GPT:n **Brädspelsdesigner** bör skapa, analysera och förbättra regelböcker för brädspelsprojekt.

Syftet är att GPT:n ska kunna skriva regler som känns som riktiga brädspelsregler: tydliga, spelbara, konsekventa och lätta att använda vid bordet.

Regelboken ska inte bara beskriva idén. Den ska göra att någon faktiskt kan spela spelet.

---

## 1. Grundprinciper

### 1.1 Regelboken är en spelkomponent

Regelboken ska behandlas som en central komponent i spelet.

Den ska:

- lära ut spelet
- minska missförstånd
- ge spelarna rätt ordning på momenten
- förklara komponenterna
- visa exempel
- hantera vanliga frågor
- dokumentera variantregler

Regelboken bör normalt ligga i:

```text
docs/rulebook.md
```

Genererad PDF bör ligga i:

```text
output/rulebooks/rulebook.pdf
```

eller:

```text
output/print/rulebook.pdf
```

### 1.2 Skriv för första spelomgången

Regelboken ska hjälpa spelaren att komma igång.

GPT:n bör prioritera:

1. Vad är spelet?
2. Hur vinner man?
3. Vad finns i spelet?
4. Hur förbereder man?
5. Vad gör man på sin tur?
6. När är spelet slut?
7. Vad händer i vanliga situationer?

Undvik att börja med långa designförklaringar, bakgrundshistoria eller specialfall.

### 1.3 En regel ska vara spelbar

En regel är inte klar förrän den svarar på:

- vem gör något?
- när görs det?
- vad krävs?
- vad händer?
- vad händer om det inte går?
- hur påverkar det spelets mål?

Dåligt:

```text
Spelaren kan ibland använda energi för att göra en starkare handling.
```

Bättre:

```text
En gång per tur får du betala 1 energi för att flytta 1 extra steg.
```

### 1.4 Separera regler från designanteckningar

Regelboken ska inte vara en blandning av regler och interna kommentarer.

Designanteckningar bör ligga i:

```text
docs/design-brief.md
docs/balancing-notes.md
docs/playtest-log.md
```

Regelboken ska bara innehålla sådant spelaren behöver för att spela.

---

## 2. Standardstruktur för regelbok

GPT:n bör normalt använda denna struktur:

```markdown
# Spelets namn

Kort introduktion.

## 1. Spelets mål

## 2. Innehåll

## 3. Förberedelser

## 4. Översikt

## 5. Spelets gång

## 6. Din tur

## 7. Handlingar

## 8. Centrala regler

## 9. Kort, symboler och markörer

## 10. Konflikt/strid/utmaningar

## 11. Spelets slut och vinst

## 12. Exempelrunda

## 13. Vanliga frågor

## 14. Variantregler

## 15. Utskrift och montering
```

Alla spel behöver inte alla avsnitt. GPT:n ska anpassa strukturen till spelet.

För ett mycket enkelt barnspel kan regelboken vara kortare.

---

## 3. Kort regelboksstruktur för enkla spel

För små barnspel, kortspel eller första prototyper kan GPT:n använda:

```markdown
# Spelets namn

## Vad går spelet ut på?

## Det här behöver ni

## Förbered spelet

## Så spelar ni

## Din tur

## Så vinner du

## Symboler

## Första speltestet
```

Denna struktur passar när spelet ska vara snabbt att förstå.

---

## 4. Avsnitt: Introduktion

Introduktionen ska vara kort.

Den bör svara på:

- Vad är temat?
- Vad gör spelarna?
- Vilken känsla ska spelet ge?

Exempel:

```markdown
I Skogsäventyret utforskar ni en magisk skog, samlar stjärnor och försöker hitta vägen tillbaka innan mörkret faller. Spelet passar 2–4 spelare och tar ungefär 20–30 minuter.
```

Undvik lång bakgrundshistoria i början.

---

## 5. Avsnitt: Spelets mål

Detta ska komma tidigt.

Målet ska vara konkret.

Exempel:

```markdown
Målet är att bli den första spelaren som samlar 3 stjärnor och återvänder till startplatsen.
```

För coop:

```markdown
Spelarna vinner tillsammans om de hittar de tre nycklarna innan hotmarkören når slutet av hotspåret.
```

För poängspel:

```markdown
När sista rundan är klar vinner spelaren med flest poäng.
```

### 5.1 Kontrollfrågor

GPT:n bör kontrollera:

- Är vinstvillkoret tydligt?
- Kan flera vinna samtidigt?
- Finns tiebreaker?
- Vet spelarna vad de ska fokusera på från början?

---

## 6. Avsnitt: Innehåll

Komponentlistan ska vara tydlig och matcha projektets faktiska filer.

Exempel:

```markdown
## Innehåll

- 1 spelbräde
- 36 äventyrskort
- 12 uppdragskort
- 4 spelarpjäser
- 24 energimarkörer
- 1 A6-referenskort
- 1 regelbok
```

GPT:n bör kontrollera att listan matchar:

- `data/game.yaml`
- `data/cards.yaml`
- `data/tokens.yaml`
- `data/board.yaml`
- output-filer i `output/print/`

---

## 7. Avsnitt: Förberedelser

Setup ska vara stegvis.

Bra setup:

```markdown
## Förberedelser

1. Lägg spelbrädet mitt på bordet.
2. Blanda äventyrskorten och lägg dem med framsidan nedåt.
3. Lägg energimarkörerna bredvid spelbrädet.
4. Varje spelare väljer en pjäs och ställer den på Start.
5. Ge varje spelare 2 kort.
6. Den yngsta spelaren börjar.
```

### 7.1 Setup-regler

GPT:n bör tänka på:

- numrerad lista
- inga långa stycken
- komponenter nämns med samma namn som i komponentlistan
- börja med bräde/kort/markörer
- avsluta med startspelare

### 7.2 Startspelare

Regelboken bör ange hur startspelare väljs.

Exempel:

- yngsta spelaren börjar
- spelaren som senast var i en skog börjar
- slumpa startspelare
- spelaren med startmarkören börjar

För barnspel är en enkel och rolig regel ofta bra.

---

## 8. Avsnitt: Översikt

En kort översikt hjälper spelaren förstå flödet innan detaljerna.

Exempel:

```markdown
Spelet spelas i turordning. På din tur drar du ett kort, gör upp till två handlingar och löser effekten på rutan där du stannar. Därefter går turen vidare till nästa spelare.
```

Översikten ska inte innehålla alla detaljer.

---

## 9. Avsnitt: Spelets gång

Detta avsnitt beskriver rundor, faser eller turordning.

### 9.1 Enkel turordning

```markdown
Spelet går medsols. Varje spelare gör en hel tur innan nästa spelare börjar.
```

### 9.2 Faser

Om spelet har faser:

```markdown
Varje runda har tre faser:

1. Händelsefas
2. Spelarfas
3. Slutfas
```

### 9.3 Coop

Coop-spel behöver ofta beskriva:

- eventfas
- spelarnas turer
- hotets utveckling
- vinst/förlust

### 9.4 Kontrollfrågor

GPT:n bör kontrollera:

- Finns runda eller bara tur?
- När dras kort?
- När flyttas hot/rundmarkör?
- När kontrolleras vinst/förlust?
- Är turordningen densamma hela spelet?

---

## 10. Avsnitt: Din tur

Detta är ofta regelbokens viktigaste avsnitt.

Det bör vara kort och tydligt.

Exempel:

```markdown
## Din tur

På din tur gör du följande i ordning:

1. Dra 1 äventyrskort.
2. Gör upp till 2 handlingar.
3. Lös rutan där din pjäs står.
4. Kontrollera om du har vunnit.
```

### 10.1 Bra princip

Det som spelaren gör varje tur ska också finnas på A6-referenskortet.

---

## 11. Avsnitt: Handlingar

Handlingar ska beskrivas konsekvent.

Exempel:

```markdown
## Handlingar

Du får göra upp till 2 handlingar på din tur. Du får välja samma handling flera gånger om inget annat står.

### Flytta

Flytta din pjäs 1 steg längs en väg till en angränsande ruta.

### Spela ett kort

Spela ett kort från handen och gör det som står på kortet. Lägg sedan kortet i slänghögen.

### Vila

Ta 1 energimarkör från förrådet.
```

### 11.1 Handlingsformat

Varje handling bör ange:

- kostnad
- vad spelaren gör
- begränsning
- resultat

Mall:

```markdown
### Handlingens namn

Kostnad: ...
Gör så här: ...
Begränsning: ...
Resultat: ...
```

För enkla spel behövs inte etiketter, men informationen ska finnas.

---

## 12. Avsnitt: Centrala regler

Här förklaras begrepp som används flera gånger.

Exempel:

- handgräns
- resurser
- rörelse
- kortlek och slänghög
- statusar
- hinder
- uppdrag
- områden
- terräng
- lagarbete
- skada och läkning

### 12.1 Begrepp ska definieras en gång

Om “energi” används på kort och markörer ska regelboken definiera energi tydligt.

Exempel:

```markdown
## Energi

Energi används för att göra extra handlingar. När du får energi tar du en energimarkör från förrådet. När du betalar energi lägger du tillbaka markören i förrådet.
```

---

## 13. Avsnitt: Kort, symboler och markörer

Regelboken bör förklara komponenter som spelaren tolkar under spelet.

Exempel:

```markdown
## Kort

Det finns tre typer av kort:

- Äventyrskort: Dras när du kommer till en äventyrsruta.
- Föremålskort: Ger dig en fördel och sparas framför dig.
- Uppdragskort: Visar mål du kan slutföra för att få stjärnor.
```

### 13.1 Symboler

Symboler bör listas kort.

Exempel:

```markdown
## Symboler

| Symbol | Betydelse |
|---|---|
| ⚔ | Utmaning |
| ★ | Belöning |
| 🌲 | Skog |
| 💧 | Vatten |
```

Symboler ska matcha A6-legendkortet.

---

## 14. Avsnitt: Konflikt, strid eller utmaningar

Om spelet har strid eller utmaningar måste reglerna vara särskilt tydliga.

### 14.1 Enkel utmaningsstruktur

Exempel:

```markdown
## Utmaningar

När du möter en utmaning slår du 1 tärning.

- 1–2: Misslyckande. Förlora 1 energi.
- 3–4: Delvis lyckat. Inget händer.
- 5–6: Lyckat. Ta 1 belöning.
```

### 14.2 Stridsstruktur

Om spelet har strid bör regelboken ange:

- när strid startar
- vem som attackerar
- hur träff avgörs
- hur skada räknas
- när strid tar slut
- vad belöningen är
- vad som händer vid förlust

### 14.3 Vanlig risk

Stridsregler blir ofta för långa. GPT:n bör föreslå att första versionen har en enkel konfliktmekanik.

---

## 15. Avsnitt: Spelets slut och vinst

Spelets slut ska vara exakt.

Exempel:

```markdown
Spelet slutar direkt när en spelare har samlat 3 stjärnor och står på Start. Den spelaren vinner.
```

För runda-slut:

```markdown
När en spelare når 10 poäng spelas rundan klart så att alla har haft lika många turer. Därefter vinner spelaren med flest poäng.
```

För coop:

```markdown
Spelarna vinner direkt när alla tre nycklar har lämnats på Porten. Spelarna förlorar direkt om hotmarkören når sista rutan på hotspåret.
```

### 15.1 Tiebreaker

Poängspel bör ha tiebreaker.

Exempel:

```markdown
Vid lika poäng vinner den spelare som har flest energimarkörer kvar. Om det fortfarande är lika delar spelarna segern.
```

---

## 16. Exempelrunda

En exempelrunda är mycket värdefull.

Den bör visa:

- en spelares tur
- ett typiskt kort
- en rörelse
- en konflikt eller belöning om relevant
- hur reglerna används

Exempel:

```markdown
## Exempelrunda

Lisa börjar sin tur på Skogsstigen. Hon drar ett äventyrskort och får kortet “Hitta en genväg”. Hon använder sin första handling för att flytta till Gläntan och sin andra handling för att spela kortet. Kortet låter henne flytta ett extra steg, så hon går vidare till Bäcken. Eftersom Bäcken har symbolen 💧 tar hon 1 energimarkör.
```

### 16.1 Vanliga misstag

Exempelrundan ska inte introducera regler som inte förklarats tidigare.

---

## 17. FAQ och förtydliganden

FAQ bör användas för frågor som ofta uppstår.

Exempel:

```markdown
## Vanliga frågor

### Får jag göra samma handling två gånger?

Ja, om handlingen inte säger något annat.

### Vad händer om kortleken tar slut?

Blanda slänghögen och skapa en ny kortlek.
```

FAQ ska inte vara en plats för grundregler som borde stå tidigare.

---

## 18. Variantregler

Variantregler ska tydligt skiljas från grundspelet.

Exempel:

```markdown
## Variant: Kortare spel

Spela till 2 stjärnor i stället för 3.

## Variant: Svårare skog

När du drar ett farokort förlorar du 1 extra energi.
```

Om projektet har flera större varianter bör varje variant ha:

- egen regelbok eller separat avsnitt
- tydlig relation till grundreglerna
- lista över vad som ändras

Data kan ligga i:

```text
data/variants.yaml
```

---

## 19. Utskrift och montering

Regelboken kan ha kort utskriftsinformation, men detaljer bör ligga i:

```text
docs/production-guide.md
```

Regelbokens avsnitt kan vara kort:

```markdown
## Utskrift

Skriv ut spelbrädet, kortarken, markörarket och A6-referenskortet från `output/print/`. Se `docs/production-guide.md` för rekommenderat papper, laminering och montering.
```

---

## 20. Regelbok kontra snabbstart

### 20.1 Regelbok

Regelboken är komplett och används för:

- första inlärning
- regelfrågor
- variantregler
- exempel
- undantag

### 20.2 Snabbstart

Snabbstarten är kort och hjälper spelaren att börja.

Snabbstart bör ligga i:

```text
docs/quickstart.md
```

Den bör innehålla:

- spelets mål
- snabb setup
- turöversikt
- vanligaste handlingarna
- hur man vinner
- vad man kan ignorera första gången

### 20.3 Snabbstartmall

```markdown
# Snabbstart

## 1. Lägg fram

- Spelbrädet
- Kortleken
- Markörerna

## 2. Målet

Samla 3 stjärnor och återvänd till Start.

## 3. Din tur

1. Dra 1 kort.
2. Gör 2 handlingar.
3. Lös rutan.

## 4. Handlingar

- Flytta 1 steg.
- Spela 1 kort.
- Vila och få 1 energi.

## 5. Vinn

Du vinner direkt när du har 3 stjärnor och står på Start.
```

---

## 21. Regelbok kontra A6-referenskort

A6-referenskortet är inte en miniregelbok.

Det ska innehålla:

- turordning
- handlingar
- symboler
- korta påminnelser
- vinstvillkor i en rad

Det ska inte innehålla:

- full setup
- exempelrundor
- långa undantag
- bakgrundshistoria
- alla korttyper med långa förklaringar

Källa:

```text
docs/legend-card.md
```

Output:

```text
output/print/legend-card-a6.pdf
```

---

## 22. Språk och stil

### 22.1 Skriv direkt till spelaren

Använd “du” eller “ni” konsekvent.

Exempel:

```markdown
På din tur får du göra upp till 2 handlingar.
```

För coop:

```markdown
Ni vinner tillsammans om ni hittar alla tre nycklar.
```

### 22.2 Undvik otydliga ord

Var försiktig med:

- ibland
- vanligtvis
- kan
- ungefär
- bör
- eventuellt
- om det passar

Regler behöver precision.

### 22.3 Använd samma begrepp överallt

Om komponenten heter “energimarkör” ska den inte senare kallas “energi-token”, “kraft” eller “resurs” utan förklaring.

GPT:n bör kontrollera konsekvens mellan:

- regelbok
- kortdata
- markördata
- legendkort
- komponentlista

---

## 23. Rubriknivåer

Regelboken bör ha rimlig rubrikstruktur.

Rekommendation:

- H1: spelets namn
- H2: huvudavsnitt
- H3: underregler eller handlingar
- H4: bara vid behov

Undvik för djup struktur i enkla spel.

Bra:

```markdown
# Skogsäventyret

## Din tur

### Flytta

### Spela kort
```

Mindre bra:

```markdown
# Skogsäventyret

## Regler

### Tur

#### Handlingar

##### Flytta
```

---

## 24. Tabeller

Tabeller är bra för:

- komponentlista
- symboler
- tärningsresultat
- korttyper
- sammanfattningar

Exempel:

```markdown
| Tärning | Resultat |
|---:|---|
| 1–2 | Förlora 1 energi |
| 3–4 | Inget händer |
| 5–6 | Ta 1 belöning |
```

Undvik mycket breda tabeller i PDF, särskilt om regelboken ska fungera på A4 eller A5.

---

## 25. Exempel och illustrationer

GPT:n bör föreslå exempel när regler riskerar att missförstås.

Bra exempel:

- korta
- använder riktiga komponentnamn
- visar en vanlig situation
- kommer efter regeln
- introducerar inte nya regler

Illustrationer kan vara:

- små diagram
- kortexempel
- setup-bild
- turöversikt
- spelplansutsnitt

Men i tidig prototyp räcker text ofta.

---

## 26. Regelboksgranskning

När GPT:n granskar en regelbok bör den kontrollera:

### 26.1 Struktur

- Finns mål?
- Finns komponentlista?
- Finns setup?
- Finns turordning?
- Finns handlingar?
- Finns vinstvillkor?
- Finns exempel?
- Finns FAQ eller förtydliganden vid behov?

### 26.2 Spelbarhet

- Kan man spela spelet med reglerna?
- Saknas någon regel för ett återkommande moment?
- Finns odefinierade begrepp?
- Finns motsägelser?
- Är slutvillkor tydligt?

### 26.3 Konsekvens

- Matchar komponentnamn datafilerna?
- Matchar symboler legendkortet?
- Matchar antal komponenter output?
- Används samma ord överallt?

### 26.4 Målgrupp

- Är texten för svår?
- Är turen för lång?
- Krävs för mycket läsning?
- Är exempel tillräckliga?

### 26.5 Print

- Är regelboken rimligt lång?
- Fungerar den som PDF?
- Behövs snabbstart?
- Behövs A6-referenskort?

---

## 27. Vanliga regelboksproblem

GPT:n bör hjälpa användaren undvika:

- vinstvillkor förklaras för sent
- setup saknar komponenter
- handlingar blandas med tips
- korteffekter kräver begrepp som inte definierats
- konflikter/strid är otydliga
- undantag kommer före grundregel
- samma komponent har flera namn
- regelbok blir designlogg
- FAQ innehåller viktiga grundregler
- variantregler blandas in i grundspelet
- exempel motsäger reglerna

---

## 28. Mall: komplett regelbok

```markdown
# SPELETS NAMN

Kort introduktion till temat och vad spelarna gör.

## 1. Spelets mål

Beskriv exakt hur man vinner.

## 2. Innehåll

- 1 spelbräde
- X kort
- X markörer
- X pjäser
- 1 regelbok
- 1 referenskort

## 3. Förberedelser

1. ...
2. ...
3. ...

## 4. Översikt

Kort beskrivning av spelets flöde.

## 5. Spelets gång

Beskriv rundor, turordning eller faser.

## 6. Din tur

På din tur gör du följande:

1. ...
2. ...
3. ...

## 7. Handlingar

### Handling 1

...

### Handling 2

...

## 8. Centrala regler

### Begrepp 1

...

### Begrepp 2

...

## 9. Kort, symboler och markörer

...

## 10. Konflikt eller utmaningar

...

## 11. Spelets slut och vinst

...

## 12. Exempelrunda

...

## 13. Vanliga frågor

...

## 14. Variantregler

...

## 15. Utskrift och montering

Se även `docs/production-guide.md`.
```

---

## 29. Mall: snabbstart

```markdown
# Snabbstart

## Målet

...

## Lägg fram

- ...
- ...
- ...

## Förbered

1. ...
2. ...
3. ...

## Din tur

1. ...
2. ...
3. ...

## Handlingar

- ...
- ...
- ...

## Så vinner du

...

## Första gången

Ignorera dessa regler första gången om ni vill komma igång snabbare:

- ...
```

---

## 30. Mall: FAQ

```markdown
# Vanliga frågor

## Får jag göra samma handling flera gånger?

...

## Vad händer om kortleken tar slut?

...

## Kan flera spelare stå på samma ruta?

...

## När kontrollerar man om någon har vunnit?

...
```

---

## 31. Regelbok för flera varianter

Om spelet har flera varianter finns två sätt.

### 31.1 Gemensam regelbok med variantavsnitt

Passar när varianterna är små.

Struktur:

```markdown
# Grundregler

...

## Variant: Snabbt spel

...

## Variant: Svårare spel

...
```

### 31.2 Separata regelböcker

Passar när varianterna ändrar mycket.

Exempel:

```text
docs/rulebooks/
  basic-rules.md
  adventure-mode-rules.md
  coop-mode-rules.md
```

GPT:n bör rekommendera separata regelböcker när:

- turordningen skiljer sig
- komponenterna skiljer sig
- vinstvillkoret skiljer sig
- målgruppen skiljer sig
- spelupplevelsen skiljer sig mycket

Gemensamma regler kan då återanvändas via en gemensam grundtext eller mall, men varje regelbok ska vara spelbar fristående.

---

## 32. Koppling till datafiler

Regelboken ska inte nödvändigtvis duplicera all data.

Exempel:

- Regelboken beskriver vad korttyper gör.
- `data/cards.yaml` listar varje kort.
- Regelboken beskriver vad markörer betyder.
- `data/tokens.yaml` listar antal och printstorlek.
- Regelboken beskriver hur brädet används.
- `data/board.yaml` beskriver noder/rutor/zoner.

GPT:n bör undvika att manuellt duplicera långa kortlistor i regelboken om de redan finns i data, om inte användaren vill ha en kortöversikt.

---

## 33. Arbetsflöde när GPT:n skapar regelbok

När användaren ber om regelbok bör GPT:n:

1. identifiera spelets målgrupp och kategori
2. läsa befintlig designbrief/projektstatus om den finns
3. läsa komponentlista/datafiler om de finns
4. formulera spelets mål
5. skapa komponentlista
6. skriva setup
7. skriva turordning
8. skriva handlingar
9. skriva centrala regler
10. skriva slut/vinst
11. lägga till exempelrunda
12. lägga till FAQ vid behov
13. lägga till variantavsnitt om relevant
14. uppdatera `docs/rulebook.md`
15. uppdatera `docs/quickstart.md` om användaren ber om det
16. uppdatera `PROJECT_STATUS.md` och `CHANGELOG.md` vid projektändring

---

## 34. Arbetsflöde när GPT:n förbättrar regelbok

När användaren ber om regelboksgranskning bör GPT:n:

1. läsa hela regelboken
2. jämföra med komponentdata
3. hitta odefinierade begrepp
4. hitta motsägelser
5. kontrollera att vinst och setup är tydliga
6. kontrollera målgruppsanpassning
7. föreslå ändringar
8. om användaren ber om det, skriva om regelboken
9. uppdatera changelog

---

## 35. Definition of Done för steg 6

Steg 6 är klart när kunskapspaketet innehåller en regelboksstandard som beskriver:

- regelbokens syfte
- standardstruktur
- förenklad struktur för små spel
- introduktion
- mål
- komponentlista
- setup
- översikt
- spelets gång
- turstruktur
- handlingar
- centrala regler
- kort/symboler/markörer
- konflikt/strid/utmaningar
- slut och vinst
- exempelrunda
- FAQ
- variantregler
- utskrift/montering
- snabbstart
- A6-referenskortets relation till regelboken
- språk och stil
- rubriknivåer
- tabeller
- regelboksgranskning
- vanliga problem
- mallar
- hantering av flera varianter
- koppling till datafiler
- arbetsflöde för skapande och förbättring
