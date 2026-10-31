# G01/G03 – första verifieringspasset

Detta pass kontrollerar **inte** språkmodellernas funktion i de fem värdarna. Skriptet `scripts/check_g01_g03_preflight.py` gör endast ZIP-CRC och kontroller av kända startfiler i distributionspaketen. Saknade eller oväntat namngivna arkiv rapporteras som NOT VERIFIED, aldrig PASS.

Kör efter att GitHub Actions byggt `dist/*.zip`:

```sh
python3 scripts/check_g01_g03_preflight.py --dist dist --output build/acceptance-preflight.json
```

G01 och G03 är fortfarande **NOT VERIFIED** tills testprompt och fullständigt svar, eventuella artefakter och bedömningsprotokoll samlats i Chat, Plugin, Claude Projects, Claude Skills och OpenCode.

Prioriterad manuell körning:
1. G01: Skapa ett print-and-play-spel för 7–10 år, 2–4 spelare, 20 min, A4. Kontrollera komponenter, regler, spelbar kärnloop och testplan.
2. G03: Öppna en ZIP med README, PROJECT_STATUS, källfiler och genererade filer. Verifiera inventering, status, käll-/outputseparation och korrekt nästa steg.

Godkänn inte release på grundval av offlinepreflight.
