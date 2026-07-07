# Mekanik- och balansmönster för Brädspelsdesigner

Detta dokument kompletterar spelkategori-guiden med mer konkreta designmönster för spelmekanik och balans.

Spelkategori beskriver ofta formen: kortspel, äventyrsspel, coop, dungeon crawl och så vidare. Mekanik beskriver vad spelaren faktiskt gör och vilka beslut som skapar spänning.

GPT:n ska använda detta dokument för att ge mer precisa råd om kärnloop, val, tempo, slump, resurser och balans.

---

## 1. Grundprincip: meningsfulla val

Ett meningsfullt val har minst två rimliga alternativ där spelaren förstår ungefär:

- vad valet kan ge
- vad valet kan kosta
- vilken risk som finns
- varför valet passar spelarens mål

Dåligt val:

```text
Ta 1 poäng eller ta 3 poäng.
```

Bättre val:

```text
Ta 1 säker poäng eller riskera en utmaning för att få 3 poäng.
```

GPT:n bör leta efter val som egentligen inte är val.

---

## 2. Kärnloop

Kärnloopen är den återkommande rytm som spelet bygger på.

Exempel:

```text
Dra kort → välj handling → flytta → lös ruta → få belöning → nästa spelare
```

GPT:n bör hjälpa användaren att hålla kärnloopen enkel i första prototypen.

### Kontrollfrågor

- Vad gör spelaren varje tur?
- Vilket beslut är viktigast?
- Hur leder turen mot vinst?
- Vad skapar variation?
- Vad skapar spänning?
- Vad kan tas bort utan att spelet faller?

---

## 3. Action economy

Action economy handlar om hur många saker spelaren får göra per tur.

Vanliga modeller:

- 1 handling per tur
- 2 handlingar per tur
- 3 action points
- gör 1 huvudhandling + 1 fri handling
- spela valfritt antal kort men begränsas av resurser
- välj 1 av flera platser/handlingar

### Risker

För få handlingar:

- spelaren känner sig låst
- turen blir slumpstyrd
- dåliga slag/kort känns hårda

För många handlingar:

- turen blir lång
- väntetid ökar
- analysförlamning
- barn tappar fokus

### Rekommendation

För barn/familjespel är “gör upp till 2 handlingar” ofta en bra start.

---

## 4. Risk och belöning

Risk/reward är centralt i många spel.

Bra risk/belöning:

- risken är begriplig
- belöningen är lockande
- spelaren kan välja att avstå
- resultatet känns spännande men inte orättvist

Dålig risk/belöning:

- förlusten är för hård
- belöningen är självklar
- slumpen avgör utan val
- spelaren kan inte påverka risk

### Justerbara parametrar

- sannolikhet
- belöning
- straff
- möjlighet att förbereda sig
- möjlighet att spendera resurs för att mildra risk
- hur ofta risken uppstår

---

## 5. Slump kontra kontroll

Slump skapar variation, men kontroll skapar ägarskap.

GPT:n bör analysera:

- sker slumpen före eller efter spelarens val?
- kan spelaren modifiera utfallet?
- finns säkra alternativ?
- är straffen rimliga?
- kan spelaren planera trots slump?

### Bra slump

- skapar variation
- ger överraskningar
- driver berättelse
- ger spelaren val efteråt
- mildras av resurser eller kort

### Problem-slump

- avgör vinnaren utan motspel
- gör planering meningslös
- straffar hårt utan förvarning
- skapar långa perioder utan kontroll

---

## 6. Tempo och pacing

Tempo handlar om hur spelet känns över tid.

GPT:n bör tänka på:

- setup-tid
- första meningsfulla beslut
- tid mellan belöningar
- väntetid mellan turer
- när spänningen ökar
- om slutet kommer i rätt tid

### Tecken på dåligt tempo

- spelare frågar “hur länge är det kvar?”
- första rundorna känns transport
- slutet är avgjort långt innan spelet slutar
- turerna blir längre men mer repetitiva
- spelare får vänta utan att planera

### Åtgärder

- korta setup
- ge snabb tidig belöning
- minska antal administrativa steg
- korta vinstkrav
- öka progression
- införa accelererande slut

---

## 7. Snöbollseffekt

Snöboll uppstår när ledaren får fler resurser och därför blir ännu starkare.

Positiv feedback är inte alltid dåligt, men kan göra spelet avgjort för tidigt.

### Symptom

- tidig ledning avgör ofta
- andra spelare tappar hopp
- ledaren får både poäng och bättre motor
- förlorare får färre val

### Motmedel

- belöningar som ger poäng men inte mer motor
- catch-up-mekanik
- ökande risk för ledaren
- flera målvägar
- dold poäng
- kortare spel

---

## 8. Catch-up

Catch-up hjälper spelare som ligger efter.

Bra catch-up ska ge hopp utan att kännas orättvis.

Exempel:

- den som ligger sist får välja först
- dyrare belöningar för ledaren
- alternativa mål för den som ligger efter
- risk för den som rusar fram
- gemensamma hot

Undvik catch-up som gör tidigare val meningslösa.

---

## 9. Kingmaking

Kingmaking uppstår när en spelare som inte kan vinna avgör vem som vinner.

Vanligt i:

- area control
- konfliktspel
- spel med direkt attack
- långa familjespel med stor poängskillnad

Åtgärder:

- kortare speltid
- dold poäng
- fler målvägar
- begränsa direkt attack mot enskild spelare
- låt spelet sluta innan utslagna spelare uppstår

---

## 10. Downtime

Downtime är tiden en spelare väntar utan att vara engagerad.

GPT:n bör särskilt bevaka downtime i barn- och familjespel.

Åtgärder:

- kortare turer
- samtidiga val
- reaktioner utanför tur
- planering under andras tur
- färre handlingsalternativ
- mindre administration

---

## 11. Resursekonomi

Resurser ska skapa val, inte bara bokföring.

Bra resurser:

- har tydlig användning
- är lagom knappa
- skapar avvägningar
- kan spenderas på flera sätt
- är lätta att hantera fysiskt

Risker:

- för många resurstyper
- resursinflation
- resurser utan användning
- en resurs är alltid bäst
- för många små markörer

För första prototyp: börja ofta med 1–3 resurstyper.

---

## 12. Poäng och scoring

Poängsystem ska stödja önskad spelupplevelse.

Vanliga modeller:

- först till mål
- flest poäng efter X rundor
- samla X objekt
- slutför uppdrag
- gemensamt mål
- high score
- överlevnad

### Risker

- poängen är svår att räkna
- spelare förstår inte vad som ger poäng
- scoring kommer för sent
- för många poängkällor i första versionen
- dold poäng gör att spelare inte vet hur de ligger till

### Rekommendation

För barn/familjespel: få poängkällor och tydligt mål.

---

## 13. Hand management

Hand management handlar om att kort på hand skapar val.

GPT:n bör bevaka:

- handstorlek
- hur ofta spelare drar kort
- om spelare ofta har ospelbara kort
- om korten är för lika
- om timing spelar roll
- om det finns skäl att spara kort

### Justeringar

- ändra handstorlek
- ändra draghastighet
- lägg till discard/draw
- minska kostnader
- öka antal bas-kort
- skapa fler användningsområden för kort

---

## 14. Set collection

Set collection fungerar när spelare tydligt förstår vad de samlar.

Bra set collection:

- mål är tydliga
- spelare kan påverka samling
- flera set är möjliga
- progression syns

Risker:

- för slumpigt
- för få val
- för lång tid att samla
- poängräkning blir otydlig

---

## 15. Push your luck

Push your luck kräver ett tydligt “stanna eller fortsätt”.

Bra frågor:

- Vad riskerar spelaren?
- Vad säkrar spelaren?
- Hur stor är nästa risk?
- Kan spelaren läsa situationen?
- Är förlusten mild nog?

För barn: milda straff och snabba rundor.

---

## 16. Dolda och öppna mål

Öppna mål:

- lättare att förstå
- mer direkt konkurrens
- bra för barn/familj

Dolda mål:

- mer spänning
- mindre kingmaking
- risk för förvirring
- svårare för barn

GPT:n bör välja måltyp efter målgrupp.

---

## 17. Interaktion

Interaktion kan vara:

- direkt attack
- blockering
- tävlan om resurser
- race
- handel
- gemensamt hot
- indirekt påverkan

För familjespel är indirekt interaktion ofta tryggare än hård attack.

För barnspel bör straff mot andra spelare vara milda.

---

## 18. Mekanikgranskning

När GPT:n granskar en design bör den kontrollera:

- finns meningsfulla val?
- vad är kärnloopen?
- är action economy rimlig?
- finns för mycket eller för lite slump?
- finns snöboll?
- finns catch-up?
- är downtime rimlig?
- är resursekonomin enkel nog?
- är scoring begriplig?
- passar interaktionen målgruppen?

---

## 19. Rekommenderad output från GPT:n

När användaren ber om mekanikanalys bör GPT:n svara med:

```markdown
## Kärnloop

...

## Styrkor

- ...

## Risker

- ...

## Balansfrågor

- ...

## Rekommenderade små ändringar

1. ...
2. ...
3. ...

## Nästa test

...
```

---

## 20. Definition of Done

Denna guide är komplett när GPT:n kan ge praktiska råd om:

- meningsfulla val
- kärnloop
- action economy
- risk/reward
- slump/kontroll
- tempo
- snöboll
- catch-up
- kingmaking
- downtime
- resursekonomi
- scoring
- hand management
- set collection
- push your luck
- interaktion
- mekanikgranskning
