# G03 ZIP-inventering – deterministiskt fixturetest

`python3 -m unittest discover -s tests -p 'test_g03_zip_inventory.py' -v`

Tester kör en liten fiktiv spelprojekt-fixture i minnet. Positivt fall innehåller `README.md`, `PROJECT_STATUS.md`, `CHANGELOG.md`, `docs/rules.md`, `data/cards.json`, `assets/board.svg` och `output/board.pdf`. Negativa fall kontrollerar saknad statusfil och otillåtna ZIP-sökvägar.

Dessa tester kontrollerar **endast testfixturens och inventeringskontraktets deterministiska beteende**. De bevisar inte att Chat, Plugin, Claude Projects, Claude Skills eller OpenCode kan importera projekt-ZIP eller faktiskt följer kontraktet. G03 i värdmiljö är fortsatt NOT VERIFIED. Release förblir blockerad.
