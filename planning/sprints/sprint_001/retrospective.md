# Sprint 001 — Retrospective

**Sprint:** 001  
**Title:** Repository skeleton and project brain  
**Date:** 2026-05-27  
**Mode at close:** Design Mode

---

## What this sprint was

Sprint 001 is the bootstrap sprint. It cannot be run the way every other sprint will be run, because the files it creates are the files every other sprint depends on. The sprint pack (requirements, blueprint, acceptance) was generated after the project brain, not before. The consistency audit was run between generation and closure, not as a pre-sprint gate.

This ordering is a one-time exception. Every sprint from Sprint 002 onward must begin with the sprint pack.

---

## What worked

**The consistency audit caught real errors.**

The audit identified 6 actionable issues in the generated files. The errors were not cosmetic:

- `AGENTS.md` had an incomplete dry run definition that omitted four of the seven required content items. An operator using the file as written would not know to document commands, dependencies, risks, or ambiguities in the dry run.
- `AGENTS.md` had a Research Mode write restriction that was over-broad — it prohibited research notes in sprint folders, which the documentation explicitly permits.
- `AGENTS.md`'s Develop Mode write list was missing `dry_run.md` and `handoff_summary.md` — the first two things Develop Mode actually writes.
- `DOMAIN.md` stated "all four groups" for the prompt catalog when five groups are defined in the requirements.
- `DOMAIN.md`'s out-of-scope table omitted four non-goals from requirements §4.

Without the audit, these errors would have entered the project brain and propagated into every future sprint. The audit is not ceremony — it catches the gap between what was intended and what was written.

**The full brand guide inconsistency was surfaced and fixed.**

The pre-existing brand guide at `docs/_PDF/style Guide/STYLE_GUIDE.md` still defined Architect Mode and Builder Mode as primary canonical terms. This contradicted Decision 002 and would have created terminology drift in any future content generated from that file. Fixing it in this sprint prevents the inconsistency from widening.

**The project brain files are internally consistent.**

All 12 generated files use Research Mode, Design Mode, and Develop Mode consistently. The mode definitions in `AGENTS.md`, the scope definitions in `DOMAIN.md`, and the terminology in `STYLE_GUIDE.md` agree with each other and with the framework documentation in `docs/`.

**Q011 emerged organically.**

The user added Q011 to `QUESTIONS.md` after the file was generated. The question — whether to name the Plan → Gate → Execute rhythm as a first-class framework principle — is a genuine framework-level question that surfaced from working with the files. This is the project brain functioning as intended: a file that is easy to add to, not a locked artifact.

---

## What needs attention

**The bootstrap ordering is an unsatisfying record.**

The sprint pack in this repository documents what was done, not what was planned before doing it. For Sprint 001 this is unavoidable. But the implementation log, blueprint, and acceptance criteria are honest about this — they document what happened, not a fiction that the plan preceded the work.

Future readers of this sprint's artifacts will notice the retrospective date and the blueprint date are the same. That is correct. It should not be normalized.

**The unscheduled v0.1 work remains unassigned.**

The following v0.1 items have no sprint assignment:

- `docs/full-manual.md` — full framework manual Markdown
- Full manual PDF
- 15 core framework diagrams
- `assets/logo/` final files (SVG readiness unconfirmed)
- `assets/lifecycle/` lifecycle diagram
- `LICENSE` (blocked by Q001 — license decision)
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`

These must be assigned to sprint numbers before Sprint 002 closes. The backlog notes them but they are not yet scheduled.

**Q001 (license) is still unresolved.**

The `LICENSE` file cannot be created until the license decision is made. This is listed in `QUESTIONS.md` as blocking v0.1 public release. It should be resolved before or during Sprint 002 so the file can be added to the repository before it goes public.

**Q011 is substantive and should not be deferred indefinitely.**

The question of whether "Plan → Gate → Execute" should be a named first-class principle is not a cosmetic documentation question. If it is adopted, it changes how the framework is explained in every mode description, every lifecycle document, and every onboarding artifact. It should be reviewed during Sprint 003 (Prompt Catalog) or before the full manual is finalized. If it is rejected, record the reason in `DECISIONS.md` so future contributors do not re-raise it.

---

## Constraints added this sprint

Two constraints were identified during this sprint and should be applied to all future sprints:

**Constraint 001 — Consistency audit before sprint close.**
Any Design Mode sprint that creates or modifies project brain files must include a consistency audit before the sprint is marked complete. The audit compares generated content against the framework documentation and the requirements document. Issues found during the audit must be resolved before human review.

This constraint was identified because the audit in Sprint 001 found real errors that would have propagated.

**Constraint 002 — Sprint pack first.**
Every sprint from Sprint 002 onward must begin by generating the sprint pack (requirements, blueprint, acceptance). No project brain files, planning files, or implementation files may be created before the sprint pack is written and reviewed by the human.

Sprint 001 is the sole exception. The exception is non-repeatable.

---

## Rules

**Rule:** The consistency audit is not optional for Design Mode sprints that generate project brain files. Run it before marking the sprint complete.

**Rule:** The sprint pack is the first artifact of every sprint. Sprint 001 is the one-time exception.

**Rule:** Every bootstrap exception must be named and non-repeatable. If a future sprint requires a similar exception, create a decision record.

---

## Next sprint

**Sprint 002 — Starter kit**

Before opening Sprint 002:

1. Resolve Q001 (license decision). Record it in `DECISIONS.md` and create `LICENSE`.
2. Assign unscheduled v0.1 items to sprint numbers or explicitly defer them.
3. Update `STATE.md` with Active Sprint: Sprint 002.
4. Generate the Sprint 002 sprint pack before beginning any starter kit work.

---

*ADDF · `planning/sprints/sprint_001/retrospective.md` · 2026-05-27*
