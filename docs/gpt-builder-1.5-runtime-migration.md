# GPT Byggaren 1.5.0 – migreringsplan

Projekt: **Brädspelsdesigner**

## Preserve-first baseline

Migreringen ska bevara:
- version **1.0.0**
- exakt **16 GPT Builder-Knowledge-filer**
- den slutliga instruktionen byte-identiskt
- instruktionen under 8000 tecken
- file uploads som central capability
- kodkörning/dataanalys för zip-, fil- och valideringsarbete
- projekt-zip som arbetsmodell
- tydlig separation mellan källa och genererad output
- stegvis förändring av källfiler, status och changelog
- print-and-play-principer
- regelboksstruktur
- playtest- och balansarbete
- guidat nybörjarläge
- release/build-arbetsflöde
- befintlig preflight-checklista och testmatris
- befintliga Chat- och Custom GPT-distributioner

## Steg

1. Etablera canonical instruktion och projektkontrakt.
2. Normalisera capability-, artifact-, workspace/state- och tool-kontrakt.
3. Normalisera Chat och Custom GPT till samma canonical källa.
4. Bedöm Claude Projects och OpenCode.
5. Bedöm OpenAI Plugin.
6. Generalisera build, parity, CI och release via runtime-registry.
7. Slutlig readiness, dokumentationssynk och 7/7-gate.

## Aktivering av nya runtimes

En runtime får bara aktiveras om den kan bevara zip-/filflödet, strukturerad källredigering, projektstatus/changelog, print-and-play, regelbok, playtest/balans och release/build utan kritisk degradering.
