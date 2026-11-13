---
name: addf-light-games
description: Run a human-led ADDF Light Games workflow for a game repository: idea discovery, focused research, design choice, sprint plan, approval-scoped implementation, refinement, playtest acceptance and safe resumption. Use only within the project's security and human gates.
---

# ADDF Light Games — Codex skill

Follow the **game project's** root `AGENTS.md` and `SECURITY.md`. This skill packages a repeatable procedure; it does not override safety constraints, change Codex sandbox settings, or expand execution authority.

## Startup and source of truth

1. Load `SECURITY.md` **before** exploring project files. Never load secrets, credentials or unrelated user directories.
2. Read `AGENTS.md` and `STATE.md`, then only relevant `GAME.md`, `DECISIONS.md`, `planning/BACKLOG.md`.
3. For the active `sprint-NNN`, verify all three records: `SPRINT.md`, `PLAN.md`, `REVIEW.md`. Examine actual branch, permitted paths, worktree and available evidence only within security rules.
4. Treat missing, ambiguous or stale human authorization as **not authorized**. Session memory, a green CI badge or tool permissions aren't human consent.

## Stages

**Research → Design / Ideation → Implement → Refine → Acceptance**

| Stage / prompt | What to do | What never happens without new authority |
| --- | --- | --- |
| START / DISCOVER | Ask one key question, or offer 2–3 playable concepts; support existing-project read-only audit | Auto-scaffold source, overwrite docs |
| RESEARCH | Gather real sources, weigh alternatives and unknowns; optionally prepare a bounded research spike | Unapproved installs, source changes |
| DESIGN | One observable playable slice, learning checkpoint, `AC-##`, actual human Gate D | Code edits based on enthusiasm |
| PLAN | Dry-run exact files/ops, commands, dependencies, risks, rollback; request Gate I for `rN` | Running planned commands before authorization |
| IMPLEMENT | Change only approved paths and run exact authorized commands; log real build/test outcomes | Widening scope, merging, deploying, self-approving |
| REFINE | Record human observation or verified failure; classify in-scope vs new plan | New dependencies or scope without revised Gate I |
| ACCEPT | Provide playable/inspectable verification and ask human Gate A; preserve each verdict round | Calling an unplayed build accepted |
| RESUME | Re-read files, compare source state and real approval evidence | Automatically continuing an interrupted command |

If framework instructions are accessible, consult `prompts/LIGHT_GAMES.md` and the matching detailed prompt. If they aren't, use this skill and the project-brain contracts; do not invent missing artifacts.

## Write permissions and approval integrity

- **Research and Design:** Only approved project-brain/sprint-planning Markdown; never product code, tests, assets, manifests, scenes or deploy config.
- **Develop:** Only after the human explicitly authorizes the **current** `PLAN.md` revision with exact operations, commands, packages and conditions. Record the actual authorization source. Review the diff and report failures.
- **Changed scope:** Stop, explain new operation/side effect/risk, revise the plan to the next revision and seek fresh Gate I. The old plan must not silently cover new work.
- **Special effects:** No unattended jobs, spending, third-party contacts, credential access, force resets, public publication or branch merges without separately explicit scope.
- **Acceptance:** Human Gate A in `REVIEW.md`, not a model verdict. Automated tests can support but cannot replace it.

## Answer format

Give a concise current-state report: **verified status**, **what changed**, **approval evidence**, **tests actually run**, **remaining unknowns**, and **one next human action**. Distinguish proposed from implemented and stop at human checkpoints.

This skill may be invoked as `$addf-light-games` when Codex supports local skill selection. The project owner must install it intentionally in `.agents/skills/addf-light-games/SKILL.md`.
