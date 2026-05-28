# Scope — v0.1 Public Proof

**Release:** v0.1.0  
**Primary reference:** `todos/ADDF_Project_Requirements_v2_1.md` §4, §21

This file is the authoritative scope boundary for v0.1. Use it to resolve "is this in sprint scope?" questions during sprint planning. If a proposed deliverable is not on the in-scope list, it requires a decision before being added.

---

## In scope for v0.1

### Repository root files

```
README.md                    — project overview (pre-existing seed, content finalized Sprint 001)
START_HERE.md                — first-session guide
LICENSE                      — awaiting Q001 resolution
CONTRIBUTING.md
CODE_OF_CONDUCT.md
CHANGELOG.md
VERSION.md
```

### Project brain files

```
AGENTS.md
DOMAIN.md
STATE.md
DECISIONS.md
COMMANDS.md
STYLE_GUIDE.md
SECURITY.md
QUESTIONS.md
RISKS.md
GIT_STRATEGY.md
PROMPT_CHANGELOG.md
```

### Documentation

```
docs/full-manual.md          — complete framework reference (single Markdown file)
docs/full-manual.pdf         — PDF export of full manual
```

The existing `docs/` seed files (`getting-started.md`, `modes/`, `sprint-loop.md`, etc.) are part of the wiki structure. Whether they are consolidated into `full-manual.md` or remain as separate pages is a design decision for Sprint 003 or a dedicated documentation sprint.

### Starter kit

```
starter-kit/blank/           — complete blank ADDF structure with placeholders
starter-kit/example-filled/  — Mini Task Tracker completed example (same as examples/)
starter-kit/README.md
starter-kit ZIP (release asset)
```

### Prompt catalog

```
prompts/research/            — 5 prompts
prompts/design/              — 9 prompts
prompts/develop/             — 5 prompts
prompts/handoff/             — 3 prompts
prompts/maintain/            — 5 prompts
Prompt catalog ZIP (release asset)
```

### Example project

```
examples/mini-task-tracker/
```

The example must show a complete project trail: `DOMAIN.md`, `STATE.md`, one full sprint (requirements, blueprint, acceptance, dry run, implementation log, human review, retrospective), and an explanation of how to resume from files.

### Assets

```
assets/logo/
  duck-logo.png
  duck-logo-ink.png
  duck-logo-paper.png
  duck-logo.svg              — if ready; PNG interim acceptable for v0.1
assets/lifecycle/
  lifecycle-diagram.png      — or .svg
assets/diagrams/
  [15 core framework diagrams in PNG and/or SVG]
```

The 15 required diagrams are listed in `todos/ADDF_Project_Requirements_v2_1.md` §15.3.

### Planning and dogfooding structure

```
planning/backlog.md
planning/releases/v0.1/
planning/sprints/sprint_001/ through sprint_009/
```

---

## Out of scope for v0.1

The following are explicitly deferred:

| Item | Deferred to | Reference |
|---|---|---|
| Public website | v0.2 | Requirements §8, §21 |
| Website homepage, Start Here page, etc. | v0.2 (Sprint 005, 006) | Requirements §8 |
| CLI initialization tool (`addf init`) | v0.3 (Sprint 010) | Requirements §13 |
| Web onboarding app | v0.4 (Sprint 011) | Requirements §14 |
| Expanded examples (web, game, data, docs) | v0.5 | Requirements §21 |
| User accounts | Not planned | Requirements §4 |
| Hosted backend | Not planned | Requirements §4 |
| Database | Not planned | Requirements §4 |
| Paid downloads | Not planned | Requirements §4 |
| Community forum | Not planned | Requirements §4 |
| Complex SaaS dashboard | Not planned | Requirements §4 |
| Real-time collaboration | Not planned | Requirements §4 |
| Fully automated agent runner | Not planned | Requirements §4 |
| Deep IDE integration | Not planned | Requirements §4 |
| Model hosting | Not planned | Requirements §4 |
| GitHub automation | Not planned | Requirements §4 |
| Polished commercial CLI | Not planned (prototype only for v0.3) | Requirements §4 |
| Requirement to use a specific LLM | Not planned | Requirements §4 |

**Rule:** If a sprint proposal touches an out-of-scope item, reject it or create a decision record before proceeding.

---

## Scope decision log

If the scope changes, record the change here with a date and reason.

| Date | Change | Reason | Decision ref |
|---|---|---|---|
| — | — | — | — |

---

*ADDF · `planning/releases/v0.1/scope.md` · maintained by Design Mode*
