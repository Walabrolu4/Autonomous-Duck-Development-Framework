# Stage 04 — Agent Prompts and Integrations Review

**Status:** Stage 4 implementation committed; **awaiting human verification**  
**Branch:** `ADDF_light_games`  
**Previous stage:** Stage 3 approved by the human before this work  
**Scope:** Prompt and skill Markdown only. No source/game implementation, local coding-agent installation, OpenClaw setup, background task, cloud transport, website publishing, or changes to original ADDF files.

## 1. Files delivered

### Nine agent-neutral lifecycle prompts + catalog (10)

- [Prompt catalog](../prompts/LIGHT_GAMES.md)
- [START](../prompts/START.md) — safely select entry route
- [DISCOVER](../prompts/DISCOVER.md) — concept and player-action discovery
- [RESEARCH](../prompts/RESEARCH.md) — evidence and focused feasibility
- [DESIGN](../prompts/DESIGN.md) — bounded slice, criteria and Gate D
- [PLAN](../prompts/PLAN.md) — exact dry run and Gate I request
- [IMPLEMENT](../prompts/IMPLEMENT.md) — approved code/test/asset changes only
- [REFINE](../prompts/REFINE.md) — evidence-led corrections and scope escalation
- [ACCEPT](../prompts/ACCEPT.md) — human playtest, review and Gate A
- [RESUME](../prompts/RESUME.md) — safe context-free resumption/handoff

### Provider adapter overview and installable skills (9)

- [Integration overview](LIGHT_GAMES.md)
- [Claude Code README](claude-code/README.md)
- [Claude Code optional bridge](claude-code/CLAUDE.md.example)
- [Claude Code Agent Skill](claude-code/skills/addf-light-games/SKILL.md)
- [Codex README](codex/README.md)
- [Codex Agent Skill](codex/skills/addf-light-games/SKILL.md)
- [OpenClaw README](openclaw/README.md)
- [OpenClaw coordinator playbook](openclaw/COORDINATOR_PLAYBOOK.md)
- [OpenClaw Workspace Skill](openclaw/skills/addf-light-games/SKILL.md)

This review document is the **20th Stage 4 file**.

**Isolation:** Existing full-ADDF `prompts/README.md` and category subdirectories were not overwritten. These new files are the Light Games catalog. No project or distribution `AGENTS.md` was replaced.

## 2. Required manual file/path check

- [ ] I am viewing **`ADDF_light_games`** (not `main`).
- [ ] `prompts/LIGHT_GAMES.md` exists alongside the nine uppercase lifecycle prompts.
- [ ] There are exactly nine lifecycle prompts: START, DISCOVER, RESEARCH, DESIGN, PLAN, IMPLEMENT, REFINE, ACCEPT, RESUME.
- [ ] `integrations/LIGHT_GAMES.md` and the three adapter subfolders exist.
- [ ] Claude Code has `README.md`, `CLAUDE.md.example`, and `skills/addf-light-games/SKILL.md`.
- [ ] Codex has `README.md` and `skills/addf-light-games/SKILL.md`.
- [ ] OpenClaw has `README.md`, `COORDINATOR_PLAYBOOK.md`, and `skills/addf-light-games/SKILL.md`.
- [ ] Each `SKILL.md` begins with YAML frontmatter containing `name: addf-light-games` and a nonempty `description:`.
- [ ] The prior Stage 1–3 files remain unchanged, and `main` still contains original ADDF.

## 3. Required behavior review

- [ ] START/DISCOVER handle **no idea**, **one-sentence idea**, and **existing game** without blindly scaffolding code.
- [ ] RESEARCH demands real evidence or explicitly marked uncertainty; no invented sources.
- [ ] DESIGN requires a bounded player-facing outcome, relevant learning, and real Gate D or valid non-required rationale.
- [ ] PLAN exposes exact paths/operations, commands, dependencies, risk and rollback **before** Gate I.
- [ ] IMPLEMENT checks that human Gate I applies to this exact `PLAN.md` revision and scope before touching source files.
- [ ] REFINE distinguishes in-scope correction from out-of-scope additions requiring renewed Gate I.
- [ ] ACCEPT requires actual human playtest verdict and preserves failed/conditional review rounds.
- [ ] RESUME re-reads files and approval evidence rather than assuming another agent's memory is trustworthy.
- [ ] Provider skill instructions **do not** override the game's `SECURITY.md`/`AGENTS.md` or grant new permissions.
- [ ] Provider installation instructions are opt-in and **do not** overwrite existing user configuration without review.
- [ ] OpenClaw does not auto-schedule work, silently message third parties, connect to home machines or self-approve.
- [ ] All prompts indicate which stage and human action is next, rather than trying to finish the entire game.

## 4. Tabletop verification scenarios (NOT claims of a live test)

| Scenario | Correct expected behavior | Main prompt/adapter |
| --- | --- | --- |
| User says “I want to make a game, no idea what” | 2–3 small concepts, one question, no code | START/DISCOVER |
| User asks “Does Phaser support this?” and research tools unavailable | Say not verified; propose test/source; no invented documentation | RESEARCH |
| User approves movement mechanic, not technical plan | Gate D recorded; no source write until Gate I | DESIGN/PLAN |
| Human authorizes three paths, worker needs fourth | Stop; revise plan revision and obtain new Gate I | IMPLEMENT/REFINE |
| Build is green, user hasn't launched game | `awaiting_acceptance`; Gate A pending | ACCEPT |
| Player rejects feedback readability | Preserve rejection, diagnose, seek approval if asset scope changes | REFINE |
| Another chat/model says “we got approval yesterday” | Verify source in project files; if missing fail closed | RESUME |
| Codex skill loaded with shell tools | Tools don't themselves grant permission; honor `PLAN.md` | Codex skill |
| Claude Code has an existing `CLAUDE.md` | Merge a pointer after review, do not replace it | Claude README |
| OpenClaw worker requests remote shell after unverified Gate I | Refuse delegation until actual authorized scope and tooling | Coordinator playbook |
| User says “keep working in the background” without details | Require separate explicit scope and supported automation/remote setup; do not claim monitoring | OpenClaw skill |

## 5. Host-specific smoke tests deferred to Stage 5

These files are structurally valid **candidate skills**, but have **not** been installed and invoked in running Claude Code, Codex, or OpenClaw instances during Stage 4.

Stage 5 should verify:
1. Actual skill discovery in supported installed versions.
2. Blank, one-sentence and existing-repo entry routes.
3. Gate D-only response never triggers game code edits.
4. One complete Gate I-approved, bounded playable implementation on a disposable project.
5. Dependency/file scope expansion triggers a fresh authorization stop.
6. Real playtest and Gate A; no self-acceptance.
7. Session/model handoff recovers safe project state.
8. OpenClaw workspace handling remains isolated; remote coordination only if separately configured and approved.

**A file existing is not evidence that the corresponding runtime successfully loaded it.** This is intentionally tracked as a future test, not misreported as complete.

## 6. Why the adapters are deliberately thin

The original Stage 1–3 contracts live in `spec/`, the nine **game project** files and agent-neutral prompt catalog. Provider wrappers contain enough startup and safety guidance to work independently, but defer to the user's game project for exact intent, permission and human verdicts. This prevents Claude, Codex and OpenClaw from becoming three conflicting “authoritative” versions of the methodology.

`AGENTS.md` remains the key shared guidance in game repositories. Claude's optional `CLAUDE.md.example` adds a pointer because that host also reads its own project guidance. The actual Claude/Codex/OpenClaw Agent Skills require deliberate installation in the *game project* or designated OpenClaw workspace.

## 7. Approval and pause

**Stage 4 is implemented, not yet human-approved.** Review the files and the checklist; request any changes before proceeding.

An explicit response after verification could be:

> “I have reviewed Stage 4 and approve the agent-neutral prompts and Claude Code, Codex and OpenClaw adapters. Proceed with Stage 5: pilot games and end-to-end tests. Stop again for my review.”

Do not start Stage 5 until the human expressly approves it. The release claim is still **candidate**, not production-tested.
