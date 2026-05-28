# DOMAIN.md

**The Autonomous Duck Deployment Framework — project scope, entities, and domain rules.**

This file defines what this project is, what it is not, what terms mean, and what the boundaries are. Load it in any Design Mode or Develop Mode session.

---

## 1. Project identity

**Full name:** Autonomous Duck Deployment Framework  
**Short name:** ADDF  
**Type:** File-first methodology for LLM-assisted software development  
**Primary principle:** The files are the project.  
**Framework version:** 3.5  
**Requirements document:** `todos/ADDF_Project_Requirements_v2_1.md`

This repository is both the distribution point and the reference implementation for ADDF. It uses ADDF internally to build itself.

---

## 2. What this project is

ADDF is a system of files, prompts, protocols, and review gates that lets operators use LLMs without making the chat thread the project memory.

This repository provides:

1. Full framework documentation.
2. `START_HERE.md` for first-session onboarding.
3. A downloadable starter kit (blank and example-filled).
4. A prompt catalog grouped by mode.
5. A worked example project (Mini Task Tracker).
6. A session handoff and resumption protocol.
7. Branding assets and style rules.
8. Versioning, changelog, and contribution materials.
9. A public website (v0.2).
10. A CLI initialization tool (v0.3).
11. A web onboarding app (v0.4).

---

## 3. What this project is not

ADDF is not:

- A SaaS product.
- An AI assistant.
- An agent runtime.
- A model wrapper.
- A code editor plugin.
- A project management tool.
- A CI/CD system.
- Anything that requires a specific LLM.

---

## 4. v0.1 scope — Public Proof

v0.1 is the first public release. Its goal is:

> A competent operator can understand ADDF, download the starter kit, and run the first session manually.

### In scope for v0.1

```
README.md
START_HERE.md
Full manual Markdown (docs/full-manual.md)
Full manual PDF
starter-kit/blank/
starter-kit/example-filled/ (Mini Task Tracker)
examples/mini-task-tracker/
prompts/ (all five groups: Research, Design, Develop, Handoff/Resumption, Maintenance)
assets/logo/
assets/lifecycle/
assets/diagrams/ (15 core framework diagrams)
Project brain files (AGENTS.md, DOMAIN.md, STATE.md, DECISIONS.md, COMMANDS.md,
                     STYLE_GUIDE.md, SECURITY.md, QUESTIONS.md, RISKS.md,
                     GIT_STRATEGY.md, PROMPT_CHANGELOG.md)
planning/ (dogfooding structure)
CHANGELOG.md
VERSION.md
LICENSE
CONTRIBUTING.md
```

### Out of scope for v0.1

The following are explicitly deferred to later releases:

| Item | Target release |
|---|---|
| Public website | v0.2 |
| CLI initialization tool (`addf init`) | v0.3 |
| Web onboarding app | v0.4 |
| Expanded examples (web, game, data, docs) | v0.5 |
| User accounts | Not planned |
| Hosted backend | Not planned |
| Database | Not planned |
| Real-time collaboration | Not planned |
| Paid downloads | Not planned |
| Community forum | Not planned |
| GitHub automation | Not planned |
| Model hosting | Not planned |
| Complex SaaS dashboard | Not planned |
| Fully automated agent runner | Not planned |
| Deep IDE integration | Not planned |
| Requirement to use a specific LLM | Not planned |

**Rule:** Do not automate a structure that has not stabilized.

---

## 5. Target operators

The primary audience is competent developers and technical leads. Write to them as peers.

| Operator type | Primary need |
|---|---|
| Senior developers and technical leads | Protocol, file-backed project memory, reviewable output |
| Solo builders | Starter templates, dry-run discipline, resumption support |
| Educators | Diagrams, examples, visible lifecycle and review gates |
| Creative technologists and designers | `START_HERE.md`, minimal starter kit, plain file structure |
| Small teams | `DECISIONS.md`, `STATE.md`, sprint folders, handoff protocol |

---

## 6. Core framework concepts

### 6.1 Work scale model

```
Project → Release → Feature → Sprint → Patch
```

Scale controls process depth. A patch needs no sprint pack. A release needs a release plan.

### 6.2 Operating modes

```
Research Mode — investigates
Design Mode — writes project memory
Develop Mode — modifies implementation files after dry run approval
```

Only three modes exist in this framework. Do not refer to Architect Mode or Builder Mode as public ADDF modes.

### 6.3 8-step lifecycle

```
1. Research
2. Design & feasibility
3. Validation
4. Architecture
5. Sprint planning
6. Build & test
7. Review & reflection
8. Deploy, maintain, or resume
```

### 6.4 Sprint loop

```
1. Pre-flight gate
2. Design sprint pack
3. Human blueprint review
4. Develop dry run
5. Design review of dry run
6. Dependency approval gate
7. Authorize development
8. Build & test
9. Design review of output
10. Human approval gate
11. Commit, update, reset
```

### 6.5 Project brain

The project brain is the local Markdown file set that defines project truth. It is loaded into AI sessions to provide context without inheriting a chat thread.

Required project brain files:

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

---

## 7. Key entities and terminology

| Term | Definition |
|---|---|
| Operator | The human using ADDF to coordinate LLM-assisted work. |
| Model | Any LLM running in a session: Claude, Codex, ChatGPT, Gemini, etc. |
| Project brain | The local Markdown file set that constitutes project memory. |
| Sprint pack | The three files that define a sprint: `requirements.md`, `blueprint.md`, `acceptance.md`. |
| Dry run | The list of every file Develop Mode intends to create, modify, or delete, produced before any implementation begins. |
| Permission level | The 0–4 scale controlling Develop Mode freedom. |
| Handoff | The process of ending one model session and resuming work in a new session, using files as the sole continuity mechanism. |
| Local File Sovereignty | The principle that project memory lives on the operator's machine in Markdown files, not in a chat thread. |
| Starter kit | The downloadable file structure that lets an operator copy ADDF into any project. |
| Prompt catalog | The collection of copy-ready prompts organized by mode. |

---

## 8. File naming conventions

| Type | Convention | Example |
|---|---|---|
| Project brain files | `UPPER_SNAKE_CASE.md` | `STATE.md`, `DOMAIN.md` |
| Sprint folders | `sprint_NNN` | `sprint_001`, `sprint_023` |
| Sprint files | `lowercase_snake.md` | `blueprint.md`, `dry_run.md` |
| Documentation pages | `lowercase-kebab.md` | `getting-started.md` |
| Release folders | `vN.N/` | `v0.1/`, `v1.0/` |
| Feature folders | `feature-name/` | `core-task-list/` |

Always wrap file names in backticks in prose: `STATE.md`, not STATE.md.

---

## 9. Domain rules

1. The public repository uses ADDF internally. Every sprint, release, and feature is documented.
2. This repository is the reference implementation of the framework, not just its distribution point.
3. No secrets, tokens, API keys, or private infrastructure paths are ever committed.
4. Framework terminology must remain consistent across all surfaces (docs, prompts, website, starter kit, examples).
5. The three public modes are Research Mode, Design Mode, and Develop Mode — no others.
6. Every public artifact has a version.
7. The starter kit defines the output that the CLI will later generate.
8. Handoff protocol is a core deliverable, not an afterthought.

---

*ADDF · `DOMAIN.md` · maintained as part of the project brain*
