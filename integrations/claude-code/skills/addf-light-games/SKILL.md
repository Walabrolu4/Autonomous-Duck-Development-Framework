---
name: addf-light-games
description: Guide a human-led game project through ADDF Light Games discovery, research, sprint design, exact implementation authorization, testing, refinement and human acceptance. Use for new game ideas, existing-game adoption, planning, approved implementation or session resumption; stop at human gates.
---

# ADDF Light Games — Claude Code skill

Use this skill **inside the user's game project** after the human has intentionally installed its project-brain files. This skill does **not** grant tool access, consent to edit game code, or permission to run unapproved commands.

## First action: recover authority and current state

1. Read `SECURITY.md` **first** and obey its secret/permission exclusions. Do not read arbitrary repository files before security screening.
2. Read `AGENTS.md` and `STATE.md`. If these files don't exist, request a safe new-project setup or **read-only** adoption review; never overwrite existing files automatically.
3. Read `GAME.md`, `DECISIONS.md`, `planning/BACKLOG.md`, and active `planning/sprints/sprint-NNN/{SPRINT.md,PLAN.md,REVIEW.md}` as needed.
4. Verify actual project branch, current sprint, the last **human** gate response, authorized plan revision, test evidence, and outstanding blockers. Memory and predecessor chat aren't approvals.

## Select one stage; do not one-shot

**Research → Design / Ideation → Implement → Refine → Acceptance**; resume from verified state rather than starting over.

- **START / DISCOVER:** Accept no idea, one-sentence idea or existing-game start. Offer 2–3 small concepts when needed. Ask one consequential question at a time. No code edits.
- **RESEARCH:** Collect focused evidence, sources, uncertainties and feasible alternatives. Read-only investigation isn't a code authorization.
- **DESIGN:** Choose a bounded playable milestone and `AC-##` checks. Explain tradeoffs and learning goals. Record real human Gate D in `SPRINT.md`/`DECISIONS.md`. No code edits.
- **PLAN:** Draft exact `PLAN.md` file operations, commands, dependency versions, side effects, verification and rollback. Show the plan and **stop** for explicit human Gate I on the current revision.
- **IMPLEMENT:** Only when Gate I is verified for this exact revision and paths/commands, make authorized edits and run approved commands. Record actual outcomes. New scope/risk = stop and re-approve.
- **REFINE:** Classify observed failure as in-plan correction or new scope. Preserve review rounds; re-plan and seek Gate I when expanded.
- **ACCEPT:** Prepare verifiable run/playtest steps, criterion results and limitations. The **human** supplies Gate A; passing tests alone cannot close the sprint.
- **RESUME:** Reconcile files, actual diff and gates after interruption. If permission uncertain, fail closed and do not code.

When the canonical framework prompt catalog is available, use its corresponding `prompts/{START,DISCOVER,RESEARCH,DESIGN,PLAN,IMPLEMENT,REFINE,ACCEPT,RESUME}.md` as the detailed procedure; if not copied into the game repo, this skill plus game-project files is sufficient for safe routing.

## Mandatory human gates

- **D (design):** Actual human choice / non-required justification for meaningful sprint direction. **Not** code authorization.
- **I (implementation):** Actual human authorizes **specific `PLAN.md` revision and listed operations/commands/dependencies**. Must occur before source/scene/asset/test/config changes, even a quick fix.
- **A (acceptance):** Actual human personally tests/reviews; record `accepted`, `accepted_with_conditions`, `needs_refinement`, `rejected`, or `paused`.

Do not generate a faux “Human approved” response. Do not self-authorize or self-accept. New packages, paths, shell commands, external network destinations or higher risk invalidate old I. Publishing, merging, purchases, destructive actions, secret handling and third-party contact need separate explicit permission.

## Expected concise output each turn

- Verified stage/status and active sprint, or explicitly unknown.
- Work accomplished **with evidence**, or proposed (do not mix them).
- Project files updated or proposed.
- Scope boundary and any real gate evidence.
- **One next user decision or safe action**, stopping when a human gate is needed.

Use the project's original human intent and restrictions. Never “helpfully” replace its `AGENTS.md`, `SECURITY.md`, or existing work.
