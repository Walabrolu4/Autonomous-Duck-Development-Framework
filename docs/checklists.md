# Operational Checklists

Four gate checklists — each is an execution gate, not a suggestion.

## Table of contents

1. [Before first AI session](#before-first-ai-session)
2. [Before Develop Mode](#before-develop-mode)
3. [Before authorizing development](#before-authorizing-development)
4. [Before commit](#before-commit)

---

## Before first AI session

Run this checklist before opening any AI session on a new project. A session that opens before `SECURITY.md` exists has no defined boundary.

- [ ] `SECURITY.md` exists.
- [ ] Never-share items are defined.
- [ ] Work scale is identified.
- [ ] Project goal is written.
- [ ] Research Mode is used if meaningful unknowns exist.
- [ ] Design Mode is used before Develop Mode.

**Rule:** Fill `SECURITY.md` before loading files into an AI session.

---

## Before Develop Mode

Run this checklist before opening a Develop Mode session. The Sprint Pack must be complete before the model sees it.

- [ ] Sprint Pack exists (`requirements.md`, `blueprint.md`, `acceptance.md`).
- [ ] `requirements.md` is clear — the sprint goal and scope are specific.
- [ ] `blueprint.md` lists exact files to create or modify.
- [ ] `acceptance.md` criteria are checkable — each can be verified with a command or observable output.
- [ ] Branch is created.
- [ ] Permission Level 0 is declared.
- [ ] Develop Mode is instructed to dry run and stop.

**Rule:** The Sprint Pack is the contract for Develop Mode.

---

## Before authorizing development

Run this checklist after reviewing `dry_run.md` and before sending the authorization message.

- [ ] `dry_run.md` matches `blueprint.md` — no unapproved files are listed.
- [ ] Design Mode review passed.
- [ ] Any new dependencies are approved and have a `DECISIONS.md` entry.
- [ ] Risks are acceptable.
- [ ] Rollback plan exists if the permission level or change scope warrants it.
- [ ] Permission level is explicit in the authorization message.

**Rule:** Develop Mode does not self-authorize.

---

## Before commit

Run this checklist after implementation and before committing to the branch.

- [ ] `implementation_log.md` is complete — every change is documented.
- [ ] Verification output is pasted into `implementation_log.md`.
- [ ] `human_review.md` passed.
- [ ] `DECISIONS.md` is updated with any new architecture or dependency decisions.
- [ ] `planning/backlog.md` is updated.
- [ ] `STATE.md` is updated.
- [ ] `retrospective.md` is completed.
- [ ] Handoff notes exist if pausing.

**Rule:** A checklist is an execution gate, not a suggestion.

---

[← Wiki Home](index.md) · ADDF v3.5
