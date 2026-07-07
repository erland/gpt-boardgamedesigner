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
