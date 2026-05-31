# v0.1 Release Plan - Mini Task Tracker

**Release goal:** A single operator can add, complete, reopen, and persist tasks in a local browser.  
**Target date:** 2026-06-07

## Success Criteria

1. [x] A task can be added with a non-empty title.
2. [x] A task can be marked complete.
3. [x] A completed task can be reopened.
4. [x] Tasks persist after browser reload.
5. [x] No backend, account, or build tool is required.

## Sprint Breakdown

| Sprint | Title | Status | Key output |
|---|---|---|---|
| Sprint 001 | Core task list | DONE | Add, complete, reopen, and persist tasks. |

## Dependencies and Blockers

| Dependency | Blocking what | Owner | Status |
|---|---|---|---|
| Browser localStorage | Persistence | Operator | Available |
| Manual browser testing | Release verification | Operator | Complete |

## Release Process

1. Create release branch - `release/v0.1`.
2. Update `VERSION.md` - set `0.1.0`.
3. Update `CHANGELOG.md` - summarize core task list.
4. Run consistency audit - check project name, dates, and scope.
5. Verify acceptance criteria - run Sprint 001 acceptance.
6. Merge to `main` - after human review.
7. Tag release - `v0.1.0`.
8. Publish release notes - use `release_notes.md`.
