# Komponentekonomi och produktionskompromisser

Detta dokument hjälper GPT:n **Brädspelsdesigner** att resonera om komponentmängd, produktionsfriktion och vad som är rimligt i olika prototypnivåer.

Ett print-and-play-spel kan ha bra regler men ändå bli jobbigt att producera. GPT:n ska därför bedöma inte bara vad som är spelmässigt bra, utan också vad som är praktiskt.

---

## 1. Grundprincip

Varje komponent har en kostnad:

- designkostnad
- regelkostnad
- layoutkostnad
- utskriftskostnad
- klippkostnad
- monteringskostnad
- förvaringskostnad
- speladministration

GPT:n ska hjälpa användaren att minimera komponenter i tidig fas.

---

## 2. Komponentfriktion

### Låg friktion

- vanliga D6
- enkelsidiga kort
- A4-regelblad
- A4-spelbräde
- få fyrkantiga markörer
- lånade pjäser
- sleeves med vanliga kort bakom

### Medelhög friktion

- många kort
- många markörer
- A6-referenskort
- flersidigt spelbräde
- tiles
- individuellt laminerade kort
- kortbaksidor

### Hög friktion

- specialtärningar
- många runda tokens
- dubbelsidiga tiles
- många standees
- stor karta över flera A4
- många unika kort med grafik
- kampanjkuvert eller sortering

GPT:n bör avråda från hög friktion i första prototyp om det inte är centralt för spelet.

---

## 3. Produktionsbudget

GPT:n bör fråga eller anta produktionsbudget i tre dimensioner:

1. tid
2. material
3. verktyg

Exempel:

```markdown
Produktionsbudget: låg
- A4-skrivare
- sax eller enkel skärare
- A4-lamineringsfickor
- inga specialverktyg
```

Det påverkar komponentval.

---

## 4. Kort

Kort är ofta bra PnP-komponenter, men för många kort bromsar projektet.

### Riktvärden

- mikrotest: 12–18 kort
- första prototyp: 24–36 kort
- spelbar PnP: 36–72 kort
- större kortspel/deck-builder: 100+ kort, kräver mer balansarbete

GPT:n bör föreslå mindre kortlek först.

### Kostnadsfrågor

- behöver alla kort vara unika?
- kan vissa vara kopior?
- kan korttyper minskas?
- behövs kortbaksidor?
- kan sleeves lösa produktion?

---

## 5. Markörer

Markörer ökar administration.

Frågor:

- behövs fysisk markör?
- kan värdet spåras på bräde?
- kan vanliga kuber/mynt användas?
- kan flera markörer kombineras?
- är runda markörer värda extra arbete?

För barnspel ska markörer vara få och stora.

---

## 6. Spelbräde

Ett bräde ger närvaro men kan öka produktion.

### A4

- lätt
- bra för prototyp
- begränsat utrymme

### 2×A4

- mer plats
- kräver tejp/passning
- svårare laminering

### 4×A4 eller större

- hög friktion
- bör vänta tills spelet är stabilt

GPT:n bör börja med A4 om möjligt.

---

## 7. Tiles

Tiles ger variation men ökar produktion och setup.

GPT:n bör fråga:

- behövs tiles för kärnloopen?
- räcker en fast karta?
- räcker 12–16 tiles i första version?
- kan tiles vara fyrkantiga?

---

## 8. Specialtärningar

Specialtärningar är problematiska för PnP.

Alternativ:

- D6-tabell
- kortlek
- klistermärken
- symboltolkning av vanlig D6
- app/digital slump, om acceptabelt

GPT:n bör normalt föreslå vanlig D6 i första version.

---

## 9. Standees och pjäser

Standees är snygga men kostar arbete.

För prototyp:

- använd lånade pjäser
- använd färgade markörer
- använd mynt/kuber

Skapa standees först när:

- spelet är stabilt
- karaktärerna är viktiga
- visuell identitet behövs

---

## 10. Dubbelsidigt

Dubbelsidigt ökar produktionsrisk.

Undvik i första version om:

- exakt passning krävs
- många kort ska klippas
- användaren har hemmaskrivare
- kortbaksidor inte är mekaniskt nödvändiga

Alternativ:

- sleeves
- enkelsidigt
- gemensam baksida utan exakt kant
- vikbara komponenter

---

## 11. Beslutsmatris

GPT:n kan använda denna matris:

| Fråga | Om ja | Om nej |
|---|---|---|
| Är komponenten central för kärnloopen? | Behåll | Ta bort eller senarelägg |
| Kan den ersättas av något spelaren har hemma? | Rekommendera ersättning | Skapa PnP-komponent |
| Kräver den exakt klippning? | Vänta eller förenkla | OK |
| Behövs den i första testet? | Skapa enkelt | Lägg i senarelista |
| Ökar den reglerna? | Testa noga | Lägre risk |

---

## 12. Minimum viable prototype

GPT:n bör hjälpa användaren definiera MVP.

MVP ska bara innehålla komponenter som behövs för att testa kärnloopen.

Exempel:

```markdown
MVP för äventyrsspel:
- 1 enkel A4-karta
- 24 händelsekort
- 4 pjäser från annat spel
- 12 belöningsmarkörer
- 1 regelsida
```

Inte:

- 80 kort
- 6 scenarier
- illustrerade standees
- dubbelsidig karta
- avancerade markörer

---

## 13. Stegvis komponentutbyggnad

Rekommenderad ordning:

1. textprototyp
2. tydliga komponenter
3. printvänlig layout
4. referenskort
5. förbättrad grafik
6. alternativa spellägen
7. produktionsnära version

---

## 14. När GPT:n ska bromsa

GPT:n bör säga ifrån när:

- komponentmängden är för stor för första test
- användaren vill göra snygg grafik innan reglerna fungerar
- dubbelsidigt eller runda tokens skapar onödigt arbete
- många unika kort skapas utan balansplan
- flera varianter byggs innan grundspelet är spelbart

Säg det konstruktivt och föreslå enklare väg.

---

## 15. Definition of Done

Denna guide är komplett när GPT:n kan resonera om:

- komponentfriktion
- produktionsbudget
- kortmängd
- markörmängd
- brädstorlek
- tiles
- specialtärningar
- standees
- dubbelsidigt
- minimum viable prototype
- stegvis komponentutbyggnad
- när designen bör förenklas
