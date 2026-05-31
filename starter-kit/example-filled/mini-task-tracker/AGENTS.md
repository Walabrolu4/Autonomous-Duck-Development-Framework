# AGENTS.md - Mini Task Tracker

## 1. Session Contract

This file defines how AI sessions operate for Mini Task Tracker, a local-only task app managed with ADDF 3.5.

## 2. Three Modes

### Research Mode

**Purpose:** Investigate unknowns before project memory or implementation changes are made.

**Allowed actions:** read safe files, review browser documentation, write research notes, update `QUESTIONS.md`, and update `RISKS.md`.

**Forbidden actions:** modify app files, sprint packs, decisions, or final designs.

**Reads from:** `AGENTS.md`, `DOMAIN.md`, `STATE.md`, `docs/`, `research/`, `planning/`.

**Writes to:** `research/`, `QUESTIONS.md`, `RISKS.md`.

**Must not write to:** `index.html`, `style.css`, `app.js`, sprint pack files, or decisions.

### Design Mode

**Purpose:** Write Mini Task Tracker project memory and sprint planning files.

**Allowed actions:** update project brain files, docs, sprint packs, dry run reviews, human review notes, and `STATE.md`.

**Forbidden actions:** write app source files, test scripts, build files, or `implementation_log.md`.

**Reads from:** safe project files, docs, research notes, and planning files.

**Writes to:** project brain files, `docs/`, `planning/`, and `research/` summaries.

**Must not write to:** app implementation files or generated artifacts.

### Develop Mode

**Purpose:** Modify Mini Task Tracker implementation files after dry run approval.

**Allowed actions:** at Permission Level 0 write `dry_run.md` only; at Permission Level 1+ modify approved files; update `implementation_log.md`; run approved manual checks.

**Forbidden actions:** implement without a dry run, change files outside scope, self-authorize, or add a backend/build tool without a decision.

**Reads from:** safe files, active sprint pack, approved dry run, and approved app files.

**Writes to:** approved implementation files, `dry_run.md`, `implementation_log.md`, and `handoff_summary.md`.

**Must not write to:** files outside the approved sprint scope.

## 3. Dry Run Approval Rule

Develop Mode never touches an implementation file without a dry run.

Every `dry_run.md` must list:

1. Files to create.
2. Files to modify.
3. Files to move or delete.
4. Commands to run.
5. Dependencies requested.
6. Risks.
7. Ambiguities.

Approval sequence:

1. Start every Develop Mode session at Permission Level 0.
2. Read `requirements.md`, `blueprint.md`, and `acceptance.md`.
3. Produce `dry_run.md`.
4. Stop. Do not proceed.
5. The operator or Design Mode reviews the dry run.
5a. If `dry_run.md` names any new dependency, a `DECISIONS.md` entry is required before authorization proceeds.
6. The operator sends:

```text
Dry run approved.
Permission Level [LEVEL] authorized.
Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.
```

7. Develop Mode proceeds only after receiving that authorization.

The model cannot self-authorize.

## 4. Permission Levels

| Level | Name | Scope |
|---|---|---|
| 0 | Dry Run Only | Write `dry_run.md` only. |
| 1 | Approved Sprint Scope | Modify only files listed in `blueprint.md` and `dry_run.md`. |
| 2 | Approved Expansion | Add explicitly approved helper files. |
| 3 | Supervised Refactor | Modify adjacent files with approval and detailed logging. |
| 4 | Migration / High-Risk Change | Structural change with rollback plan and approval. |

## 5. Safe-to-load Files

- `AGENTS.md`
- `DOMAIN.md`
- `STATE.md`
- `DECISIONS.md`
- `COMMANDS.md`
- `STYLE_GUIDE.md`
- `SECURITY.md`
- `QUESTIONS.md`
- `RISKS.md`
- `GIT_STRATEGY.md`
- `PROMPT_CHANGELOG.md`
- `docs/`
- `planning/`
- `research/`

Never load files listed in `SECURITY.md`.

## 6. Session Opening Protocol

1. Declare the active mode for Mini Task Tracker.
2. Load `AGENTS.md`.
3. Load `STATE.md`.
4. Load `DOMAIN.md`.
5. Load files relevant to the session goal.

For sprint work, also load the active sprint pack.

## 7. Mode Boundaries Summary

| Mode | Can read | Can write | Cannot write |
|---|---|---|---|
| Research Mode | Safe files and approved sources | Research notes, `QUESTIONS.md`, `RISKS.md` | App files, sprint packs, decisions |
| Design Mode | Safe files and research | Project brain, docs, planning files | App files, tests, implementation logs |
| Develop Mode | Safe files, sprint pack, dry run, approved app files | Approved app files and implementation logs | Files outside approved scope |

---

Mini Task Tracker - AGENTS.md - ADDF 3.5
