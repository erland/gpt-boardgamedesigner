# Brädspelsdesigner – Samlade testprompter


---


# Testprompter för steg 1

Dessa testprompter används för att se om GPT:ns grundroll och arbetssätt fungerar innan mer kunskap läggs till.

## Test 1: Nytt barnspel

```text
Jag vill skapa ett enkelt brädspel för barn 7–10 år med äventyrstema. Det ska gå att skriva ut hemma. Hjälp mig ta fram första spelbara versionen.
```

Förväntat beteende:

- föreslår målgruppsanpassad riktning
- skapar enkel kärnloop
- föreslår komponenter
- nämner print-and-play
- överkomplicerar inte

## Test 2: Otydlig idé

```text
Jag vill göra ett spel om att utforska en magisk skog, men jag vet inte om det ska vara kortspel eller spelbräde.
```

Förväntat beteende:

- jämför 2–3 riktningar
- rekommenderar en väg
- förklarar varför
- föreslår första prototyp

## Test 3: Befintlig zip

```text
Analysera den här projekt-zippen och föreslå vad vi bör göra härnäst.
```

Förväntat beteende:

- inventerar struktur
- letar efter README, PROJECT_STATUS och CHANGELOG
- skiljer källa från output
- föreslår praktiska nästa steg

## Test 4: Regelbok

```text
Skapa en regelbok utifrån den här spelidén och strukturera den som en riktig brädspelsregelbok.
```

Förväntat beteende:

- använder tydlig regelboksstruktur
- inkluderar mål, komponenter, setup, turordning och vinstvillkor
- skriver praktiskt och spelbart

## Test 5: A6-förklaringskort

```text
Skapa ett A6-förklaringskort för spelet så att det känns som ett snyggt referenskort, inte som en manual.
```

Förväntat beteende:

- prioriterar kort och tydlig text
- föreslår symboler och turöversikt
- undviker långa regeltexter

## Test 6: Projektstädning

```text
Zippen börjar bli stor. Identifiera historiska filer och output som kan rensas bort utan att källmaterial försvinner.
```

Förväntat beteende:

- är försiktig
- identifierar output och historiska filer
- föreslår rensning utan att radera källor
- dokumenterar ändringen om den utförs


---


# Testprompter för steg 11A

## Test 1: Mekanikanalys

```text
Analysera kärnloopen i det här spelet och säg om spelarna har meningsfulla val eller om det blir för mycket slump.
```

Godkänt om GPT:n tar upp kärnloop, action economy, risk/belöning, slump/kontroll och nästa test.

## Test 2: Komponentfriktion

```text
Första prototypen har 90 kort, runda tokens, specialtärningar och ett bräde på 4 A4. Är det rimligt?
```

Godkänt om GPT:n bromsar scope och föreslår MVP.

## Test 3: Blindtest

```text
Vi vill blindtesta spelet. Skapa blindtestpaket, instruktion och feedbackformulär.
```

Godkänt om GPT:n skapar struktur för testare och fokuserar på regelklarhet.

## Test 4: Konstruktiv kritik

```text
Var kritisk: vad är största risken med den här designen?
```

Godkänt om GPT:n inte bara är positiv utan identifierar konkreta risker och förenklingar.

## Test 5: Inspiration från befintligt spel

```text
Jag vill göra något som påminner om ett känt spel men för barn och print-and-play. Hur analyserar vi inspirationen utan att kopiera?
```

Godkänt om GPT:n abstraherar kärnloop och komponentmodell, varnar för kopiering och anpassar till nytt tema/målgrupp.

## Test 6: Finbalans för tidigt

```text
Vi har inte speltestat än men vill finjustera alla kortvärden.
```

Godkänt om GPT:n avråder från finbalans och föreslår testbara hypoteser.


---


# Testprompter för steg 11B – Nybörjarguide

## Test 1: Total nybörjare

```text
Jag har aldrig gjort ett brädspel tidigare men vill testa. Var börjar jag?
```

Godkänt om GPT:n:

- lugnar användaren
- föreslår liten första prototyp
- frågar högst 2–3 enkla frågor eller gör rimliga antaganden
- undviker teoriöverlast
- föreslår snabbt första test

## Test 2: För stor idé

```text
Jag vill göra mitt första spel: ett kampanjspel med 200 kort, 20 figurer, flera kartor och fyra spellägen.
```

Godkänt om GPT:n:

- bromsar utan att döda idén
- föreslår MVP
- väljer en liten första testversion
- säger vad som kan vänta

## Test 3: 1-sidesregler

```text
Hjälp mig skriva första 1-sidesregeln för ett enkelt äventyrsspel för barn.
```

Godkänt om GPT:n:

- använder kort regelstruktur
- har mål, komponenter, setup, din tur och vinst
- håller texten enkel

## Test 4: Efter första testet

```text
Vi testade första versionen. Barnen förstod målet men turen tog för lång tid och de ville ändå spela igen.
```

Godkänt om GPT:n:

- lyfter det som fungerade
- prioriterar turlängd
- föreslår 1–3 ändringar
- säger vad som ska vänta

## Test 5: Grafik för tidigt

```text
Innan vi testar vill jag göra alla kort illustrerade och skapa en snygg box.
```

Godkänt om GPT:n:

- förklarar varför det är bättre att vänta
- föreslår enkel prototypgrafik
- bevarar entusiasmen


---


# Testprompter för steg 2 – Projektstandard

Dessa testprompter kontrollerar att GPT:n kan använda projektstandarden.

## Test 1: Skapa ny projektstruktur

```text
Jag vill skapa ett nytt print-and-play-spel med kort och ett litet spelbräde. Skapa en lämplig projektstruktur och förklara vilka filer som ska vara källor.
```

Förväntat:

- föreslår README, PROJECT_STATUS och CHANGELOG
- skapar docs/data/output-struktur
- skiljer källa från output
- föreslår `data/cards.yaml` och `data/board.yaml`

## Test 2: Minimal struktur

```text
Jag vill börja väldigt enkelt med ett litet kortspel. Vilken minsta projektstruktur räcker?
```

Förväntat:

- föreslår enkel struktur
- inkluderar docs och data
- undviker onödig komplexitet

## Test 3: Zip-analys

```text
Analysera den här zippen och identifiera vad som verkar vara källfiler respektive genererad output.
```

Förväntat:

- prioriterar README, PROJECT_STATUS, CHANGELOG
- identifierar docs/data/templates/scripts/output
- varnar om PDF verkar vara output

## Test 4: Rensning

```text
Zippen har blivit stor. Föreslå vad som kan rensas utan att förlora källmaterial.
```

Förväntat:

- föreslår att gamla output-, preview- och cachefiler kan rensas
- är försiktig med docs, data, templates, scripts och assets/source
- föreslår dokumenterad rensning

## Test 5: Projektstatus

```text
Skapa ett PROJECT_STATUS.md för ett första spelbart prototypprojekt.
```

Förväntat:

- använder standardformat
- inkluderar version, status, klart, saknas, kända problem och nästa steg

## Test 6: Changelog

```text
Vi har lagt till kortdata och en första regelbok. Skapa en changelog-post för detta.
```

Förväntat:

- använder Tillagt/Ändrat/Fixat/Rensat/Kommentar
- skriver kort och tydligt


---


# Testprompter för steg 3 – Komponentstandard

Dessa testprompter kontrollerar att GPT:n kan använda komponentstandarden.

## Test 1: Komponentlista för nytt spel

```text
Jag vill skapa ett äventyrsspel för 2–4 barn där man rör sig på en karta, hittar saker och undviker faror. Vilka komponenter bör första spelbara prototypen ha?
```

Förväntat:

- föreslår minsta spelbara komponentuppsättning
- skiljer på prototyp och senare snygg version
- nämner spelbräde, kort, markörer, regelbok och referenskort
- undviker för stor komponentmängd

## Test 2: Kortdata

```text
Skapa en första cards.yaml-struktur för ett familjespel med händelsekort, föremålskort och uppdragskort.
```

Förväntat:

- använder stabila id:n
- inkluderar type, deck, count, effect och tags
- håller korttexten kort
- tänker på balans och antal kort

## Test 3: Spelbräde

```text
Jag vill ha ett spelbräde där spelare utforskar en skog. Ska det vara bana, rutnät, zoner eller nodkarta?
```

Förväntat:

- jämför flera brädetyper
- rekommenderar en väg
- förklarar print-and-play-konsekvenser
- föreslår `data/board.yaml`

## Test 4: Markörer

```text
Spelet behöver energi, skada och belöningar. Hur bör jag designa markörerna för enkel utskrift och laminering?
```

Förväntat:

- föreslår token-data
- tar upp storlek, form och klippbarhet
- nämner att fyrkantiga markörer ofta är enklare än runda
- undviker för mycket text på markörer

## Test 5: A6-förklaringskort

```text
Skapa innehållsstruktur för ett A6-förklaringskort till ett spel med turordning, symboler och terräng.
```

Förväntat:

- skapar kort, visuellt innehåll
- inkluderar turordning, symboler och kom ihåg-ruta
- gör det inte till en mini-regelbok

## Test 6: Komponentgranskning

```text
Granska komponenterna i det här projektet och kontrollera om regler, datafiler och print-output verkar matcha.
```

Förväntat:

- kontrollerar fullständighet
- kontrollerar konsekventa namn
- letar efter komponenter som nämns i regler men saknas i data/output
- skiljer källfiler från output

## Test 7: Produktionsnivå

```text
Vi har en rå prototyp men vill göra den snyggare utan att låsa reglerna för tidigt. Vilken produktionsnivå bör vi sikta på?
```

Förväntat:

- förklarar nivå 1–3
- rekommenderar spelbar print-and-play snarare än produktionsnära version
- föreslår små förbättringar


---


# Testprompter för steg 4 – Spelkategori-guide

Dessa testprompter kontrollerar att GPT:n kan använda spelkategori-guiden.

## Test 1: Välja kategori från lös idé

```text
Jag vill göra ett spel där man utforskar en magisk skog, hittar föremål och möter faror. Det ska passa barn 7–10 år och gå att skriva ut hemma. Vilken typ av spel bör det vara?
```

Förväntat:

- föreslår 2–3 möjliga kategorier
- rekommenderar en huvudkategori
- motiverar med målgrupp och print-and-play
- föreslår första prototyp

## Test 2: Kortspel eller spelbräde

```text
Min idé kan antingen bli ett kortspel eller ett spel med karta. Hur avgör vi vad som är bäst?
```

Förväntat:

- jämför kortspel och karta/nodkarta
- beskriver komponenter, risker och prototypinsats
- rekommenderar väg utifrån önskad upplevelse

## Test 3: Barnspel

```text
Jag vill göra ett spel för barn 6–8 år med lite spänning men utan att det blir för svårt. Vilka kategorier passar bäst?
```

Förväntat:

- rekommenderar barnanpassade kategorier
- varnar för text och komplexitet
- föreslår korta turer, tydliga symboler och få komponenter

## Test 4: Familjespel

```text
Jag vill göra ett familjespel på 30 minuter där både barn och vuxna har riktiga val. Vilken speltyp rekommenderar du?
```

Förväntat:

- föreslår set collection, push your luck, tile placement, enkel nodkarta eller liknande
- förklarar varför
- föreslår komponentnivå

## Test 5: Coop

```text
Jag vill göra ett samarbetsspel där spelarna tillsammans försöker stoppa ett hot. Vad bör jag tänka på?
```

Förväntat:

- tar upp hotspår, eventfas och roller
- varnar för alfa-spelare
- föreslår enkel första prototyp

## Test 6: Dungeon crawl

```text
Jag vill skapa ett dungeon crawl som print-and-play, men jag vill inte att det ska bli för stort. Hur bör jag avgränsa första versionen?
```

Förväntat:

- föreslår mycket smal prototyp
- begränsar antal rum, fiender, hjältar och kort
- varnar för komponentmängd och administration

## Test 7: Kategori och balans

```text
Vilka balansfrågor bör jag ställa för ett kortdrivet äventyrsspel med nodkarta?
```

Förväntat:

- kombinerar balansfrågor för kortspel och nodkarta/äventyr
- tar upp vägval, händelser, kortstyrka och mål


---


# Testprompter för steg 5 – Print-and-play-guide

Dessa testprompter kontrollerar att GPT:n kan använda print-and-play-guiden.

## Test 1: Kort på A4

```text
Jag har 36 spelkort med ganska kort text. Hur bör jag lägga upp dem på A4 för print-and-play?
```

Förväntat:

- jämför 3×3 och 4×4
- tar hänsyn till läsbarhet
- nämner skärlinjer och säkerhetszon
- ger praktisk rekommendation

## Test 2: Laminering av kort

```text
Jag har A4-lamineringsfickor. Ska jag laminera hela kortarket och klippa efteråt eller klippa först och laminera sedan?
```

Förväntat:

- förklarar skillnaden mellan metoderna
- säger att helarks-laminering inte ger plastkant runt varje kort
- rekommenderar metod beroende på prototyp eller hållbar version

## Test 3: Markörer

```text
Spelet har energi-, skada- och belöningsmarkörer. Hur bör jag göra dem enkla att skriva ut, klippa och laminera?
```

Förväntat:

- föreslår storlek runt 20–25 mm
- rekommenderar fyrkantiga markörer för enkelhet
- nämner runda markörer/cirkelstans som senare alternativ
- föreslår tokenark

## Test 4: A6-referenskort

```text
Jag vill skapa ett A6-förklaringskort och skriva ut flera på A4. Hur bör det produceras?
```

Förväntat:

- beskriver A6-format
- föreslår källa och output
- nämner 4×A6 på A4
- fokuserar på kort, visuellt innehåll

## Test 5: Dubbelsidig utskrift

```text
Jag vill ha kortbaksidor, men min skrivare passar inte dubbelsidigt exakt. Vad är bästa lösningen?
```

Förväntat:

- varnar för passningsproblem
- föreslår sleeves eller enkelsidigt
- föreslår baksidor utan exakt kantpassning om dubbelsidigt ändå används

## Test 6: Produktionsguide

```text
Skapa en docs/production-guide.md för ett spel med kort, markörer, spelbräde, regelbok och A6-referenskort.
```

Förväntat:

- listar printfiler
- rekommenderar papper
- beskriver laminering/skärning
- skiljer printklara filer från preview

## Test 7: Ink-friendly

```text
Spelet har mycket färg och zippen innehåller många stora PDF:er. Hur kan vi göra en mer utskriftsvänlig version?
```

Förväntat:

- föreslår ink-friendly-output
- minskar stora färgfält
- använder ljusa bakgrunder och ikoner
- nämner separat output/print/ink-friendly


---


# Testprompter för steg 6 – Regelboksstandard

Dessa testprompter kontrollerar att GPT:n kan använda regelboksstandarden.

## Test 1: Komplett regelbok

```text
Skapa en regelbok för ett enkelt äventyrsspel där spelare rör sig på en nodkarta, drar händelsekort, samlar tre stjärnor och återvänder till start.
```

Förväntat:

- innehåller mål, komponenter, setup, turordning, handlingar och vinstvillkor
- har exempelrunda
- är spelbar och inte bara beskrivande
- passar målgruppen om den anges

## Test 2: Kort barnregelbok

```text
Skriv reglerna för ett barnspel 7–10 år i en kortare och mer lättläst struktur.
```

Förväntat:

- använder förenklad regelboksstruktur
- korta avsnitt
- tydlig turordning
- lite text och enkla ord

## Test 3: Snabbstart

```text
Skapa en snabbstart för ett spel med spelbräde, äventyrskort, energimarkörer och målet att samla 3 stjärnor.
```

Förväntat:

- 1–2 sidor i struktur
- mål, lägg fram, förbered, din tur, handlingar och vinst
- inga långa specialregler

## Test 4: FAQ

```text
Skapa en FAQ för ett spel där spelare har kort på hand, energimarkörer, rörelse på karta och händelsekort.
```

Förväntat:

- svarar på vanliga regelfrågor
- flyttar inte grundregler till FAQ
- formulerar korta, precisa svar

## Test 5: Granska regelbok

```text
Granska den här regelboken och hitta otydliga regler, saknade begrepp, motsägelser och sådant som kan bli svårt vid första spelomgången.
```

Förväntat:

- granskar struktur, spelbarhet, konsekvens, målgrupp och print
- identifierar saknade regler
- föreslår konkreta förbättringar

## Test 6: Flera varianter

```text
Spelet har grundläge, äventyrsläge och coop-läge. Bör vi ha en gemensam regelbok eller separata regelböcker?
```

Förväntat:

- förklarar när gemensam regelbok räcker
- rekommenderar separata regelböcker om turordning, komponenter eller vinstvillkor skiljer sig mycket
- föreslår struktur för `docs/rulebooks/`

## Test 7: Koppling till datafiler

```text
Regelboken nämner 36 kort och 24 energimarkörer. Hur säkerställer vi att det matchar datafiler och print-output?
```

Förväntat:

- jämför `docs/rulebook.md`, `data/cards.yaml`, `data/tokens.yaml`, `data/game.yaml` och `output/print/`
- föreslår konsekvenskontroll
- varnar för att PDF-output inte ska vara enda källa


---


# Testprompter för steg 7 – Playtest- och balansguide

Dessa testprompter kontrollerar att GPT:n kan använda playtest- och balansguiden.

## Test 1: Första playtest-plan

```text
Vi har en första spelbar prototyp av ett barnäventyrsspel med karta, kort och markörer. Skapa en playtest-plan för första testet.
```

Förväntat:

- föreslår testnivå
- anger syfte och mätvärden
- fokuserar på kärnloop och begriplighet
- föreslår vad som inte ska testas ännu

## Test 2: Playtestlogg

```text
Skapa en docs/playtest-log.md-mall för vårt projekt.
```

Förväntat:

- inkluderar version, testtyp, testmål, resultat, observationer, balansindikationer och beslut
- har fältet “Ändra inte ännu”

## Test 3: Tolka testanteckningar

```text
Testet tog 55 minuter, barnen tappade fokus efter halva tiden, men de tyckte händelsekorten var roliga. Vad bör vi ändra?
```

Förväntat:

- identifierar speltid som huvudproblem
- bevarar händelsekorten som fungerade
- föreslår 1–3 små ändringar
- anger nästa testmål

## Test 4: Balans för kort

```text
Här är tio kort. Kan du analysera om några verkar för starka eller för svaga och föreslå hur vi ska testa dem?
```

Förväntat:

- tittar på kostnad, effekt, timing, antal kopior och kombinationer
- säger att teoretisk balans behöver speltest
- föreslår testbara hypoteser

## Test 5: Coop-svårighet

```text
Vårt coop-spel är för lätt med 4 spelare men lagom med 2. Vad bör vi mäta och justera?
```

Förväntat:

- tar upp skalning
- föreslår justering av hot, mål eller resurser
- föreslår mätvärden för vinstgrad och rundor

## Test 6: Blindtest

```text
Vi vill låta några andra testa spelet utan att vi förklarar. Hur förbereder vi ett blindtest?
```

Förväntat:

- beskriver material, instruktioner och frågor
- fokuserar på regelbok och komponentbegriplighet
- föreslår vad observatören ska notera

## Test 7: För tidigt för balans

```text
Vi har bara spelat en halv omgång och reglerna var oklara. Kan du balansera korten?
```

Förväntat:

- avråder från detaljerad balans ännu
- föreslår regel- och kärnlooptest först
- kan ändå identifiera uppenbara extremkort

## Test 8: Projektuppdatering efter test

```text
Uppdatera projektet efter speltestet: sänk vinstkravet till 2 stjärnor i barnvarianten och dokumentera beslutet.
```

Förväntat:

- uppdaterar relevanta källfiler
- uppdaterar regelbok/variantdata om relevant
- uppdaterar playtestlogg, balansanteckningar, PROJECT_STATUS och CHANGELOG


---


# Testprompter för steg 8 – Exempelprojektmönster

Dessa testprompter kontrollerar att GPT:n kan använda det generella exempelprojektmönstret utan att låsa sig till ett visst tema.

## Test 1: Analysera befintlig projektzip

```text
Analysera den här projektzippen och identifiera vilka filer som verkar vara källor, vilka som är output och vilka nästa steg du rekommenderar.
```

Förväntat:

- letar efter README, PROJECT_STATUS och CHANGELOG
- skiljer docs/data/templates/scripts från output
- identifierar varianter, komponenter och printspår
- föreslår 3–5 konkreta nästa steg

## Test 2: Legendkort som egen komponent

```text
Spelet har många symboler på kort och spelbräde. Hur bör vi skapa ett A6-legendkort så det blir en riktig spelhjälp och inte en manual?
```

Förväntat:

- behandlar legendkort som egen komponent
- föreslår docs/legend-card.md eller data/legend-card.yaml
- föreslår output/print/legend-card-a6.pdf
- håller innehållet kort och visuellt

## Test 3: Flera varianter

```text
Spelet har grundregler, äventyrsläge och en enklare barnvariant. Hur bör projektet strukturera regelböcker och variants.yaml?
```

Förväntat:

- skiljer små och stora varianter
- föreslår separata regelböcker om varianterna skiljer sig mycket
- föreslår data/variants.yaml
- undviker att blanda variantregler otydligt i grundreglerna

## Test 4: Rensa gamla printspår

```text
Zippen innehåller flera gamla printmappar och PDF:er. Hur avgör vi vad som kan rensas?
```

Förväntat:

- skiljer källfiler från output
- föreslår rensning av gamla preview/output om de kan genereras
- är försiktig med docs/data/templates/scripts/assets/source
- föreslår rensningsrapport och changelog

## Test 5: Skapa återgenererbart projektmönster

```text
Jag vill starta ett nytt print-and-play-projekt med kort, markörer, spelbräde, regelbok och legendkort. Skapa en struktur som går att bygga vidare på.
```

Förväntat:

- föreslår docs/data/templates/scripts/output
- skapar källor för komponenter
- föreslår print-layoutdata
- nämner projektstatus och changelog

## Test 6: Validering

```text
Vilka valideringar bör ett större brädspelsprojekt ha för att säkerställa att regler, kort, markörer, bräde och legend hänger ihop?
```

Förväntat:

- föreslår kontroll av id:n, komponentantal, symboler, platstyper och output
- nämner schema/checklista/script
- prioriterar datakällor före PDF-output

## Test 7: Inte kopiera temat

```text
Använd lärdomarna från exempelprojektet men skapa en struktur för ett helt annat speltema.
```

Förväntat:

- återanvänder arbetsmetod
- kopierar inte tema, varumärke eller specifika filspår
- anpassar struktur efter det nya spelets kategori
