# ADDF Light Games — Stage 5 Pilot Index

**Status:** Stage 5 pilot candidate; manual human verification pending.

This directory is a **test bed for the framework**, not the original full-ADDF example collection. It exercises the three approved starts, a minimal browser game, documented decision/approval boundaries, and safe handoff reasoning.

| Pilot | What it demonstrates | What is actually tested |
| --- | --- | --- |
| [From zero](from-zero/README.md) | No-idea and one-sentence routes; scoped decisions, Gate D/I/A scripts | Tabletop walkthrough, not real human conversation or coding-agent run |
| [Completed game](completed-game/README.md) | A dependency-free playable dodge prototype | Executable Node logic tests; optional automated Chromium browser smoke; user playtest still pending |
| [Existing project](existing-project/README.md) | Safe read-only adoption from an older game with existing rules | Auditable fixture file inventory and proposed changes, with no migrated files overwritten |
| [Pilot test matrix](TEST_MATRIX.md) | Test scope, permissions and unresolved coverage | Separates executed checks from simulated scenarios and deferred user/provider tests |

## Scope of Stage 5

Stage 5 intentionally includes executable game source, test scripts, a local browser prototype, and realistic workflow exercises. It **does not** claim that Claude Code, Codex, or OpenClaw were installed in the human's own environment, or that a human accepted a completed game sprint. Any simulated consent in written scenarios is labeled **fictional**.

**The human approved Stage 5 framework implementation**, not a concrete game project's `PLAN.md` Gate I. Consequently the code demo is an **authorized framework pilot artifact**; its existence must not be cited as evidence that an agent may bypass Gate I in someone's game repository.

## Launch the playable prototype

1. Open [completed-game/index.html](completed-game/index.html) from a clone/download of the **`ADDF_light_games`** branch.
2. Select **Start game**, move with arrow keys or W A S D, avoid red obstacles, and try pause/restart.
3. Review [completed-game/README.md](completed-game/README.md) and record your first-hand observations.
4. Do **not** mark the example human-accepted until that review actually occurs.

No public GitHub Pages deployment is included here, and the original site's `main` deployment is unchanged.

## Safe scenario progression

```text
No idea / idea / existing project
  → Research and real alternatives
  → Design selection and acceptance criteria (Gate D)
  → Exact dry run (Gate I)
  → Authorized implementation and verified tests
  → Human playable review (Gate A)
  → Resumption from durable files
```

The scenario documents show what should happen at each stop. Test scripts can prove game logic and fixture structural behavior, **not** that an LLM will obey these constraints under all circumstances.

## After Stage 5

Stage 6 is the **general-purpose automated project-file validator**. Stage 5's tests are deliberately *pilot-specific*. The full wiki, generated manual, logo, website, and release remain later stages.

**Review checkpoint:** [STAGE_05_REVIEW.md](STAGE_05_REVIEW.md). Stop before Stage 6.
