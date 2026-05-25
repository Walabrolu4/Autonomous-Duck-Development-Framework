[Home](index.md)

# Quick Reference

Three short checklists for the three most critical moments in the framework. For full detail on any item, see [Sprint Workflow](sprint-workflow.md).

---

## Before the First AI Session

- [ ] `SECURITY.md` has a safe-to-share list and a never-share list
- [ ] `DOMAIN.md` has a project overview, core entities, workflows, and out-of-scope boundaries
- [ ] `COMMANDS.md` has development, test, build, lint/type-check, deploy, and rollback commands
- [ ] `STATE.md` says exactly what step you are on
- [ ] `QUESTIONS.md` has no blocker that prevents Sprint 001 planning

---

## Before Builder Writes Code

- [ ] Sprint branch exists in git
- [ ] `requirements.md`, `blueprint.md`, and `acceptance.md` exist in the sprint folder
- [ ] Builder has completed Level 0 dry run and produced `dry_run.md`
- [ ] Architect has approved `dry_run.md` and assigned a permission level
- [ ] New dependencies (if any) have `DECISIONS.md` entries
- [ ] No secrets or PII are loaded into the Builder session

---

## Before Committing a Sprint

- [ ] `implementation_log.md` lists every file created or modified
- [ ] Test, build, and lint output is pasted verbatim into `implementation_log.md`
- [ ] `human_review.md` passes all five gates: Scope, Tests, Debt, Decisions, State
- [ ] `STATE.md` has been updated to reflect the completed sprint
- [ ] `retrospective.md` records what worked, what broke, and what should change next time
- [ ] Builder thread has been closed after the work is captured in files

## See Also

- [Sprint Workflow](sprint-workflow.md)
- [Troubleshooting](troubleshooting.md)
- [Sprint Files](file-reference/sprint-files.md)
