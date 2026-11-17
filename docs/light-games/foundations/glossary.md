# Glossary

A concise shared vocabulary matters because an AI can otherwise treat “approve,” “test,” or “sprint” too loosely.

## When to use

Use this when a term in a prompt, review, agent handoff, or validator report is unclear.

| Term | Meaning in ADDF Light Games |
| --- | --- |
| **Acceptance criteria (`AC-##`)** | Observable checks written **before implementation**; each must have a corresponding `REVIEW.md` result |
| **Agent / assistant** | An AI providing research, drafting or authorized implementation; it does not become the human project owner |
| **Backlog (`B-###`)** | Future candidate outcomes and experiments, not implementation authorization |
| **Capability** | Research, Design, or Develop write boundary; separate from the five lifecycle stages |
| **Decision (`D-###`)** | Consequential human choice, including alternatives, rationale and future revisit trigger |
| **Dry run** | Proposed exact file operations, commands, dependencies, risks and tests in `PLAN.md`, performed **without code edits** |
| **Evidence** | Source, actual test result, inspectable artifact or human observation; classified as verified/inferred/proposed/unknown |
| **Gate D** | Human decides material design direction and relevant sprint acceptance goal |
| **Gate I** | Human explicitly authorizes a **specific current plan revision and scope**, before source edits |
| **Gate A** | Human evaluates the actual outcome via first-hand test/review and supplies acceptance verdict |
| **Human owner** | Person who approves significant design, authorization and acceptance; may delegate routine within-scope work |
| **Light** | Low-friction daily use with thorough reference docs, not reduced safety or a light-color variant |
| **Learning checkpoint** | A short explanation/prediction tied to a design tradeoff and later observation |
| **Material scope change** | New paths, commands, dependency, risk, external effect or meaningful behavior; requires a revised Gate I |
| **Optional module** | Advanced architecture, risk, feature/release or asset tracking added only when necessary |
| **Plan revision (`rN`)** | Version of the technical authorization scope; old consent does not cover a materially changed revision |
| **Playable slice** | Small, observable player action and game response that can be evaluated in one bounded iteration |
| **Project brain** | Six persistent Markdown files recording safe rules, game intent, decisions, state and backlog |
| **Refinement round (`round-N`)** | Preserved record of feedback, correction, retest and verdict in `REVIEW.md` |
| **Research spike** | Bounded investigation with a specific evidence deliverable, not an automatically playable feature |
| **Sprint** | One bounded game outcome or focused research experiment, with `SPRINT.md`, `PLAN.md`, `REVIEW.md` once active |
| **Stage** | User-facing Research, Design/Ideation, Implement, Refine, Acceptance |
| **State/status** | Current operational position in `STATE.md`; status must match the stage and actual gate evidence |
| **Synthetic fixture** | Invented test data, which does not constitute a real person's approval or playtest |
| **T0 / T1 / T2** | Routine detail / consequential design choice / high-impact safety or cost decision |
| **Worktree** | Actual source-control checkout and uncommitted state; must be inspected before risky edits |

## Applying terms correctly

“Design approved” means Gate D, not permission to write source. “Plan authorized” means Gate I for exactly one revision/scope, not permission to deploy. “Automated test passed” is evidence, not Gate A. “Accepted with conditions” preserves those conditions and cannot silently become an unconditional release.

## Common failures

**Generic yes:** The human says “yes” but the agent cannot identify which revision and scope was displayed. Keep Gate I pending and ask a precise question.

**Invented test:** A model narrates “I opened the game” without tool evidence or the person's report. Mark unverified.

**Conflicting state:** The plan shows r2, the state refers to r1. Stop and reconcile.

## Related

[Workflow states](../lifecycle/index.md) · [Approval policy](../sprints/approvals.md) · [Validator](../quality/validation.md)
