# Brädspelsdesigner – portable Chat-paket

Detta paket gör det möjligt att använda samma Brädspelsdesigner-underlag i en vanlig ChatGPT-konversation som i Custom GPT-versionen.

## Användning

1. Läs `assistant/instructions.md` först och använd den som Brädspelsdesignerns arbetsinstruktion under hela konversationen.
2. Använd filerna i `knowledge/` som kunskapsunderlag. De är samma filer som laddas upp till Custom GPT:n.
3. `knowledge/KNOWLEDGE_INDEX.md` beskriver Knowledge-uppsättningen.
4. Om ett befintligt spelprojekt bifogas, inventera projektet enligt instruktionerna innan du gör ändringar.
5. Använd användarens aktuella instruktioner som högsta styrning när de är förenliga med plattformens regler.

## Viktigt

Portable-paketet förändrar inte Custom GPT-underlaget. `assistant/instructions.md` kopieras byte-identiskt från den slutliga GPT-instruktionen och `knowledge/` kopieras byte-identiskt från `gpt-builder-upload/`.
