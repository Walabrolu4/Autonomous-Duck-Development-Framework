# File Reference: Ownership and Minimum Contents

This reference explains **where each kind of truth lives**. Stage 2's Project and Sprint File Contracts remain normative for exact headings, keys and values; this page tells a human when to open and edit each document.

## When to use

Use to onboard a new model, find a missing decision or determine which file needs an update after implementation/playtesting.

## Six persistent game-project files

| Path | Canonical responsibility | Who decides? | When updated? |
| --- | --- | --- | --- |
| `SECURITY.md` | Excluded context, secret boundaries, tool/external-effect limits | Human/security policy; agent can propose tightening | Setup, new risk, tool changes |
| `AGENTS.md` | Session behavior, stage/capability boundaries and approval gates | Human adopts permissions | Setup or reviewed policy change |
| `GAME.md` | Player experience, mechanics, pillars, constraints, first playable hypothesis | Human confirms meaningful intent | Discovery or material design change |
| `STATE.md` | Current verified stage/status, active sprint, approval summary, next action | Agent derives from actual evidence; human controls gates | Any transition, blocker, handoff |
| `DECISIONS.md` | Significant `D-###` choices and reversals | Human owns T1/T2 choice | Decision made, deferred or superseded |
| `planning/BACKLOG.md` | Candidate `B-###` outcomes and research spikes | Human sets material priority | Ideas discovered, scope deferred, sprint closed |

A **blank** project has these six files and no sprint directory. `unknown` values are honest and valid. The agent fills records as the user answers; the user should not have to hand-author the files.

## Three files in an active sprint

| File | Main sections | Gate |
| --- | --- | --- |
| `planning/sprints/sprint-NNN/SPRINT.md` | Reason, player outcome, in/out scope, research, alternatives, learning, criteria, risks | D |
| `planning/sprints/sprint-NNN/PLAN.md` | Exact file operations, commands, dependencies/assets, implementation sequence, verification, rollback, execution record | I |
| `planning/sprints/sprint-NNN/REVIEW.md` | Build/test evidence, `AC-##` results, playtest steps, human observations, refinement rounds, retrospective | A |

For a specific game the three files must agree on `sprint_id`, `project_id` and `sprint_kind`. `PLAN.md` revisions use `r1`, `r2`, etc.; Gate I only applies to the current approved revision/scope.

## What is not mandatory

Architecture diagrams, deeper research reports, asset provenance logs, feature packages, releases, extra command registries and risk matrices are **optional modules**, not required at initialization. Add them when they solve a real coordination problem.

The original full ADDF's `DOMAIN.md`, `COMMANDS.md`, `QUESTIONS.md`, `RISKS.md`, separate dry runs and detailed sprint records may contain critical history. Do not erase them during an existing-project migration.

## Documentation versus project truth

The distribution repository contains `spec/`, `docs/light-games/`, `prompts/`, `starter-kit/`, `integrations/` and `examples/`. Its generated `MANUAL.md` is a *reference artifact*, not a game project's living state.

When wiki prose conflicts with exact contract fields, consult the approved `spec/` schema and current human decision before changing template behavior. A future framework update must be intentionally migrated into existing game projects.

## Common failures

**Everything in STATE:** One file stores all decisions and test results. Use it as summary; preserve source in decisions, plan and review.

**Approval in comments only:** A chat says “authorized” but plan revision isn't recorded. Keep unapproved.

**Premature advanced docs:** A beginner receives 20 blank files. Stay minimal until necessary.

## Related

[Project file contract](../../spec/PROJECT_FILE_CONTRACTS.md) · [Sprint file contract](../../spec/SPRINT_FILE_CONTRACTS.md) · [Sprint overview](../sprints/overview.md)
