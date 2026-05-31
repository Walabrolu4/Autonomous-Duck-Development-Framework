# Autonomous Duck Deployment Framework

ADDF is a file-first methodology for LLM-assisted software development. It keeps project memory in local Markdown files so an operator can resume work across models, sessions, interruptions, and long breaks without depending on chat history.

## Current Release

**Active release:** v0.1 Public Proof  
**Framework version:** 3.5

v0.1 exists so a competent operator can understand ADDF, copy the starter kit, and run a first ADDF session manually.

## Core Idea

The files are the project. The model reads the project files, operates in an explicit mode, and writes only what that mode allows.

ADDF uses three public modes:

| Mode | Purpose | Writes |
|---|---|---|
| Research Mode | Investigate unknowns and surface risks | `research/`, `QUESTIONS.md`, `RISKS.md` |
| Design Mode | Write project memory and sprint plans | project brain files, docs, sprint packs |
| Develop Mode | Modify approved implementation files after dry run authorization | `dry_run.md`, `implementation_log.md`, approved files |

## Dry Run Rule

Develop Mode starts at Permission Level 0. It produces `dry_run.md`, lists every planned file, command, dependency, risk, and ambiguity, then stops. The human reviews the dry run and authorizes implementation with the required message before any approved work begins.

## Repository Contents

| Path | Purpose |
|---|---|
| `AGENTS.md` | Session operating rules and mode boundaries. |
| `DOMAIN.md` | Project scope, terminology, and domain rules. |
| `STATE.md` | Current project status and next step. |
| `docs/` | Framework documentation and wiki pages. |
| `starter-kit/` | Blank and example-filled ADDF starter kits. |
| `prompts/` | Copy-ready prompt catalog for Research, Design, Develop, Handoff, and Maintenance workflows. |
| `planning/` | Dogfooding release, sprint, review, and audit artifacts. |

## Start Here

1. Read [`START_HERE.md`](START_HERE.md).
2. Review [`AGENTS.md`](AGENTS.md), [`DOMAIN.md`](DOMAIN.md), and [`STATE.md`](STATE.md).
3. Copy [`starter-kit/blank/`](starter-kit/blank/) into a new project.
4. Use the [`Prompt Catalog`](prompts/README.md) to start mode-specific AI sessions.

## Documentation

- [Wiki home](docs/index.md)
- [Prompt catalog documentation](docs/prompt-catalog.md)
- [Starter kit README](starter-kit/README.md)
- [Handoff protocol](docs/handoff-protocol.md)

## License

Starter kit and framework content are licensed under Creative Commons Attribution 4.0 International. See [`LICENSE`](LICENSE).

---

ADDF - README - Framework 3.5
