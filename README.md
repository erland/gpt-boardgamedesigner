# Brädspelsdesigner GPT

Detta repository innehåller den aktuella konfigurationen och Knowledge för Custom GPT:n **Brädspelsdesigner**, tillsammans med stöd för portabel Chat-distribution och versionsmärkta GitHub Releases.

## Aktuell GPT-konfiguration

Viktigaste filen inför GPT Builder är:

```text
preflight/COPY_TO_GPT_BUILDER.md
```

Den slutliga instruktionen finns i:

```text
gpt-final-config/final-instructions-under-8000-chars.md
```

Conversation starters finns i:

```text
gpt-final-config/final-conversation-starters.md
```

Knowledge som laddas upp finns i:

```text
gpt-builder-upload/
```

Mappen innehåller 15 numrerade Knowledge-filer samt `KNOWLEDGE_INDEX.md`, totalt 16 filer.

## Aktuellt testunderlag

- `gpt-final-config/final-test-matrix.md` – sammanfattad testmatris för GPT-konfigurationen.
- `tests/all-test-prompts.md` – samlade regressionstestprompter.
- `tests/release-and-build-workflow-test-prompts.md` – riktade tester för release-/build-arbetsflödet.

Historiska stegvisa arbetsanteckningar och separata stegtestfiler ligger inte längre i repositoryt; Git-historiken används för dem.

## Käll- och uppladdningsmaterial

`knowledge/` innehåller de namngivna kunskapsdokumenten utan uppladdningsprefix. `gpt-builder-upload/` är den faktiska uppsättning som används vid installation i GPT Builder.

## Portabel Chat-distribution och releaser

Repositoryt bygger två distributioner från samma aktuella GPT-underlag:

- `bradspelsdesigner-custom-gpt-vX.Y.Z.zip` – för GPT Builder. Slutlig instruktion, conversation starters och samtliga 16 Knowledge-filer kopieras byte-identiskt från källorna.
- `bradspelsdesigner-chat-vX.Y.Z.zip` – för en vanlig ChatGPT-konversation. Börja med `START-HERE.md`.

Lokalt eller vid vanlig push/PR används versionen i `VERSION`:

```bash
python3 scripts/build_distributions.py
python3 scripts/validate_distributions.py
```

Vid en publicerad GitHub Release används release-taggen som versionskälla. En release med taggen `v1.1.0` bygger och bifogar automatiskt:

```text
bradspelsdesigner-custom-gpt-v1.1.0.zip
bradspelsdesigner-chat-v1.1.0.zip
```

Taggen måste följa `v<semver>`, exempelvis `v1.0.0` eller `v1.2.3`.

## GPT Byggaren 1.5.0

Migreringen är **7/7 komplett**. Canonical instruktion finns i `assistant/instructions.md`; legacy-källan `gpt-final-config/final-instructions-under-8000-chars.md` bevaras. Build, validering och aktivt distributionsset härleds från `runtime-distribution-registry.yaml`.

Bevarat genom migreringen:
- version `1.0.0`
- 16/16 GPT Builder-Knowledge-filer
- instruktion under 8000 tecken
- projekt-zip som arbetsmodell
- källfiler framför genererad output
- uppdatering av `PROJECT_STATUS.md` och `CHANGELOG.md`
- print-and-play-principer
- regelboksstruktur
- playtest och balansarbete
- guidat nybörjarläge
- release/build-arbetsflöde

Aktiva runtimes är Chat och Custom GPT. OpenCode är compatibility-bedömd som equivalent candidate men inte aktiv. Claude Projects och OpenAI Plugin är reduced candidates och inte aktiva distributionsmål.
