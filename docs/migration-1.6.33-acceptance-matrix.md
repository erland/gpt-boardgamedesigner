# Acceptance matrix – five peer runtimes

All cells are **NOT VERIFIED** pending actual host execution. This document is the runnable test plan, not fabricated test output.

| Scenario | Chat | Plugin | Claude Project | Claude Skills | OpenCode |
|---|---|---|---|---|---|
| A. Children's print-and-play prototype | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |
| B. Card versus board decision | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |
| C. Existing project ZIP analysis | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |
| D. Playable rulebook | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |
| E. Playtest and balancing recommendations | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |
| F. Honest production/release classification | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED | NOT VERIFIED |

Use the existing prompts in `gpt-final-config/final-test-matrix.md` and `tests/all-test-prompts.md`. For each test save: prompt, host/model, complete response, any generated assets, PASS/FAIL/NOT VERIFIED, and precise evidence.

Acceptance gate: all core behaviors PASS on activated hosts, or a documented supported host limitation and corresponding fallback is accepted. Merely finding instructions in ZIP files does not constitute a behavioral PASS.

Prior to release, regenerate all five archives from the official pinned 1.6.33 engine and inspect Plugin and Claude Skills Knowledge coverage specifically. Historical Custom GPT is not a sixth active runtime.
