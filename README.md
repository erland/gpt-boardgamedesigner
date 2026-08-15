# Brädspelsdesigner GPT – Release-workflow-uppdatering

Detta paket bygger vidare på Preflight 10B och för in release-/build-förbättringarna från den uppladdade analysen.

## Nytt

- `knowledge/release-and-build-workflow.md`
- `gpt-builder-upload/15-release-and-build-workflow.md`
- uppdaterad `gpt-builder-upload/KNOWLEDGE_INDEX.md`
- uppdaterad slutlig instruktion
- uppdaterad testmatris
- `tests/release-and-build-workflow-test-prompts.md`
- `RELEASE_WORKFLOW_UPDATE_NOTES.md`
- uppdaterad preflight-rapport

## Preflight-status

**GODKÄND**

| Begränsning | Resultat |
|---|---:|
| Instruktion max 8000 tecken | OK |
| Slutlig instruktion | 5004 tecken |
| Knowledge-filer max 20 | OK |
| Knowledge-filer att ladda upp | 16 filer |

## Viktigaste fil inför GPT Builder

```text
preflight/COPY_TO_GPT_BUILDER.md
```

---

## Portabel Chat-distribution och releaser

Repositoryt kan nu bygga två distributioner från samma källor utan att ändra GPT:ns beteendestyrande filer:

- `bradspelsdesigner-custom-gpt-vX.Y.Z.zip` – för GPT Builder. Den slutliga instruktionen, conversation starters och alla 16 Knowledge-filer kopieras byte-identiskt från de befintliga källorna.
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
