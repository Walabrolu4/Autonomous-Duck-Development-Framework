[Home](../index.md) → [File Reference](index.md)

# File Reference: Overview

## The Project Brain Files

The ADDF framework stores all project intelligence in a small set of Markdown files on your local drive. These files are not just documentation — they are the operating memory of the project. Every AI session reads from them; every sprint writes back to them. Because the project brain lives in files, the project survives rate limits, model swaps, lost chats, and long breaks. You can load these files into any capable LLM and restore full project context instantly.

There are two categories: **root tracking files** (which live at the project root and persist across every sprint) and **sprint folder files** (which are created fresh for each sprint). This page covers the root files. For sprint folder files, see [Sprint Files](sprint-files.md).

---

## Context Loading Table

Load only what the current session needs — loading everything wastes tokens and introduces noise. Use this table to determine which files to load for each session type.

| Session Type | Load These Files | Do Not Load |
|---|---|---|
| **Architect Planning** | AGENTS.md, STATE.md, DOMAIN.md, DECISIONS.md, QUESTIONS.md, RISKS.md | Full source code, old sprint folders |
| **Builder Implementation** | AGENTS.md, STATE.md, sprint requirements + blueprint + acceptance, COMMANDS.md, and only source files the sprint touches | DECISIONS.md, old sprints, unrelated files |
| **Audit Verification** | acceptance.md, dry_run.md, implementation_log.md, test output | Source files, DOMAIN.md |
| **Data Ingestion (Mode 4)** | AGENTS.md, FILE_INVENTORY.md, raw source documents (redacted) | Sprint files, source code |
| **Style Check** | AGENTS.md, DOMAIN.md, STYLE_GUIDE.md, files being validated | Sprint files |

> **Security check:** Before any session, verify that no file you are loading contains API keys, passwords, .env contents, or real user PII. See [SECURITY.md](security.md) for the never-upload list.

---

## File Pages

Individual reference pages for every root tracking file:

- [AGENTS.md](agents.md) — Persona rules and permission levels. Loaded in every single session.
- [STATE.md](state.md) — Living project status board. Updated at the close of every session.
- [DOMAIN.md](domain.md) — Business logic, entities, and workflows. The AI's specification.
- [DECISIONS.md](decisions.md) — Immutable ADR ledger. Records every significant technical decision.
- [COMMANDS.md](commands.md) — Run, test, build, deploy, and rollback commands.
- [STYLE_GUIDE.md](style-guide.md) — Naming conventions, code standards, and style rules.
- [SECURITY.md](security.md) — What may and may never be uploaded to an AI session.
- [GIT_STRATEGY.md](git-strategy.md) — Branching model and commit rules.
- [PROMPT_CHANGELOG.md](prompt-changelog.md) — Version history of all prompts used with the framework.
- [Sprint Files](sprint-files.md) — All 9 files inside a `planning/sprints/sprint_NNN/` folder.
- [Planning Files](planning-files.md) — `backlog.md` and `FILE_INVENTORY.md`.

## See Also

- [AGENTS.md](agents.md)
- [STATE.md](state.md)
- [DOMAIN.md](domain.md)
- [DECISIONS.md](decisions.md)
- [COMMANDS.md](commands.md)
- [STYLE_GUIDE.md](style-guide.md)
- [SECURITY.md](security.md)
- [GIT_STRATEGY.md](git-strategy.md)
- [PROMPT_CHANGELOG.md](prompt-changelog.md)
- [Sprint Files](sprint-files.md)
- [Planning Files](planning-files.md)
