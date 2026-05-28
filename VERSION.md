# VERSION.md

**The Autonomous Duck Deployment Framework — artifact version registry.**

Every public artifact has a version. This file is the single source of truth for current version numbers. Update it when a release is prepared.

---

## Current versions

| Artifact | Version | Status | Last updated |
|---|---|---|---|
| Framework manual | 3.5 | Published (internal) | May 2026 |
| Starter kit | 0.1.0 | In development | — |
| Prompt catalog | 0.1.0 | In development | — |
| Example projects | 0.1.0 | In development | — |
| Diagram package | 0.1.0 | In development | — |
| Website | — | Not started | — |
| CLI init tool | — | Not started | — |
| Web onboarding app | — | Not started | — |
| Release package | — | Not started | — |

---

## Release history

| Release | Name | Date | Notes |
|---|---|---|---|
| v0.0.1 | Repository initialized | May 2026 | Seed files and project brain. |

---

## Versioning scheme

This project uses semantic versioning: `vMAJOR.MINOR.PATCH`.

| Component | Increments when |
|---|---|
| MAJOR | Framework concepts change in a backward-incompatible way. |
| MINOR | New artifacts, new prompts, new examples added. |
| PATCH | Corrections, clarifications, typos fixed. |

The first public release is `v0.1.0`. The framework reaches `v1.0.0` when the core documentation, starter kit, prompt catalog, and example project are all stable and the methodology has been validated by at least one external project.

---

## Framework manual versioning

The framework manual is versioned separately from the repository release.

| Manual version | What changed |
|---|---|
| 3.5 | Three public modes (Research, Design, Develop). Work scale model. 8-step lifecycle. Current canonical version. |
| 3.0 | Introduced Architect/Builder internal model (not public terminology). |

---

## Artifact compatibility

Artifacts are compatible when their major versions match. A starter kit at `0.1.x` is compatible with a prompt catalog at `0.1.x`. A major version bump in one artifact may require updates in others.

When a new version of a dependent artifact is released, this file must be updated.

---

*ADDF · `VERSION.md` · maintained as part of the project brain*
