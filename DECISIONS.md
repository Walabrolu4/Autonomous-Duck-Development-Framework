# DECISIONS.md

**The Autonomous Duck Deployment Framework — durable architectural and strategic decisions.**

Record every decision that would be costly or confusing to reverse here. Do not record sprint-level choices or temporary preferences. When a decision is superseded, mark it as Superseded and record the new decision.

---

## Decision 001: Dogfood ADDF in the public repository

**Status:** Accepted  
**Date:** May 2026  
**Decided by:** Project owner

### Context

The public repository is both the distribution point and the reference implementation for ADDF. Operators evaluating the framework will inspect the repository itself to understand how the methodology works.

### Decision

The repository will include its own project brain, release plans, feature plans, sprint folders, reviews, retrospectives, and handoff records. Every release of ADDF will be planned and built using ADDF.

### Tradeoffs

This increases repository size but makes the methodology inspectable. An operator can open `planning/sprints/sprint_001/` and see exactly how the framework was applied to build itself.

### Consequences

- All project brain files (`AGENTS.md`, `DOMAIN.md`, `STATE.md`, `DECISIONS.md`, `COMMANDS.md`, `STYLE_GUIDE.md`, `SECURITY.md`, `QUESTIONS.md`, `RISKS.md`, `GIT_STRATEGY.md`, `PROMPT_CHANGELOG.md`) must be maintained and kept current.
- Planning history is public. This is intentional.
- Sprint retrospectives will be visible. Write them factually and without blame.

---

## Decision 002: Three public operating modes

**Status:** Accepted  
**Date:** May 2026  
**Decided by:** Project owner

### Context

Earlier internal versions of the framework used Architect Mode and Builder Mode as primary terminology. The public framework requires terminology that is clearer to new operators and does not imply specific tooling or product configurations.

### Decision

The public framework uses exactly three modes:

```
Research Mode
Design Mode
Develop Mode
```

Architect Mode and Builder Mode are not exposed as primary public modes. All public documentation, prompts, website copy, starter kit files, and example projects must use the three-mode terminology.

### Tradeoffs

This breaks continuity with internal documentation that uses Architect/Builder language. Internal STYLE_GUIDE references to Architect/Builder must be reviewed and updated before public release.

### Consequences

- `AGENTS.md` must define Research Mode, Design Mode, and Develop Mode.
- No prompt in the prompt catalog may instruct a model to "enter Architect Mode" or "enter Builder Mode."
- The style guide's vocabulary table must reflect this decision.

---

## Decision 003: Static website first

**Status:** Accepted  
**Date:** May 2026  
**Decided by:** Project owner

### Context

The v0.1 release requires documentation, a starter kit, and examples — not a dynamic web application. Backend complexity adds risk without adding v0.1 value.

### Decision

The first website (v0.2) will be a static site. No server-side rendering, no database, no API calls, no user accounts. All content is pre-built.

### Tradeoffs

This defers features that would benefit from server-side logic (prompt copy buttons backed by analytics, user project storage, dynamic download tracking). These features are not needed in v0.2.

### Consequences

- The web onboarding app (v0.4) will be a separate scoped effort.
- v0.2 website downloads serve static file assets — ZIP files in `assets/` or a release package location.
- Any framework requiring a backend is deferred to v0.4 or later.

---

## Decision 004: Starter kit before CLI init tool

**Status:** Accepted  
**Date:** May 2026  
**Decided by:** Project owner

### Context

The CLI init tool generates an ADDF starter structure. That structure must be fully defined and stable before the CLI can be built correctly.

### Decision

`starter-kit/blank/` ships in v0.1. The CLI init tool ships in v0.3. The CLI must produce output identical to the starter kit structure.

### Tradeoffs

Operators in v0.1 and v0.2 must copy the starter kit manually. This is acceptable — it forces operators to understand the file structure before automating it.

### Consequences

- Starter kit structure must be finalized and reviewed before CLI work begins.
- Any change to the starter kit structure in v0.2 must be reflected in the CLI spec.
- The CLI must be tested against the starter kit acceptance criteria, not a separate spec.

---

## Decision 005: Handoff protocol ships in v0.1

**Status:** Accepted  
**Date:** May 2026  
**Decided by:** Project owner

### Context

Model handoff — the ability to end a session with one model and resume with another using only files — is a core ADDF value proposition. If the first public release does not demonstrate this, the framework's claims are unsupported.

### Decision

`docs/handoff-protocol.md` and `prompts/handoff/` ship as part of v0.1. The handoff protocol includes session checkpoint, incoming model resumption, and long-break recovery.

### Tradeoffs

This adds scope to v0.1. The alternative — deferring handoff to v0.2 — would mean the most important differentiating feature is absent from the first release.

### Consequences

- Sprint 008 (Handoff and Resumption Package) must be included in v0.1 scope.
- Handoff prompts must be copy-ready without referencing any specific LLM.
- The Mini Task Tracker example must show a handoff scenario.

---

## Decision 006: License selection — pending

**Status:** Pending  
**Date:** May 2026  
**Target:** Resolved before v0.1 public release

### Context

The project needs a license before public release. Code and documentation may warrant different licenses.

### Options under consideration

| Option | Code | Documentation |
|---|---|---|
| A | MIT | Creative Commons Attribution 4.0 |
| B | Apache 2.0 | Creative Commons Attribution 4.0 |
| C | MIT only | MIT (apply uniformly) |

### Open question

See `QUESTIONS.md` Question 001.

### Decision

Not yet made. Record here when resolved.

---

## Decision 007: Prompt distribution — pending

**Status:** Pending  
**Date:** May 2026  
**Target:** Resolved before v0.1 public release

### Context

Prompts could ship as individual files, one combined catalog file, or both.

### Open question

See `QUESTIONS.md` Question 010.

### Decision

Not yet made. Record here when resolved.

---

*ADDF · `DECISIONS.md` · maintained as part of the project brain*
