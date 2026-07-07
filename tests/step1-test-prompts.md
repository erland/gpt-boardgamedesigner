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
