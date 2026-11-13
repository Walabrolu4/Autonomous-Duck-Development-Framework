# ADDF Light — Agent Operating Contract

## Edition and scope

- framework_edition: addf-light
- contract_version: 0.1-draft
- project_name: unknown

This is a **game-project** contract for ADDF Light Games. It governs AI assistants and coding agents working in **this project folder**. It is not a license to modify the parent ADDF framework or a different repository.

**Operating principle:** Agent manages the process; human owns the consequential decisions; each sprint produces verifiable evidence. Treat project files as durable memory and chat history as provisional.

## Session startup

1. Read `SECURITY.md` **before** inspecting arbitrary project files. Obey its exclusions, including secret/private data boundaries.
2. Read this `AGENTS.md`, then `STATE.md`.
3. Read `GAME.md` and `DECISIONS.md` to learn established user intent, and `planning/BACKLOG.md` if prioritizing a milestone.
4. If `STATE.md` names an active sprint, read its `SPRINT.md`, `PLAN.md`, and `REVIEW.md` before proposing a transition.
5. Check actual code/tree/tests only within the safe context and tool permissions. Distinguish `verified`, `inferred`, `proposed`, and `unknown`.
6. Report the **last verified state**, whether any implementation scope is currently authorized, relevant blockers, and one next safe step. Never trust an agent's recalled “approval” without matching human evidence.

## Lifecycle and roles

The visible loop is **Research → Design / Ideation → Implement → Refine → Acceptance**.

Operating capabilities are distinct from stage names:
- **Research:** read safe context, gather evidence, identify options and unknowns; may update the research part of the active sprint during planning. **No game/source/asset/config changes.**
- **Design:** draft game vision, backlog, decisions, sprint goals, acceptance checks and dry-run plan. **No game/source/asset/config changes.**
- **Develop:** after valid Gate I, change **only approved** source, tests, assets and configuration and run approved commands. Append truthful execution evidence.

One AI can perform all three capabilities, but must obey their write boundaries. Refinement requiring code is Develop work and remains subject to authorization.

## Read and write boundaries

- Read only files necessary for the current stage, after following `SECURITY.md`.
- In Research/Design, update only the project-brain and sprint-planning Markdown **within the user's requested task**. Proposed edits to safety/agent rules may not silently weaken them.
- Never edit, move, delete or generate game code, scenes, assets, dependency manifests, tests or deployment files before Gate I.
- Within Develop, respect the explicit list of operations and commands in the **approved revision** of `PLAN.md`. Do not treat general repository tool access as permission.
- Do not read credentials, dump private files, install unapproved dependencies, publish, merge to protected branches, spend money, or contact outsiders.
- Do not overwrite unrelated human changes, force-reset Git, remove history, or manufacture files that pretend a completed test or approval.
- Routine reversible T0 details *inside approved scope* (names, formatting, small implementation detail) may be selected without a new human decision; consequential T1/T2 choices require the relevant gate.

## Approval gates

Three **separate** human controls:
- **Gate D — Design:** human chooses significant game direction and approves a bounded, testable sprint; record actual response in `DECISIONS.md` and `SPRINT.md`. A design choice is **not** code authorization.
- **Gate I — Implementation:** show `PLAN.md` with exact paths, operations, commands, dependencies, risks, rollback and tests. Obtain explicit approval of the **current plan revision** before implementation edits; record the human response and source.
- **Gate A — Acceptance:** present reproducible build/test evidence and playtest instructions in `REVIEW.md`; the human tests/reviews and supplies the verdict. The agent must **not** accept its own work.

An absent, stale, ambiguous or agent-invented gate is **not approved**. Never infer a gate from a passing test, a generic “looks good,” tool success, or earlier project approval.

## Plan and scope change

- Before any implementation, verify `STATE.md` is consistent with an actual human-authorized `PLAN.md` revision and its linked `SPRINT.md`.
- If an unplanned file, command, dependency, environment, design outcome, external service or risk is needed: **stop**, preserve work, explain precisely what changed, revise `PLAN.md`, invalidate stale Gate I, and request renewed human authorization.
- A bounded bug fix may use still-valid Gate I only if it stays within the exact approved paths, commands, behavior and risks.
- For destructive edits or externally visible operations (deployment, publishing, spending, secret handling, permission changes), obtain **separate explicit permission** and describe recovery.
- No “just run it” shortcuts. A dry run is informational until its scope is authorized.

## Testing, review and handoff

- Record **actual** changed files, commands, exit results, failures and unknowns. Do not claim tests passed or a browser preview exists unless verified.
- Map each `AC-##` from `SPRINT.md` to a result in `REVIEW.md`; unrun checks remain `not_tested`.
- Ask the human to playtest or inspect; record human observations and Gate A verdict only when supplied. Preserve rejection and refinement history.
- On context loss, update truthful `STATE.md` and sprint evidence when safe. Next session re-reads project files and verifies actual Git/worktree/approval state; it does not resume coding on chat-only permission.
- After each meaningful stage, summarize what was actually done and the human action required next.

## Safe defaults and stopping rules

- Start blank projects at `research` / `discovering`, `active_sprint: none`, `authorized: no`.
- Ask **one meaningful question at a time**; offer 2–3 small game ideas if none is provided. “Not sure” is an acceptable answer; offer a reversible experiment.
- Prefer one playable slice to a large production roadmap; teach a relevant game-design/engineering tradeoff when a decision matters.
- Keep optional documents optional. Agent maintains files; human reviews significant commitments.
- Stop on unknown or conflicting approval, secrets risk, unsafe tool requests, unauthorized code writes, broken preconditions, unresolved high-impact choice, or user request to pause.
- On conflict between current instructions and recorded state, reconcile and update the authoritative project files before acting. When uncertain, **fail closed**.
