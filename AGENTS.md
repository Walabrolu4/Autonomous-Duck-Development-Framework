# AGENTS.md

**The Autonomous Duck Deployment Framework — session operating rules.**

Load this file first in every AI session. It defines the mode contract for this repository.

---

## 1. The three modes

ADDF operates in exactly three modes. Every AI session must declare one mode before acting. The mode is the write-permission contract for the session.

### Research Mode

**Purpose:** Investigate and synthesize information.

**Allowed actions:**
- Read any safe-to-load file.
- Search documentation, specifications, and external sources.
- Produce research notes, source summaries, tool comparisons, and open questions.
- Update `QUESTIONS.md` with new unknowns surfaced during research.
- Add to `RISKS.md` if a new risk is identified.

**Forbidden actions:**
- Modify source code, implementation files, or website files.
- Modify sprint files (`requirements.md`, `blueprint.md`, `acceptance.md`).
- Make or record architectural decisions.
- Produce final designs or specifications.

**Writes to:** `research/` notes, `QUESTIONS.md`, `RISKS.md`.

**Must not write to:** Sprint plan files (`requirements.md`, `blueprint.md`, `acceptance.md`), `docs/` (substantive changes), implementation files.

---

### Design Mode

**Purpose:** Write the project memory. Convert research, intent, and human feedback into durable Markdown artifacts.

**Allowed actions:**
- Create and update all project brain files.
- Create and update sprint packs (`requirements.md`, `blueprint.md`, `acceptance.md`).
- Create and update release plans, feature briefs, retrospectives, and handoff notes.
- Record decisions in `DECISIONS.md`.
- Update `STATE.md`.
- Create documentation Markdown files in `docs/`.
- Create starter kit files, prompt catalog files, and example project files.
- Review dry run output and produce `dry_run_review.md`.

**Forbidden actions:**
- Write source code.
- Write or modify website implementation files (HTML, CSS, JS).
- Write CLI tool code.
- Write test files or scripts.
- Modify `implementation_log.md` (that is Develop Mode's file).

**Writes to:** All project brain files, sprint planning files, `docs/`, `prompts/`, `starter-kit/`, `examples/`, `assets/` (description files only).

**Must not write to:** `website/src/`, `tools/`, `*.js`, `*.ts`, `*.py`, `*.sh`.

---

### Develop Mode

**Purpose:** Modify implementation files after dry run approval. This is the only mode that changes code, website source, or tool scripts.

**Allowed actions:**
- At Permission Level 0: produce `dry_run.md` only. No file modifications.
- At Permission Level 1+: modify only files listed in the approved `blueprint.md` and `dry_run.md`.
- Update `implementation_log.md` with changes made.
- Write and run tests within the approved scope.

**Forbidden actions:**
- Implement without a dry run at Level 0 first.
- Modify files outside the approved blueprint without an explicit human authorization for a higher permission level.
- Self-authorize a permission level escalation.
- Invent rules or constraints not present in the project brain.

**Writes to:** `dry_run.md`, `implementation_log.md`, `handoff_summary.md`, and implementation files approved in `blueprint.md`.

**Must not write to:** Project brain files (use Design Mode for those), files outside the approved sprint scope.

---

## 2. Dry run approval rule

**Develop Mode never touches an implementation file without a dry run.**

The sequence is:

1. Start every Develop Mode session at Permission Level 0.
2. Read the sprint pack: `requirements.md`, `blueprint.md`, `acceptance.md`.
3. Produce `dry_run.md` listing: files to create; files to modify; files to move or delete; commands to run; dependencies requested; risks; and ambiguities.
4. Stop. Do not proceed.
5. Design Mode (or the human) reviews the dry run against the sprint pack.
5a. If `dry_run.md` names any new dependency, a `DECISIONS.md` entry for that dependency is required before authorization proceeds.
6. The human sends the authorization message:

```
Dry run approved.
Permission Level [LEVEL] authorized.
Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.
```

7. Develop Mode proceeds only after receiving this exact authorization.

**The model cannot self-authorize.** If the model determines mid-session that it needs a higher permission level, it stops and reports the need. The human decides.

---

## 3. Permission levels

| Level | Name | Meaning |
|---|---|---|
| 0 | Dry Run Only | Read-only analysis of intended changes. No implementation. |
| 1 | Approved Sprint Scope | Modify only files approved in `blueprint.md` and `dry_run.md`. |
| 2 | Approved Expansion | Add minor helper files surfaced in the dry run and explicitly approved. |
| 3 | Supervised Refactor | Modify adjacent files with explicit approval and detailed logging. |
| 4 | Migration / High-Risk Change | Structural changes or architecture-heavy work. Requires a rollback plan. |

**Rule:** Permission level controls Develop Mode freedom.

---

## 4. Safe-to-load files

These files may be loaded into any AI session without restriction:

```
AGENTS.md
DOMAIN.md
STATE.md
DECISIONS.md
COMMANDS.md
STYLE_GUIDE.md
QUESTIONS.md
RISKS.md
GIT_STRATEGY.md
PROMPT_CHANGELOG.md
CHANGELOG.md
VERSION.md
README.md
START_HERE.md
docs/
planning/
prompts/
starter-kit/
examples/
research/
```

**Never load:**
- Any `.env` file.
- Any file containing API keys, tokens, or credentials.
- Any file with private infrastructure paths or personal contact information.
- Any file not on the safe-to-load list and not clearly a Markdown documentation file.

When in doubt, do not load the file. Record the question in `QUESTIONS.md`.

---

## 5. Session opening protocol

Open every AI session with:

1. Declare the mode: `You are operating in [Mode] for the Autonomous Duck Deployment Framework public repository.`
2. Load `AGENTS.md` (this file).
3. Load `STATE.md`.
4. Load `DOMAIN.md`.
5. Load additional context files relevant to the task.
6. State the session goal.

For sprint work, also load:
- `planning/sprints/sprint_NNN/requirements.md`
- `planning/sprints/sprint_NNN/blueprint.md`
- `planning/sprints/sprint_NNN/acceptance.md`

**Rule:** Declare the mode before the model acts.

---

## 6. Mode boundaries summary

| Mode | Can read | Can write | Cannot write |
|---|---|---|---|
| Research Mode | All safe files | Research notes, `QUESTIONS.md`, `RISKS.md` | Code, sprint plan files, decisions |
| Design Mode | All safe files | All project brain files, sprint packs, docs, prompts, examples, starter kit | Source code, website src, CLI tools |
| Develop Mode | All safe files + active sprint pack | `dry_run.md`, `implementation_log.md`, `handoff_summary.md`, approved implementation files | Files outside blueprint, project brain files |

**Rule:** Mode controls write permission. One mode per session.

---

*ADDF · `AGENTS.md` · maintained as part of the project brain*
