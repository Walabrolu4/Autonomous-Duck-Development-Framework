# Failure Handling & Troubleshooting

Failure recovery begins by writing state — not by asking the model to try again.

## Table of contents

1. [Develop Mode touched unapproved files](#develop-mode-touched-unapproved-files)
2. [The model invented business logic](#the-model-invented-business-logic)
3. [Project state is confused](#project-state-is-confused)
4. [Model runs out of context](#model-runs-out-of-context)

---

## Develop Mode touched unapproved files

Develop Mode modified a file that was not listed in `blueprint.md` or `dry_run.md`.

**Stop implementation immediately.**

Actions:

1. Record the issue in `implementation_log.md` — what file was touched, what changed.
2. Compare the full change set against `dry_run.md` to identify every unauthorized modification.
3. Revert unapproved changes using git.
4. Update `RISKS.md` with the scope-creep pattern observed.
5. Add a constraint to `AGENTS.md` — for example: "Develop Mode must not modify any file not listed in `blueprint.md`."

**Rule:** Failure recovery begins by writing state, not by asking for another fix.

---

## The model invented business logic

Develop Mode created behavior — a validation rule, a permission check, a data transformation — that was not specified in `DOMAIN.md`, `requirements.md`, or `blueprint.md`.

Actions:

1. Identify the invented logic — find the specific lines or functions where it appears.
2. Check `DOMAIN.md` — is this logic described anywhere? If not, it has no authority.
3. Remove the logic or mark it explicitly for human review.
4. Update `DOMAIN.md` only if a human decides the invented logic is correct and should be adopted.
5. Record the incident in `retrospective.md`.
6. Add a Develop Mode constraint to `AGENTS.md` naming the specific pattern that caused the invention.

**Rule:** Develop Mode does not invent business rules.

---

## Project state is confused

`STATE.md` is stale, `DECISIONS.md` contradicts `blueprint.md`, or a new session cannot determine what is current.

Use Design Mode for a consistency audit.

Load into the Design Mode session:

```
DOMAIN.md
STATE.md
DECISIONS.md
recent sprint folders
docs/architecture.md
```

Ask Design Mode to identify any inconsistencies or drift between the files — for example, a decision that contradicts the current `STATE.md`, or a sprint retrospective that records a rule change that never made it back to `AGENTS.md`.

Design Mode returns a list of recommended updates. The human approves each one before any file is changed.

**Rule:** Design Mode identifies drift. The human approves corrections.

---

## Model runs out of context

The active session is approaching its context limit, or the model shows signs of losing track of earlier instructions.

Use the Session Checkpoint Protocol.

Before ending the session, require the model to update:

```
STATE.md
implementation_log.md   — if in Develop Mode
handoff_summary.md
```

Then close the session, open a new one, and run the [Resumption Prompt](prompt-catalog.md#resumption-prompt) to orient the new session from files.

The previous chat is not required. The files are sufficient.

**Rule:** Failure recovery begins by writing state, not by asking for another fix.

---

[← Wiki Home](index.md) · ADDF v3.5
