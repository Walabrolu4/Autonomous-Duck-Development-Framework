# Release Plan — v0.1 Public Proof

**Release:** v0.1.0  
**Name:** Public Proof  
**Target:** First public release  
**Status:** In progress  
**Primary reference:** `todos/ADDF_Project_Requirements_v2_1.md` §21, §23

---

## Release goal

> A competent operator can understand ADDF, download the starter kit, and run the first session manually.

This release does not require a website, CLI tool, or onboarding app. It requires that the documentation, starter kit, prompt catalog, example project, and handoff protocol exist in a form an operator can use without further assistance.

---

## Success criteria

The v0.1.0 release is acceptable when all of the following are true:

- [ ] A new operator can understand ADDF from `README.md` and `START_HERE.md` alone.
- [ ] A new operator can download the starter kit as a ZIP.
- [ ] A new operator can follow `START_HERE.md` and reach the end of their first sprint.
- [ ] A new operator can create `DOMAIN.md`, `STATE.md`, and a sprint folder from the blank starter kit.
- [ ] The repository contains full framework documentation (`docs/full-manual.md`).
- [ ] The repository contains a copy-ready prompt catalog in `prompts/`.
- [ ] The repository contains a complete example project in `examples/mini-task-tracker/`.
- [ ] The repository documents Research Mode, Design Mode, and Develop Mode.
- [ ] The repository explains `Project → Release → Feature → Sprint → Patch`.
- [ ] The repository explains the 8-step lifecycle.
- [ ] The repository explains the handoff and resumption protocol.
- [ ] The repository contains the 15 core framework diagrams.
- [ ] The starter kit has a version number.
- [ ] The prompt catalog has a version number.
- [ ] A `LICENSE` file exists.
- [ ] A `CHANGELOG.md` is current.
- [ ] No secrets, tokens, API keys, or private infrastructure paths are committed.
- [ ] The repository uses ADDF internally (dogfooding requirement, §20).

---

## Scope

See `planning/releases/v0.1/scope.md` for the complete in-scope and out-of-scope lists.

---

## Sprint breakdown

| Sprint | Title | Status | Sprint pack |
|---|---|---|---|
| 001 | Repository skeleton and project brain | `ACTIVE` | `planning/sprints/sprint_001/` |
| 002 | Starter kit | `PLANNED` | Not yet written |
| 003 | Prompt catalog | `PLANNED` | Not yet written |
| 007 | Example project — Mini Task Tracker | `PLANNED` | Not yet written |
| 008 | Handoff and resumption package | `PLANNED` | Not yet written |
| 009 | Release package | `PLANNED` | Not yet written |

Note: Sprints 004, 005, 006 are website work scheduled for v0.2. Sprints 010, 011 are CLI and onboarding app work scheduled for v0.3 and v0.4. See `planning/backlog.md`.

---

## Unscheduled v0.1 work

These items are in scope for v0.1 but not yet assigned to a sprint:

| Item | Blocker | Target sprint |
|---|---|---|
| `docs/full-manual.md` — full manual Markdown | Consolidates existing docs/ seed files | Sprint 003 or new sprint |
| Full manual PDF | Depends on full-manual.md | Sprint 009 |
| 15 core framework diagrams (`assets/diagrams/`) | Requires visual asset production | TBD |
| `assets/logo/` final files | SVG readiness confirmation | TBD |
| `assets/lifecycle/` | Part of diagrams work | TBD |
| `LICENSE` | Q001 (license decision) must be resolved | Sprint 001 close or Sprint 002 |
| `CONTRIBUTING.md` | None | Sprint 002 or Sprint 009 |
| `CODE_OF_CONDUCT.md` | None | Sprint 002 or Sprint 009 |

---

## Dependencies and blockers

| Item | Depends on | Status |
|---|---|---|
| `LICENSE` | Q001 — license decision | `OPEN` |
| CLI package name | Q002 — npm name availability | `OPEN` (v0.3) |
| Onboarding app | Q006 — confirm v0.4 target | `OPEN` |
| Diagrams | Visual asset production capacity | `OPEN` |
| Full manual PDF | Full manual Markdown complete | `BLOCKED` by Markdown |

---

## Risks

See `RISKS.md` for the current risk register.

Risks most relevant to v0.1:
- Risk 001: Terminology drift
- Risk 003: Scope creep from v0.2+ features
- Risk 004: Secrets committed to public repository
- Risk 008: Handoff protocol not tested before release
- Risk 009: Version misalignment between artifacts

---

## Release process

When all sprint acceptance criteria pass:

1. Run the consistency audit prompt across all documentation.
2. Verify all artifact versions are updated in `VERSION.md`.
3. Write `planning/releases/v0.1/release_notes.md`.
4. Update `CHANGELOG.md`.
5. Merge `release/v0.1.0` branch to `main`.
6. Tag: `git tag -a v0.1.0 -m "v0.1.0 Public Proof"`.
7. Create GitHub release with release notes.
8. Attach release package assets.
9. Write `planning/releases/v0.1/retrospective.md`.
10. Update `STATE.md` to begin v0.2 planning.

---

*ADDF · `planning/releases/v0.1/release_plan.md` · maintained by Design Mode*
