# Sprint 001 — Requirements

**Sprint:** 001  
**Title:** Repository skeleton and project brain  
**Release:** v0.1 Public Proof  
**Mode:** Design Mode (this sprint contains no implementation files)  
**Status:** In progress  
**Primary reference:** `todos/ADDF_Project_Requirements_v2_1.md` §20, §22

---

## Sprint goal

Add the complete ADDF project brain and planning structure to the repository.

By the end of this sprint, the repository must contain all required project brain files with accurate, consistent content, and the planning structure must be in place for the v0.1 release and Sprint 001 sprint pack.

---

## Context

Before this sprint, the repository contained only seed files:

```
README.md         — basic project overview
STATE.md          — initialized with goal and active sprint
SECURITY.md       — never-load rules
docs/             — wiki seed files (getting-started, modes, sprint-loop, etc.)
todos/            — requirements document and tutorial references
```

The project brain had not been created. There were no `AGENTS.md`, no `DOMAIN.md`, no sprint planning files, and no release structure. This sprint creates everything.

---

## In scope

### Project brain files (root level) — all new

These files did not exist before this sprint. Design Mode creates them.

```
AGENTS.md               — session operating rules, mode definitions, dry run approval rule
DOMAIN.md               — project scope, entities, terminology, v0.1 boundary
DECISIONS.md            — durable decisions including Decision 001 (Dogfood ADDF)
COMMANDS.md             — run, build, test, deploy, rollback commands
QUESTIONS.md            — open questions from requirements §24
RISKS.md                — project-specific risks with mitigations
STYLE_GUIDE.md          — project brain style quick reference
GIT_STRATEGY.md         — branching, commit, PR, and release process
PROMPT_CHANGELOG.md     — prompt catalog version history
START_HERE.md           — first-session guide (15 steps)
VERSION.md              — artifact version registry
CHANGELOG.md            — project changelog
```

### Pre-existing documentation file — correction only

```
docs/_PDF/style Guide/STYLE_GUIDE.md   — terminology corrections per Decision 002
                                          Sections updated: 2.4, 11.1, 11.3, 12.1, 20
```

### Planning structure — all new

```
planning/backlog.md
planning/releases/v0.1/release_plan.md
planning/releases/v0.1/scope.md
planning/releases/v0.1/release_notes.md     — placeholder only
planning/sprints/sprint_001/requirements.md  — this file
planning/sprints/sprint_001/blueprint.md
planning/sprints/sprint_001/acceptance.md
planning/sprints/sprint_001/consistency_audit.md   — Design Mode audit artifact
```

---

## Out of scope

The following are explicitly excluded from Sprint 001:

| Excluded item | Reason |
|---|---|
| Content updates to `README.md` | Pre-existing seed. Content review is a separate sprint-closing task. |
| Updates to `STATE.md` | State is updated when the sprint closes, not during it. |
| `starter-kit/` files | Sprint 002 scope. |
| `prompts/` files | Sprint 003 scope. |
| `examples/` files | Sprint 007 scope. |
| `docs/full-manual.md` | Requires full documentation consolidation. Future sprint. |
| 15 core framework diagrams | Requires visual asset production. Future sprint. |
| `LICENSE`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md` | License decision (Q001) not yet resolved. Future sprint. |
| Any source code, website files, or CLI scripts | No Develop Mode work in this sprint. |
| `website/` directory | v0.2 scope. |
| `tools/` directory | v0.3 scope. |

---

## Constraints

1. **Design Mode only.** This sprint does not use Develop Mode. No implementation files are created or modified.
2. **No secrets.** No API keys, tokens, credentials, or private paths may appear in any generated file.
3. **Canonical terminology.** All generated files must use Research Mode, Design Mode, and Develop Mode as the three public operating modes. No Architect Mode or Builder Mode as primary mode names.
4. **Framework consistency.** All files must be internally consistent with each other and with the framework documentation in `docs/`.
5. **Accuracy over completeness.** A sparse, accurate file is better than a complete but incorrect one.

---

## Success criteria

See `planning/sprints/sprint_001/acceptance.md` for the human-verifiable checklist.

---

*ADDF · `planning/sprints/sprint_001/requirements.md`*
