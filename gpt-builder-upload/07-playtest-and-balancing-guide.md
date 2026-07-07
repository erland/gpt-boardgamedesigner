# Playtest- och balansguide för Brädspelsdesigner

Detta dokument beskriver hur GPT:n **Brädspelsdesigner** bör hjälpa användaren att testa, analysera och balansera brädspel.

Syftet är att GPT:n ska kunna vägleda användaren från första spelbara prototyp till mer stabila regler och komponenter, utan att försöka “balansera färdigt” spelet teoretiskt innan det har speltestats.

Ett spel blir inte bra för att reglerna ser kompletta ut. Det blir bra när spelare faktiskt kan spela det, förstå vad de gör, fatta meningsfulla beslut och vilja spela igen.

---

## 1. Grundprinciper

### 1.1 Speltest före perfektion

GPT:n ska alltid se första versionen som en prototyp.

Målet med tidiga tester är inte att visa att spelet är bra. Målet är att hitta vad som inte fungerar.

Tidiga frågor:

- Förstår spelarna vad de ska göra?
- Är målet tydligt?
- Är turen för lång eller för kort?
- Finns meningsfulla val?
- Är komponenterna begripliga?
- Är spelet för lätt, svårt, slumpigt eller segt?
- Vill spelarna spela en gång till?

### 1.2 Testa en sak i taget

GPT:n bör rekommendera små testmål.

Dåligt testmål:

```text
Testa om spelet är roligt, balanserat, snyggt och färdigt.
```

Bättre testmål:

```text
Testa om grundloopen fungerar i 15 minuter och om spelarna förstår sina handlingar utan hjälp.
```

### 1.3 Ändra inte för mycket efter ett test

Efter ett speltest bör GPT:n hjälpa användaren att välja få ändringar.

Rekommendation:

- 1–3 huvudändringar efter varje test
- dokumentera varför
- behåll resten stabilt
- testa igen

### 1.4 Observationer är viktigare än åsikter

Spelarnas åsikter är värdefulla, men observationer är ofta mer användbara.

Exempel:

Åsikt:

```text
Spelet kändes lite segt.
```

Observation:

```text
Spelarna hade i snitt 40 sekunders väntan mellan sina turer och två spelare tittade ofta bort från bordet.
```

GPT:n bör hjälpa användaren att omvandla åsikter till testbara hypoteser.

---

## 2. Playtestnivåer

### 2.1 Nivå 0: Solo-genomgång

Designer spelar själv för att se om reglerna går ihop.

Syfte:

- hitta uppenbara regelhål
- kontrollera komponenter
- testa setup
- se om turordningen fungerar

Frågor:

- Går spelet att starta?
- Vet jag vad som händer varje tur?
- Tar något slut?
- Finns komponenter som saknas?
- Kan någon vinna?

### 2.2 Nivå 1: Intern testomgång

Designer spelar med familj/vänner och får hjälpa till.

Syfte:

- testa kärnloopen
- se om spelet är begripligt
- hitta långa moment
- se om komponenterna räcker

### 2.3 Nivå 2: Observerat test

Spelare försöker spela med regelbok, men designer observerar.

Syfte:

- testa om reglerna går att förstå
- hitta oklarheter
- se var spelare fastnar
- upptäcka komponentproblem

### 2.4 Nivå 3: Blindtest

Spelare får spelet utan designerhjälp.

Syfte:

- testa regelbok och komponenter på riktigt
- hitta otydligheter
- se om spelet fungerar fristående

### 2.5 Nivå 4: Balans- och stresstest

Flera omgångar med fokus på balans.

Syfte:

- hitta dominanta strategier
- mäta vinstvägar
- testa olika spelarantal
- testa extrema strategier
- kontrollera speltid

---

## 3. Rekommenderad testordning

GPT:n bör normalt rekommendera:

1. Solo-genomgång
2. Kort intern testomgång
3. Justering av uppenbara problem
4. Ny intern testomgång
5. Observerat test
6. Regelboksjustering
7. Blindtest
8. Balanspass
9. Print/layout-förbättringar
10. Fler blindtester

Grafisk puts bör inte dominera förrän nivå 2–3 fungerar.

---

## 4. Testlogg

Alla projekt bör ha:

```text
docs/playtest-log.md
```

För större projekt kan även finnas:

```text
docs/playtest-guide.md
docs/balancing-notes.md
data/playtest-metrics.yaml
```

### 4.1 Mall: playtest-log.md

```markdown
# Playtestlogg

## Test 001 – YYYY-MM-DD

### Version

v0.1

### Testtyp

Solo-genomgång / intern test / observerat test / blindtest / balanspass

### Spelare

- Antal spelare:
- Ålder/erfarenhet:
- Vem förklarade reglerna:

### Testmål

- ...

### Setup

- ...

### Resultat

- Speltid:
- Vinnare:
- Slutpoäng:
- Antal rundor:
- Avbröts spelet? Ja/nej

### Observationer

- ...

### Vad fungerade

- ...

### Vad fungerade inte

- ...

### Frågor som uppstod

- ...

### Balansindikationer

- ...

### Beslut till nästa version

1. ...
2. ...
3. ...

### Ändra inte ännu

- ...
```

### 4.2 Viktigt fält: Ändra inte ännu

Det är ofta lika viktigt att dokumentera vad man inte ska ändra.

Exempel:

```markdown
### Ändra inte ännu

- Kortkostnaderna justeras inte förrän vi har testat med 3 spelare.
- Spelbrädet ritas inte om förrän rörelsereglerna är stabila.
```

---

## 5. Playtestguide

`docs/playtest-guide.md` bör beskriva hur nästa test ska göras.

Mall:

```markdown
# Playtestguide

## Syfte med nästa test

...

## Version som testas

...

## Saker vi särskilt observerar

- ...
- ...
- ...

## Saker vi inte testar den här gången

- ...
- ...

## Före testet

- Skriv ut ...
- Kontrollera ...
- Förbered ...

## Under testet

- Mät speltid.
- Notera regler som spelare frågar om.
- Notera när spelet stannar upp.
- Hjälp bara om testtypen tillåter det.

## Efter testet

Ställ dessa frågor:

1. Vad var tydligast?
2. Vad var mest oklart?
3. När kändes spelet roligast?
4. När kändes spelet långsamt?
5. Vilken regel glömde ni?
6. Vilken komponent var svårast att förstå?
```

---

## 6. Balansanteckningar

`docs/balancing-notes.md` bör användas för mer långsiktiga balansfrågor.

Mall:

```markdown
# Balansanteckningar

## Aktuell hypotes

...

## Kända balansrisker

- ...

## Värden att följa

| Värde | Önskat intervall | Observation |
|---|---:|---|
| Speltid | 20–30 min | |
| Antal rundor | 8–12 | |
| Kort per spelare | 3–6 | |
| Poäng vid slut | 8–12 | |

## Misstänkta problem

- ...

## Testade ändringar

| Version | Ändring | Resultat |
|---|---|---|
| v0.2 | ... | ... |
```

---

## 7. Vad GPT:n bör mäta

Mätvärden beror på speltyp, men ofta är följande användbara:

### 7.1 Allmänna mätvärden

- total speltid
- setup-tid
- regelgenomgångstid
- antal rundor
- antal turer per spelare
- genomsnittlig turlängd
- väntetid mellan turer
- slutpoäng
- poängskillnad
- antal gånger spelare frågar om regler
- antal gånger spelet stannar
- vilka komponenter som glöms
- vilka regler som glöms

### 7.2 Barnspel

- förstod barnen målet?
- kunde barnen ta turen själva?
- behövde vuxen läsa kort?
- blev någon frustrerad?
- var väntetiden för lång?
- ville barnen spela igen?

### 7.3 Kortspel

- handstorlek över tid
- hur ofta spelare saknar spelbara kort
- vilka kort spelas alltid?
- vilka kort spelas aldrig?
- hur ofta kortleken tar slut
- dominerande kortkombinationer

### 7.4 Äventyrsspel/nodkarta

- används alla vägar?
- fastnar spelare på vissa platser?
- är händelser för starka?
- är målet tydligt?
- tar resor för lång tid?

### 7.5 Coop

- hur ofta vinner spelarna?
- när förlorar de?
- styr en spelare de andra?
- känns hotet pressande?
- finns meningsfulla roller?

### 7.6 Deck-building

- hur snabbt blir leken bättre?
- vilka köp är självklara?
- finns döda kort?
- hur ofta blandas leken?
- hur lång tid tar spelet att accelerera?

---

## 8. Balansmål

GPT:n bör hjälpa användaren definiera mål.

Exempel:

```markdown
## Balansmål v0.2

- Spelet ska ta 20–30 minuter.
- En ny spelare ska förstå sin tur efter 2 rundor.
- Inget kort ska kännas obligatoriskt.
- Vinnaren ska oftast avgöras de sista 5 minuterna.
- Barn ska kunna spela sin tur med högst lite hjälp.
```

Balansmål ska vara konkreta och testbara.

---

## 9. Vanliga balansproblem

### 9.1 Dominant strategi

En strategi är för bra och används alltid.

Symptom:

- vinnaren gör samma sak varje spel
- spelare slutar överväga alternativ
- vissa kort/platser väljs alltid

Åtgärder:

- sänk belöning
- höj kostnad
- lägg till risk
- gör alternativ mer attraktiva
- begränsa frekvens

### 9.2 Döda val

Ett val är nästan aldrig bra.

Symptom:

- vissa kort spelas aldrig
- vissa rutter används aldrig
- vissa handlingar känns bortkastade

Åtgärder:

- förbättra valet
- förenkla bort valet
- ge valet en tydligare nisch
- kombinera med annat val

### 9.3 För mycket slump

Spelare känner att de inte påverkar.

Symptom:

- vinnaren avgörs av enstaka slag/kort
- planering spelar liten roll
- spelare uttrycker “det spelar ingen roll vad jag gör”

Åtgärder:

- ge fler val efter slumpen
- ge resurser för att modifiera resultat
- mildra negativa effekter
- minska straff
- låt spelare förbereda sig

### 9.4 För lite variation

Spelet känns samma varje gång.

Symptom:

- samma strategi
- samma öppning
- samma slut
- få överraskningar

Åtgärder:

- fler mål
- varierad setup
- modulära händelser
- små asymmetrier
- olika scenarier

### 9.5 För lång speltid

Symptom:

- spelet når “egentligt slut” innan det tar slut
- spelare tappar fokus
- senare rundor känns repetitiva

Åtgärder:

- sänk vinstkrav
- öka belöning
- korta banan
- minska antal rundor
- ta bort administrativa steg
- inför accelererande slutvillkor

### 9.6 För snabb snöboll

En ledare blir svår att stoppa.

Symptom:

- tidig ledning avgör
- rik blir rikare
- övriga spelare tappar hopp

Åtgärder:

- minska positiv feedback
- ge catch-up-mekanik
- gör belöningar mindre multiplikativa
- låt mål avslöjas senare
- ge risk med ledning

### 9.7 För hård negativ spiral

En spelare som ligger efter får svårare att komma tillbaka.

Åtgärder:

- mildra straff
- ge comeback-val
- låt förlorande spelare få kompensation
- undvik att ta bort turer
- undvik eliminering i familjespel

---

## 10. Balansjusteringar

GPT:n bör föreslå små justeringar först.

### 10.1 Justerbara parametrar

- antal kort på hand
- antal handlingar per tur
- rörelselängd
- kostnad
- belöning
- skada
- poäng
- vinstkrav
- antal rundor
- antal markörer i förråd
- sannolikhet i kortlek
- antal kopior av kort
- placering på spelbräde
- resurstillgång

### 10.2 Ändra helst en parameter

Om speltiden är för lång, välj en huvudjustering:

- sänk vinstkravet
- eller öka belöningarna
- eller minska banans längd

Gör inte alla samtidigt om det inte är uppenbart nödvändigt.

### 10.3 Dokumentera hypotes

Exempel:

```markdown
Hypotes: Spelet tar för lång tid eftersom spelare får för få stjärnor per runda.

Ändring: Öka belöningen på äventyrsrutor från 1 till 2 stjärnpoäng.

Förväntad effekt: Spelet slutar efter 8–10 rundor i stället för 12–15.
```

---

## 11. Speltest efter målgrupp

### 11.1 Barnspel

Prioritera:

- förståelse
- tempo
- tydlighet
- känsla
- låg frustration

Testfrågor:

- Kan barnet förklara målet?
- Kan barnet göra sin tur utan hjälp efter 2 rundor?
- Vilken symbol var svår?
- Vilket moment var roligast?
- När tappade barnet fokus?
- Var straff för hårda?

Balans är sekundärt i tidig barnspelsfas. Begriplighet är viktigare.

### 11.2 Familjespel

Prioritera:

- snabb inlärning
- jämn speltid
- lagom slump
- meningsfulla val
- låg väntetid

Testfrågor:

- Kunde spelet läras ut på under 10 minuter?
- Fick alla göra något intressant?
- Var någon ofta sysslolös?
- Var poängräkningen begriplig?
- Ville spelarna spela igen?

### 11.3 Hobbyspel

Prioritera:

- strategiskt djup
- balans mellan vägar
- återspelbarhet
- tydliga undantag
- dominanta strategier

Testfrågor:

- Finns flera gångbara strategier?
- Var någon strategi uppenbart bäst?
- Fanns intressanta avvägningar?
- Var administrationen värd djupet?
- Var reglerna konsekventa?

---

## 12. Speltest efter kategori

### 12.1 Kortspel

Testa:

- korttextens tydlighet
- handstorlek
- draw/discard-flöde
- starka kombinationer
- kort som aldrig spelas
- om korttyperna känns olika

### 12.2 Tärningsspel

Testa:

- om slag ger val
- hur ofta spelare misslyckas
- om sannolikheter känns rättvisa
- om spelaren kan mildra otur

### 12.3 Bana/race

Testa:

- om rörelse bara är slump
- om specialrutor gör skillnad
- om spelare kan komma ikapp
- om banan har intressanta vägval

### 12.4 Nodkarta/äventyr

Testa:

- om kartan erbjuder riktiga val
- om händelser avbryter för mycket
- om mål och belöningar är tydliga
- om spelare rör sig över hela kartan

### 12.5 Coop

Testa:

- vinstprocent
- hotnivå
- alfa-spelare
- rollernas betydelse
- om spelare känner gemensam press

### 12.6 Dungeon crawl

Testa:

- stridstid
- fiendevariation
- scenario-längd
- skada/läkning
- om spelarna gör taktiska val

### 12.7 Worker placement

Testa:

- om alla platser används
- om en plats är för stark
- om resurser stockar sig
- om rundor känns repetitiva

### 12.8 Deck-building

Testa:

- marknadens balans
- om startleken känns seg
- om spelet accelererar lagom
- om vissa kortköp är självklara

### 12.9 Tile placement

Testa:

- om scoring är begriplig
- om tiles ger intressanta val
- om slumpen i draget är lagom
- om fysisk hantering fungerar

---

## 13. Testscenarier

GPT:n kan hjälpa användaren skapa testscenarier.

### 13.1 Mikrotest

Syfte: testa en mekanik.

Exempel:

```markdown
Testa bara rörelse och händelser i 10 turer. Ignorera poäng och vinst.
```

### 13.2 Halv omgång

Syfte: testa tempo.

```markdown
Spela tills någon fått 2 stjärnor eller 15 minuter har gått.
```

### 13.3 Full omgång

Syfte: testa helheten.

```markdown
Spela hela spelet med nuvarande regler och logga speltid, vinnare och frågor.
```

### 13.4 Stresstest

Syfte: testa extremfall.

```markdown
En spelare försöker bara samla resurser. En annan rusar mot mål. Se vilken strategi som verkar starkast.
```

### 13.5 Blindtest

Syfte: testa regelbok.

```markdown
Ge spelarna bara komponenter och regelbok. Observera utan att hjälpa, om möjligt.
```

---

## 14. Hur GPT:n ska tolka speltestanteckningar

När användaren ger speltestanteckningar bör GPT:n:

1. sammanfatta observationerna
2. skilja fakta från känsla
3. identifiera möjliga orsaker
4. prioritera problem
5. föreslå få ändringar
6. föreslå vad nästa test ska kontrollera
7. uppdatera playtestlogg/balansanteckningar om användaren ber om det

### 14.1 Exempel

Anteckning:

```text
Spelet tog 55 minuter, barnen tappade fokus, men de gillade att dra händelsekort.
```

GPT-tolkning:

```markdown
Problem: Speltiden är för lång för målgruppen.
Det som fungerar: Händelsekorten skapar engagemang.
Trolig orsak: Vinstkravet eller rörelsen gör progressionen för långsam.
Föreslagen ändring:
1. Sänk vinstkravet från 3 mål till 2 mål för barnvarianten.
2. Låt vissa händelsekort ge extra rörelse.
Nästa test: Mät om spelet slutar inom 20–30 minuter.
```

---

## 15. Prioritering av problem

Alla problem är inte lika viktiga.

### 15.1 Kritiska problem

Åtgärda först:

- spelet går inte att spela klart
- spelarna förstår inte målet
- regler motsäger varandra
- komponenter saknas
- en spelare elimineras tidigt och får vänta länge
- första turen är oklar
- vinstvillkoret fungerar inte

### 15.2 Stora problem

Åtgärda efter kritiska:

- speltid fel för målgruppen
- en strategi dominerar
- vissa komponenter används aldrig
- för mycket administration
- barn förstår inte symboler
- turordning glöms ofta

### 15.3 Mindre problem

Vänta med:

- grafisk puts
- små formuleringar
- exakt ikonstil
- avancerad balans på kort
- premiumkomponenter
- specialfall som uppstår sällan

GPT:n bör hjälpa användaren att inte fastna i mindre problem för tidigt.

---

## 16. Beslutslogg

Större balans- och designbeslut bör dokumenteras.

Fil:

```text
docs/design-decisions.md
```

eller i `PROJECT_STATUS.md` under “Viktiga beslut”.

Mall:

```markdown
## Beslut 003 – Sänkt vinstkrav

Datum: YYYY-MM-DD
Version: v0.3

### Bakgrund

Test 002 tog 55 minuter för barn 7–10 år.

### Beslut

Vinstkravet sänks från 3 stjärnor till 2 stjärnor i barnvarianten.

### Förväntad effekt

Speltiden bör minska till cirka 25–30 minuter.

### Uppföljning

Testas i Test 003.
```

---

## 17. Balansdata i YAML

För större projekt kan GPT:n föreslå strukturerad balansdata.

Exempel:

```yaml
balance_targets:
  play_time_minutes:
    target_min: 20
    target_max: 30
  rounds:
    target_min: 8
    target_max: 12
  win_rate_coop:
    target_min: 0.4
    target_max: 0.6

tracked_metrics:
  - play_time_minutes
  - rounds_played
  - cards_drawn
  - energy_gained
  - stars_gained
```

Detta är inte nödvändigt i små projekt, men kan hjälpa när spelet växer.

---

## 18. Kortbalans

När spelet har kort bör GPT:n hjälpa användaren att analysera:

- kostnad
- effekt
- timing
- mål
- antal kopior
- korttyp
- krav
- risk
- belöning
- kombinationspotential

### 18.1 Enkel kortbalansmodell

GPT:n kan föreslå grov poängsättning.

Exempel:

```markdown
Riktvärde:
- Dra 1 kort ≈ 1 värde
- Få 1 energi ≈ 1 värde
- Flytta 1 extra steg ≈ 1 värde
- Få 1 stjärna ≈ 3 värde
- Förhindra fara ≈ 2 värde
```

Detta är inte absolut sanning. Det är ett verktyg för att upptäcka kort som sticker ut.

### 18.2 Kortgranskning

GPT:n bör leta efter:

- kort som gör samma sak men ett är bättre
- kort utan tydligt användningsområde
- kort med för lång text
- kort som kringgår kärnloopen
- kort som skapar oändliga kombinationer
- kort som är för starka i början/slutet

---

## 19. Kart- och brädbalans

För spel med karta bör GPT:n kontrollera:

- avstånd mellan start och mål
- om vissa rutter alltid är bäst
- om risk och belöning matchar
- om specialplatser är för starka
- om spelare samlas eller sprids
- om banan skapar beslut
- om spelare kan fastna

### 19.1 Nodkarta

Frågor:

- Har varje väg ett skäl att väljas?
- Är genvägar riskabla?
- Är långa vägar mer belönande?
- Är viktiga noder för långt bort?
- Finns flaskhalsar?

### 19.2 Bana

Frågor:

- Finns alternativ till att bara gå framåt?
- Finns catch-up?
- Är specialrutor jämnt fördelade?
- Tar det för lång tid att nå mål?

---

## 20. Ekonomi och resurser

Om spelet har resurser bör GPT:n analysera:

- hur resurser skapas
- hur resurser spenderas
- om resurser blir för många
- om spelare ofta saknar resurser
- om det finns meningsfulla val
- om en resurs är mer värdefull än andra

### 20.1 Vanliga problem

- resursinflation
- resursbrist
- en resurs är alltid bäst
- resurser saknar användning
- för mycket räkning
- för många token-typer

---

## 21. Slump och kontroll

Slump kan skapa spänning men också frustration.

GPT:n bör analysera:

- sker slump före eller efter spelarens val?
- kan spelaren påverka utfallet?
- är straff rimliga?
- är belöningar för swingiga?
- kan spelare planera trots slump?

### 21.1 Bra slump

- ger variation
- skapar spänning
- ger spelaren val efteråt
- kan mildras med resurser
- leder inte till total förlust på ett slag

### 21.2 Problem-slump

- avgör vinnaren utan motspel
- tar bort spelarens val
- straffar hårt utan möjlighet att reagera
- gör planering meningslös

---

## 22. Svårighetsgrad i coop

Coop-spel behöver ofta svårighetsbalans.

Mål kan vara:

- barn/familj: spelarna vinner ofta men inte alltid
- hobby-coop: 40–60 % vinstgrad
- kampanj: varierande svårighet

### 22.1 Justerbara parametrar

- startresurser
- hotökning per runda
- antal eventkort
- antal mål
- tidspress
- fiendestyrka
- antal spelare
- skalning per spelare

### 22.2 Skalning

För olika spelarantal kan GPT:n föreslå:

```yaml
scaling:
  players_1:
    threat_per_round: 1
    objectives_required: 2
  players_2:
    threat_per_round: 1
    objectives_required: 3
  players_3:
    threat_per_round: 2
    objectives_required: 3
  players_4:
    threat_per_round: 2
    objectives_required: 4
```

---

## 23. Tempo och speltid

GPT:n bör hjälpa användaren justera speltid.

### 23.1 Om spelet är för långt

Möjliga åtgärder:

- sänk vinstkrav
- korta banan
- öka belöningar
- minska antal rundor
- minska handlingsalternativ
- ta bort administrativ fas
- gör slutet accelererande

### 23.2 Om spelet är för kort

Möjliga åtgärder:

- höj vinstkrav
- lägg till delmål
- minska belöningar
- öka risk
- lägg till fler rundor
- skapa mer vägval

### 23.3 Om spelet känns segt men inte är långt

Orsaken kan vara:

- för lång väntetid
- för mycket administration
- för få beslut
- otydlig tur
- för många små räkningar
- för lite framsteg per tur

---

## 24. Regeltest

Regler ska testas, inte bara läsas.

GPT:n bör föreslå regeltest:

### 24.1 Förståelsetest

Ge en spelare regeln:

```text
På din tur får du göra upp till 2 handlingar.
```

Fråga:

- Vad får du göra nu?
- Får du göra samma handling två gånger?
- När slutar turen?

### 24.2 Setup-test

Be någon sätta upp spelet från regelboken.

Mät:

- tid
- frågor
- komponenter som saknas
- om något placeras fel

### 24.3 Första tur-test

Be någon spela första turen från regelboken.

Observera:

- var de tvekar
- vilka begrepp de inte förstår
- om komponenter ligger rätt

---

## 25. Blindtest

Blindtest är särskilt viktigt när spelet ska kunna delas.

### 25.1 Förberedelse

Skicka eller ge:

- regelbok
- printbara komponenter
- produktionsguide
- testfrågor
- version

### 25.2 Instruktion till testare

```markdown
Försök spela utan hjälp från designern. Markera alla ställen där regler eller komponenter är otydliga. Skriv gärna ner exakt vilken fråga som uppstod och när.
```

### 25.3 Efter blindtest

Fråga:

- Kunde ni förbereda spelet?
- Kunde ni förstå målet?
- Vilken regel behövde ni läsa om?
- Vilken komponent var otydlig?
- Kunde ni spela klart?
- Vad hade ni behövt på referenskortet?

---

## 26. Playtestrapport

När GPT:n sammanfattar test bör den skriva kort och handlingsinriktat.

Mall:

```markdown
# Playtestanalys

## Sammanfattning

...

## Viktigaste fynd

1. ...
2. ...
3. ...

## Sannolika orsaker

- ...

## Rekommenderade ändringar

1. ...
2. ...
3. ...

## Nästa test

Syfte: ...
Mät: ...
Behåll oförändrat: ...
```

---

## 27. Hur GPT:n ska uppdatera projektet efter test

När användaren ber GPT:n att genomföra justeringar efter test bör GPT:n:

1. uppdatera relevanta källfiler
2. uppdatera regelbok om regler ändras
3. uppdatera kortdata/tokendata/bräddata om komponenter ändras
4. uppdatera `docs/playtest-log.md`
5. uppdatera `docs/balancing-notes.md`
6. uppdatera `PROJECT_STATUS.md`
7. uppdatera `CHANGELOG.md`
8. regenerera output om användaren ber om det
9. paketera zip

GPT:n ska inte bara skriva en analys utan att föra in beslut i projektet när användaren vill fortsätta bygga på zippen.

---

## 28. När GPT:n bör avråda från balansarbete

GPT:n bör säga till om balansarbete är för tidigt.

Exempel:

- reglerna är inte spelbara
- komponenter saknas
- mål och vinstvillkor är oklara
- spelarna förstår inte turen
- spelet har bara testats en gång med hjälp från designern
- designern ändrar stora system varje gång

Då bör GPT:n rekommendera struktur- eller regeltest först.

---

## 29. När GPT:n bör rekommendera grafisk puts

Grafisk puts är lämplig när:

- grundloopen fungerar
- målgruppen förstår reglerna
- komponentlistan är stabil
- kortantalet inte ändras kraftigt
- speltest visar att spelet är värt att fortsätta
- printformaten är beslutade

Innan dess bör grafiken vara tydlig men inte överarbetad.

---

## 30. Definition of Done för steg 7

Steg 7 är klart när kunskapspaketet innehåller en playtest- och balansguide som beskriver:

- speltestprinciper
- testnivåer
- rekommenderad testordning
- playtestlogg
- playtestguide
- balansanteckningar
- mätvärden
- balansmål
- vanliga balansproblem
- balansjusteringar
- målgruppsanpassad testning
- kategorispecifik testning
- testscenarier
- tolkning av testanteckningar
- prioritering av problem
- beslutslogg
- strukturerad balansdata
- kortbalans
- kartbalans
- resursekonomi
- slump och kontroll
- coop-svårighet
- tempo och speltid
- regeltest
- blindtest
- playtestrapport
- projektuppdatering efter test
- när balansarbete är för tidigt
- när grafisk puts är lämplig
