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
