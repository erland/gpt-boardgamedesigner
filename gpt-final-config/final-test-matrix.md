# Slutlig testmatris för Brädspelsdesigner

Använd dessa tester efter att GPT:n har skapats i GPT Builder.

## Test 1: Nytt barnspel

Prompt:

```text
Jag vill skapa ett enkelt brädspel för barn 7–10 år med äventyrstema. Det ska gå att skriva ut hemma. Hjälp mig ta fram första spelbara versionen.
```

Godkänt om GPT:n:

- föreslår målgruppsanpassad spelkategori
- skapar kärnloop
- föreslår liten komponentuppsättning
- tänker på A4/print-and-play
- föreslår första speltest

## Test 2: Kategorival

Prompt:

```text
Min idé kan antingen bli ett kortspel eller ett spel med karta. Hur avgör vi vad som är bäst?
```

Godkänt om GPT:n:

- jämför alternativen
- beskriver komponenter/risker
- ger tydlig rekommendation
- kopplar valet till målgrupp och prototypinsats

## Test 3: Projektzip

Prompt:

```text
Analysera den här projekt-zippen och föreslå nästa steg.
```

Godkänt om GPT:n:

- inventerar struktur
- hittar README/PROJECT_STATUS/CHANGELOG
- skiljer källa från output
- identifierar komponenter/varianter/printstatus
- föreslår 3–5 konkreta nästa steg

## Test 4: Regelbok

Prompt:

```text
Skapa en regelbok utifrån den här spelidén och strukturera den som en riktig brädspelsregelbok.
```

Godkänt om GPT:n:

- har mål, komponenter, setup, turordning, handlingar och vinst
- skriver spelbart, inte bara beskrivande
- inkluderar exempel eller FAQ vid behov

## Test 5: A6-legend

Prompt:

```text
Skapa ett A6-förklaringskort för spelet så att det känns som ett snyggt referenskort, inte som en manual.
```

Godkänt om GPT:n:

- håller texten kort
- fokuserar på turordning, symboler och påminnelser
- föreslår källa och output
- undviker fullständig regelbok på A6

## Test 6: Print-and-play

Prompt:

```text
Jag har 36 kort, 24 markörer och ett A4-spelbräde. Hur bör jag lägga upp print-and-play-produktionen?
```

Godkänt om GPT:n:

- föreslår kortark, tokenark och bräde
- nämner skärlinjer, säkerhetszon och laminering
- föreslår testutskrift
- tänker på tonerförbrukning och hemmaproduktion

## Test 7: Playtest

Prompt:

```text
Vi har en första spelbar prototyp. Skapa en playtest-plan och säg vad vi ska mäta.
```

Godkänt om GPT:n:

- väljer rimlig testnivå
- definierar testmål
- föreslår mätvärden
- avgränsar vad som inte ska testas ännu

## Test 8: Speltestanteckningar

Prompt:

```text
Testet tog 55 minuter, barnen tappade fokus efter halva tiden, men händelsekorten var roliga. Vad bör vi ändra?
```

Godkänt om GPT:n:

- identifierar speltid/fokus som huvudproblem
- behåller det som fungerade
- föreslår få ändringar
- formulerar nästa testmål

## Test 9: Rensning

Prompt:

```text
Zippen börjar bli stor. Identifiera historiska filer och output som kan rensas bort utan att källmaterial försvinner.
```

Godkänt om GPT:n:

- är försiktig med docs/data/templates/scripts/assets/source
- föreslår rensning av gamla output/preview/cache
- föreslår changelog/rensningsrapport

## Test 10: Flera varianter

Prompt:

```text
Spelet har grundläge, äventyrsläge och coop-läge. Bör vi ha en gemensam regelbok eller separata regelböcker?
```

Godkänt om GPT:n:

- förklarar när separata regelböcker behövs
- föreslår variants.yaml
- kopplar regler, komponenter och vinstvillkor
