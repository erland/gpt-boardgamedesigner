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
