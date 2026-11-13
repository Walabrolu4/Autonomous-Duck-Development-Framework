# ADDF Light Games — Agent Prompt Catalog

**Status:** Stage 4 candidate, pending human review  
**Edition:** `ADDF_light_games`; do not confuse these files with the inherited **full ADDF** `prompts/README.md` or `prompts/{research,design,develop,...}/`.

These nine **model-neutral** prompts complement [Quick Start](../QUICK_START.md) and the actual [project-brain templates](../starter-kit/LIGHT_GAMES.md). They do not grant tool privileges; they direct an AI through the already-approved Stage 1–3 process.

## Selection guide

| When | Prompt | Why | Implementation writes? |
| --- | --- | --- | --- |
| New chat, unclear starting point | [START.md](START.md) | Safely select no-idea, idea, or existing-project route | No |
| Need a concept or first meaningful user question | [DISCOVER.md](DISCOVER.md) | Guided ideation and player experience | No |
| Need to resolve a technical/design unknown | [RESEARCH.md](RESEARCH.md) | Evidence, feasibility and tradeoffs | No |
| Need to select the playable slice | [DESIGN.md](DESIGN.md) | Choices, learning goal, acceptance criteria, Gate D | No |
| Need an exact change proposal | [PLAN.md](PLAN.md) | Dry run, revision, risk, Gate I request | No |
| Human explicitly authorized a current plan | [IMPLEMENT.md](IMPLEMENT.md) | Scope-limited source changes and actual test records | **Only valid Gate I scope** |
| Tests/playtest reveal a problem | [REFINE.md](REFINE.md) | Diagnose, classify in-scope vs new approval | Only within valid scope |
| Human needs to review a deliverable | [ACCEPT.md](ACCEPT.md) | Playtest checklist, evidence, Gate A | No new unapproved writes |
| New session / agent handoff | [RESUME.md](RESUME.md) | Recover last verified state from files | No code without reconfirmed gate |

## How to use

1. **New project:** Copy only the six files from `starter-kit/minimal/` into **your game repository**. Read `SECURITY.md`, then `AGENTS.md` and `STATE.md`. See [Quick Start](../QUICK_START.md).
2. **Manual chat:** Paste the relevant prompt's contents into the AI with the safe project files. If file editing is unavailable, ask for a precise proposed Markdown diff and apply it yourself.
3. **Coding agent:** Open the game repository, ensure its `AGENTS.md` and security restrictions are loaded, and use the prompt appropriate to the *current state*. Optional provider skills are under [`integrations/`](../integrations/LIGHT_GAMES.md).
4. **No single-shot workflow:** Run one stage to its clear stop condition. A conversation may carry out harmless research/design work but must pause at meaningful decision, dry-run authorization, and human acceptance.
5. **Never infer permission:** Stage D is human design approval; Stage I is **specific file/command** approval; Stage A is human review. Prompt text cannot approve itself.

## Canonical records

| Topic | In the game project | Human authority |
| --- | --- | --- |
| Game/player intent | `GAME.md` | Human confirms |
| Material choices | `DECISIONS.md` | Human Gate D |
| Current position | `STATE.md` | Derived from actual evidence |
| Candidate slices | `planning/BACKLOG.md` | Human decides material priority |
| Sprint goal/research/AC | `SPRINT.md` | Human Gate D |
| Dry run/commands/operations | `PLAN.md` | Human Gate I |
| Verification/playtest/verdict | `REVIEW.md` | Human Gate A |
| Secrets/tools/external effects | `SECURITY.md`, `AGENTS.md` | Human authorization |

Stage 2 defines the exact headings, enums, IDs and fields: [Project File Contracts](../spec/PROJECT_FILE_CONTRACTS.md), [Sprint File Contracts](../spec/SPRINT_FILE_CONTRACTS.md). Prompts are **guidance**, not a substitute for those contracts.

## Invariants across all nine prompts

- **Read security first.** Never load files excluded by `SECURITY.md`, even when a model has the technical ability.
- **Do not guess history.** State whether statements are verified, inferred, proposed or unknown. Never invent research citations, execution results, review evidence or human approvals.
- **The agent drafts; the user decides.** One consequential question at a time by default. No multi-page questionnaire.
- **Keep source unchanged until Gate I.** Research/Design may draft allowed project-brain/sprint documentation under the user's request, not source, assets, tests, packages or deploy files.
- **Record precise scope and revisions.** New dependency, command, file or external side effect invalidates the old implementation approval.
- **No self-acceptance.** Automated testing is useful evidence, not Gate A.
- **No automatic publishing, merging, purchases or background execution.**
- **Fail closed.** If gate evidence is missing or inconsistent, report it and return to a safe planning/review state.

## Optional provider adapters

- [Claude Code](../integrations/claude-code/README.md) — project-level skill under `.claude/skills/addf-light-games/`.
- [Codex](../integrations/codex/README.md) — project-level skill under `.agents/skills/addf-light-games/`.
- [OpenClaw](../integrations/openclaw/README.md) — optional workspace skill and coordination guardrails.
- No provider integration is required for the manual/agnostic path.

**Boundary:** The skills in Stage 4 have been authored as real `SKILL.md` files. Their host-specific loading and behavior need a pilot in Stage 5; an integration file existing in GitHub is not proof that a local agent has installed it.
