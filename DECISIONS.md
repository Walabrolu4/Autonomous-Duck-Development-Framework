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

## Decision 006: License — CC BY 4.0

**Status:** Accepted  
**Date:** May 2026  
**Decided by:** Project owner

### Context

The project needs a license before public release. ADDF contains methodology documentation, starter kit files, prompts, examples, and (from v0.3) code. Research (`research/licensing.md`) assessed MIT, Apache 2.0, CC BY 4.0, and MIT-0 across all content types.

### Decision

ADDF uses **Creative Commons Attribution 4.0 International (CC BY 4.0)** for all framework content: documentation, manual, starter kit files, prompts, and examples.

When code is introduced (CLI init tool in v0.3, web onboarding app in v0.4), those files are licensed under **MIT**.

### Tradeoffs

CC BY 4.0 requires attribution when distributing or adapting ADDF content — but imposes no copyleft. Operators can use the methodology and build their own projects under any license they choose. Their work does not inherit ADDF's license. Attribution is only required when distributing the ADDF files themselves.

Note: methodology usage (applying ADDF in a project without distributing ADDF files) cannot be legally governed by any license. The broader community norm of crediting the framework is cultural, not contractual.

### Consequences

- `LICENSE` must be created before v0.1 public release. It states CC BY 4.0 for framework content and MIT for code.
- `README.md` should clarify which license applies to which content type.
- Starter kit files carry CC BY 4.0. Operators who redistribute them must credit ADDF.
- Prompt catalog files carry CC BY 4.0. Same attribution requirement applies when shared.
- Code files (v0.3+) carry MIT. No special requirements beyond preserving the notice.

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

## Decision 008: QUESTIONS.md and DECISIONS.md are universal — no project is too small

**Status:** Accepted  
**Date:** May 2026  
**Decided by:** Project owner

### Context

Q005 asked whether `DECISIONS.md` belongs to minimal ADDF or only full ADDF. The minimum viable ADDF setup in the requirements omits `DECISIONS.md`, implying it is optional for small projects.

### Decision

`QUESTIONS.md` and `DECISIONS.md` are required in every ADDF project regardless of scale. There is no project size below which recording open questions and durable decisions is unnecessary.

The minimal ADDF file list is updated to include both files. The starter kit must include both in the blank template.

### Tradeoffs

This adds two files to the minimum setup. The alternative — treating decisions as optional for small projects — means small projects accumulate undocumented choices and lose the ability to explain why things are the way they are. A one-person project with five decisions written down is better positioned than a ten-person project with none.

### Consequences

- `starter-kit/blank/` must include `DECISIONS.md` and `QUESTIONS.md`.
- `START_HERE.md` must reference both files in the first-session steps.
- `DOMAIN.md` minimum viable file list must be updated to include both files.
- The starter kit README must not describe `DECISIONS.md` or `QUESTIONS.md` as optional.

---

## Decision 009: v0.2 website and v0.4 onboarding app are one deployment

**Status:** Accepted  
**Date:** May 2026  
**Decided by:** Project owner

### Context

Q003 asked whether the v0.2 static website and v0.4 onboarding app should be separate deployments or the same site. Research (`research/website-stack.md`) confirmed that the onboarding app requires no server — file generation is client-side only — so there is no technical barrier to hosting both in one deployment.

### Decision

The v0.2 website and v0.4 onboarding app are one website. The onboarding app is a page (or section) within the main site, not a separate product at a separate URL. v0.2 launches without the onboarding page. v0.4 adds it to the same site.

### Tradeoffs

A single deployment means v0.2 framework choice binds v0.4. The mitigation is to choose a framework that supports interactive islands from the start (Astro is the current leading candidate per `research/website-stack.md`) so v0.4 is additive work, not a migration.

### Consequences

- The v0.2 website sprint must choose a framework that can host interactive client-side components without a rewrite.
- The v0.4 onboarding app is planned as a page within the existing site, not a new repository or new host.
- A single domain serves both the documentation and the file generator.
- Q003 is resolved. See also Decision 003 (static website first).

---

*ADDF · `DECISIONS.md` · maintained as part of the project brain*
