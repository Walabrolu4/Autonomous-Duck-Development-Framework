# Existing Game Adoption Pilot — Legacy Paddle

**Status:** Read-only fixture and adoption walkthrough. No actual migration performed.

The [fixture/](fixture/) is a small, pre-existing JavaScript game project. Its key property is an **existing `AGENTS.md` file that must never be overwritten** by copying the ADDF Light Games starter kit blindly.

1. Inspect [fixture/README.md](fixture/README.md) and [fixture/AGENTS.md](fixture/AGENTS.md) before proposing any files.
2. Verify [fixture/paddle.js](fixture/paddle.js) can be read without claiming it was executed.
3. Read the [grounded read-only audit and proposed mapping](READ_ONLY_AUDIT.md).
4. The assistant should propose the new Light files and an `AGENTS.md` **merge**, then stop for a real human adoption approval.
5. After human migration approval, preserve existing files and record `project_origin: existing-project`. A separate first playable improvement still requires its own Gate D/I/A.

**This fixture is intentionally not modified** during the Stage 5 pilot. The [general adoption guide](../../starter-kit/EXISTING_PROJECTS.md) remains authoritative.

No credentials, paid services, network integrations, engine migration or Git history rewriting are authorized by this example.

Return to [Pilot Index](../README.md) and [Stage 5 Review](../STAGE_05_REVIEW.md).
