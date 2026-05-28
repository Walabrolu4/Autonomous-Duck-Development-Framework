# QUESTIONS.md

**The Autonomous Duck Deployment Framework — open questions and unknowns.**

Record every question that is blocking or could affect a decision here. When a question is resolved, mark it Resolved, record the answer, and update the relevant file (usually `DECISIONS.md` or `DOMAIN.md`).

Do not delete resolved questions. Resolved questions are part of the project record.

---

## Open questions

### Question 001 — License

**Status:** Open  
**Blocking:** v0.1 public release  
**Raised:** May 2026

What license will ADDF use?

The project likely needs two licenses — one for code, scripts, and tools, and one for documentation and educational materials. The current options are MIT + CC BY 4.0, Apache 2.0 + CC BY 4.0, or MIT across all content.

The decision must be recorded in `DECISIONS.md` and the `LICENSE` file must exist before the first public commit.

---

### Question 002 — CLI package name

**Status:** Open  
**Blocking:** v0.3 CLI planning  
**Raised:** May 2026

What is the final package name for the CLI init tool?

Current candidates:
- `addf` (the `addf init` command)
- `create-addf-project` (the `npx create-addf-project` form)

Both may need to be claimed on npm before the name is decided. Verify availability before committing to the name.

---

### Question 003 — Static website only

**Status:** Open  
**Blocking:** v0.2 website planning  
**Raised:** May 2026

Should the first website be static-only?

The recommended decision (Decision 003, see `DECISIONS.md`) says yes — but the web onboarding app eventually needs interactive behavior. Confirm whether the v0.2 website and the v0.4 onboarding app are separate deployments or the same deployment with a static-first phase.

---

### Question 004 — Release folders in starter kit

**Status:** Open  
**Blocking:** Sprint 002 (Starter Kit)  
**Raised:** May 2026

Should the first public release include full release folders in the starter kit?

The full ADDF starter kit spec includes `planning/releases/v0.1/` with release plan, scope, release notes, and retrospective. These add structure but also add ceremony for small projects. Decide whether these folders are included in the blank starter kit or only in the example-filled version.

---

### Question 005 — DECISIONS.md in minimal ADDF

**Status:** Open  
**Blocking:** Sprint 002 (Starter Kit)  
**Raised:** May 2026

Should minimal ADDF include `DECISIONS.md`, or only full ADDF?

The minimum viable ADDF setup listed in the requirements (`AGENTS.md`, `DOMAIN.md`, `STATE.md`, `COMMANDS.md`, `SECURITY.md`, `planning/sprints/sprint_001/`) omits `DECISIONS.md`. However, even small projects benefit from recording their first architectural decisions. Decide which tier `DECISIONS.md` belongs to and document it in the starter kit README.

---

### Question 006 — Onboarding app in v0.1

**Status:** Open  
**Blocking:** v0.1 scope confirmation  
**Raised:** May 2026

Should the first release include the onboarding app, or wait until v0.4?

The current roadmap places the onboarding app at v0.4. Confirm this is correct and that the v0.1 release does not attempt to include even a prototype of the browser-based generator.

---

### Question 007 — Visual assets for v0.1

**Status:** Open  
**Blocking:** v0.1 release package  
**Raised:** May 2026

What visual assets are required for v0.1?

The requirements list: `assets/logo/`, `assets/lifecycle/`, and `assets/diagrams/` with the 15 core framework diagrams. Confirm which diagram formats are required (SVG, PNG, or both), whether all 15 diagrams are in scope for v0.1, and whether the vector duck logo (`duck-logo.svg`) will be ready by v0.1 or if PNG assets will serve as interim.

---

### Question 008 — Planning history visibility

**Status:** Open  
**Blocking:** First public commit decision  
**Raised:** May 2026

Should the repo include complete planning history from the first public commit?

The alternative is to begin the public repository at a clean state and keep earlier planning history private. Decide whether sprint artifacts (retrospectives, implementation logs, human reviews) from the repository setup phase are published or redacted.

---

### Question 009 — CLI implementation language

**Status:** Open  
**Blocking:** v0.3 CLI planning  
**Raised:** May 2026

Should the init tool be implemented in JavaScript (Node.js), Python, or both?

A Node.js CLI has the advantage of `npx create-addf-project` as the distribution mechanism. A Python CLI requires no Node.js installation. Decide the primary implementation language before Sprint 010. A dual implementation is possible but doubles the maintenance surface.

---

### Question 010 — Prompt distribution format

**Status:** Open  
**Blocking:** Sprint 003 (Prompt Catalog)  
**Raised:** May 2026

Should prompts ship as individual files, one combined file, or both?

The individual file approach (`prompts/design/sprint-pack-generation.md`) allows operators to load exactly the prompt they need. A combined catalog file is easier to share as a download. Decide whether both formats are produced in Sprint 003 or only individual files for v0.1.

---

### Question 011 — The missing named principle: Design → Gate → Develop

**Status:** Open  
**Blocking:** Framework documentation clarity  
**Raised:** May 2026

The ADDF sprint loop (section 6.5 of the requirements) describes 11 steps. But those steps are actually one repeating rhythm applied at multiple levels:

```txt
For every unit of work at every scale:
  PLAN (Design Mode produces a plan)
  GATE (human reviews and approves or rejects)
  EXECUTE (Develop Mode acts on the approved plan)
```

This pattern appears at every scale:

```txt
Project:  Research → Validation gate → Sprint execution
Sprint:   Sprint pack → Blueprint review → Dry run → Approval → Build → Output review → Approval gate → Commit
Session:  Mode declaration → Task → Output review
```

The framework describes the steps but never names the rhythm underneath them. A student reading the 11-step sprint loop sees eleven things. A student who has been told "for every unit of work, you plan, gate, then execute" sees three things — and recognises them each time they appear.

Should this be added to the framework as a named first-class principle, alongside "The files are the project" and "The model is temporary compute"?

Candidate phrasing:

```txt
Plan before every action. Gate before every execution. Review after every output.
```

or:

```txt
For every unit of work: Design → Gate → Develop.
No model self-approves. No step skips the gate.
```

**Relevant files:** `AGENTS.md`, `docs/full-manual.md`, `docs/lifecycle.md`, the tutorial files

---

## Resolved questions

*None yet. Questions will be moved here with their resolution as the project progresses.*

---

*ADDF · `QUESTIONS.md` · maintained as part of the project brain*
