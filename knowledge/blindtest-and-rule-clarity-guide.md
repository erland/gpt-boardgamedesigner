# Blindtest- och regelklarhetsguide för Brädspelsdesigner

Detta dokument kompletterar regelboksstandarden och playtestguiden med fokus på om spelet kan förstås utan att designern förklarar.

Blindtestbarhet är ett tecken på att regler, komponenter och referenskort fungerar tillsammans.

---

## 1. Vad är ett blindtest?

Ett blindtest innebär att spelare får spelet, reglerna och komponenterna utan att designern lär ut spelet.

Syftet är att testa:

- om regelboken går att följa
- om setup är tydlig
- om komponenter går att identifiera
- om målet förstås
- om första turen kan spelas
- om frågor kan lösas med regelboken
- om referenskortet hjälper

Blindtest är inte första testet. Gör det först när spelet fungerar internt.

---

## 2. När är spelet redo för blindtest?

Spelet är redo när:

- kärnloopen fungerar
- komponentlistan är stabil
- regelboken har setup, turordning och vinstvillkor
- kort/markörer/bräde har konsekventa namn
- någon annan än designern har spelat med viss hjälp
- uppenbara regelhål är åtgärdade

Inte redo när:

- designern fortfarande måste förklara varje tur
- kort saknar text eller id
- komponenter saknas
- vinstvillkor ändras ofta
- setup inte är dokumenterad

---

## 3. Blindtestpaket

Ett blindtestpaket bör innehålla:

```text
docs/rulebook.md eller rulebook.pdf
docs/quickstart.md
docs/production-guide.md
output/print/
docs/blindtest-feedback-form.md
PROJECT_STATUS.md med version
```

Om testaren ska skriva ut själv behövs produktionsguide.

Om komponenterna redan är fysiska behövs ändå en komponentlista.

---

## 4. Instruktion till blindtestare

Mall:

```markdown
# Blindtestinstruktion

Tack för att ni testar spelet.

Försök spela utan hjälp från designern. Markera eller anteckna varje ställe där något är oklart.

## Gör så här

1. Läs reglerna så som ni normalt skulle göra.
2. Förbered spelet från setup-avsnittet.
3. Spela en hel omgång om möjligt.
4. Skriv ner frågor direkt när de uppstår.
5. Gissa inte tyst om något är oklart – notera det.

## Särskilt viktigt

- Var fastnade ni?
- Vilka komponenter var svåra att identifiera?
- Vilken regel behövde ni läsa flera gånger?
- Kunde ni avgöra när spelet var slut?
```

---

## 5. Feedbackformulär

```markdown
# Blindtest-feedback

## Version

...

## Testare

Antal spelare:
Ålder/erfarenhet:

## Setup

- Kunde ni förbereda spelet utan hjälp?
- Vilka steg var oklara?
- Saknades någon komponent?

## Första turen

- Förstod ni vad första spelaren skulle göra?
- Behövde ni leta i reglerna?

## Under spelet

- Vilka frågor uppstod?
- Vilka begrepp var otydliga?
- Vilka kort/markörer/symboler var oklara?

## Spelets slut

- Kunde ni avgöra när spelet var slut?
- Var vinstvillkoret tydligt?

## Regelbok

- Vilket avsnitt var mest hjälpsamt?
- Vilket avsnitt behöver förbättras?
- Saknades exempel?

## Referenskort

- Hjälpte referenskortet?
- Vad saknades på det?

## Helhetsintryck

- Vad var roligast?
- Vad var mest förvirrande?
- Skulle ni spela igen?

## Exakta citat/frågor

- ...
```

---

## 6. Regelklarhet: kontrollfrågor

GPT:n bör granska regler med dessa frågor:

### Mål

- Står målet tidigt?
- Är vinstvillkoret exakt?
- Finns tiebreaker om relevant?

### Komponenter

- Matchar komponentlistan faktiska komponenter?
- Har varje komponent ett konsekvent namn?
- Finns symboler förklarade?

### Setup

- Är setup numrerad?
- Vet spelaren var varje komponent ska ligga?
- Framgår startresurser och startspelare?

### Tur

- Finns en tydlig “Din tur”-lista?
- Vet spelaren när turen slutar?
- Vet spelaren hur många handlingar som får göras?

### Handlingar

- Har varje handling kostnad, effekt och begränsning?
- Kan samma handling göras flera gånger?
- Finns standardfall och undantag separerade?

### Kort och effekter

- Använder korten definierade begrepp?
- Finns timing?
- Finns mål för effekten?
- Framgår vad som händer efter att kort spelas?

### Slut

- När kontrolleras vinst?
- Slutar spelet direkt eller spelas rundan klart?
- Vad händer vid lika?

---

## 7. Vanliga blindtestproblem

### 7.1 Setup tar stopp

Orsak:

- otydlig komponentlista
- komponenter saknar namn
- setup nämner sak som inte finns
- startlägen saknas

Åtgärd:

- numrera setup
- lägg till setup-bild eller tabell
- matcha komponentnamn

### 7.2 Första turen är oklar

Orsak:

- turordning saknas
- handlingar beskrivs för sent
- mål inte förstått

Åtgärd:

- lägg “Din tur” tidigt
- skapa snabbstart
- lägg turöversikt på A6-kort

### 7.3 Begrepp används innan de definieras

Åtgärd:

- definiera centrala begrepp före kort/specialregler
- använd konsekventa namn
- skapa ordlista vid behov

### 7.4 FAQ innehåller grundregler

Åtgärd:

- flytta grundregeln till huvudtexten
- låt FAQ bara förtydliga

### 7.5 Exempel motsäger regel

Åtgärd:

- uppdatera exempel efter regeländring
- använd riktiga komponentnamn
- undvik specialfall i första exemplet

---

## 8. Exempelplacering

Exempel ska komma direkt efter regeln de förklarar.

Bra:

```markdown
### Flytta

Flytta din pjäs 1 steg längs en väg till en angränsande ruta.

Exempel: Om du står på Skogsstigen kan du flytta till Gläntan eller Bäcken.
```

Sämre:

- alla exempel sist
- exempel innan regeln
- exempel med specialfall innan grundfall

---

## 9. Språkregler

GPT:n bör föreslå:

- korta meningar
- aktiv form
- konsekvent “du” eller “ni”
- ett begrepp per sak
- undvik “kan ibland”
- undvik “normalt”
- undvik “om lämpligt”
- skriv exakt när effekter sker

Dåligt:

```text
Spelaren kan normalt sett använda ett kort om situationen tillåter det.
```

Bättre:

```text
Du får spela 1 kort från handen under din tur.
```

---

## 10. Blindtestanalys

När användaren ger blindtestanteckningar ska GPT:n:

1. lista var testarna fastnade
2. koppla varje stopp till regelbok/komponent/print
3. prioritera första tre åtgärder
4. skilja regelproblem från balansproblem
5. föreslå ny blindtestversion
6. uppdatera regelbok/quickstart/legend om användaren ber om det

---

## 11. Definition of Done

Denna guide är komplett när GPT:n kan hjälpa till med:

- blindtestpaket
- blindtestinstruktion
- feedbackformulär
- regelklarhetsgranskning
- setup-test
- första-tur-test
- begreppskontroll
- exempelplacering
- språkputs
- analys av blindtestanteckningar
