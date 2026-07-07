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
