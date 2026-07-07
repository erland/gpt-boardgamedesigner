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
