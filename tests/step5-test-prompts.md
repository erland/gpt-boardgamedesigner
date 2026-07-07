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
