# QUESTIONS.md

**The Autonomous Duck Deployment Framework — open questions and unknowns.**

Record every question that is blocking or could affect a decision here. When a question is resolved, mark it Resolved, record the answer, and update the relevant file (usually `DECISIONS.md` or `DOMAIN.md`).

Do not delete resolved questions. Resolved questions are part of the project record.

---

## Open questions


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

### Question 012 — Unplanned session termination

**Status:** Open  
**Type:** Decision required  
**Blocking:** AGENTS.md protocol, handoff protocol  
**Raised:** May 2026

The handoff protocol requires the active model to generate `handoff_summary.md` before the session ends. This assumes the termination is planned. Context limits are not planned — the session can die mid-task with no opportunity to produce a handoff summary.

In this case the incoming model has only `STATE.md` and `implementation_log.md` to resume from. If `implementation_log.md` is only updated at sprint close, it may not reflect what was half-done when the session ended.

**Options to consider:**

Option 1 — Periodic human-triggered checkpoints
The human prompts a mini handoff at natural break points within a sprint.
Relies on human discipline. Does not solve a true mid-sentence termination.

Option 2 — Implementation log as a live running record
The model updates `implementation_log.md` after every file it touches,
not just at sprint close. The log becomes a real-time record.
If the session dies, the incoming model reads the log and knows
the last completed action.

Option 3 — Standing instruction in AGENTS.md
Add a rule: "After completing each file or discrete task, update
`implementation_log.md` before proceeding to the next task."
No human action required. The model logs as it goes.
This is the lowest friction option.

Option 4 — Combination
Option 3 as the default behaviour, plus a human checkpoint prompt
available in the prompt catalog for use at natural break points.

**Recommended direction:** Option 3 or 4. The implementation log should
be a live document during Develop Mode, not a closing summary.
If adopted, this changes the instruction in AGENTS.md and the
description of implementation_log.md in the starter kit.

**Relevant files:** `AGENTS.md`, `docs/handoff-protocol.md`,
`prompts/handoff/`, `starter-kit/blank/planning/sprints/_template/`

---

## Resolved questions

### Question 010 — Prompt distribution format

**Status:** Resolved  
**Blocking:** Sprint 003 (Prompt Catalog)  
**Raised:** May 2026  
**Resolved:** 2026-05-31

Should prompts ship as individual files, one combined file, or both?

**Resolution:** v0.1 ships prompts as individual Markdown files under `prompts/`, with `prompts/README.md` and `docs/prompt-catalog.md` serving as catalog indexes. A downloadable prompt catalog ZIP remains release packaging work for Sprint 009. No combined prompt file is produced in Sprint 003.

---

### Question 004 — Release folders in starter kit

**Status:** Resolved  
**Blocking:** Sprint 002 (Starter Kit)  
**Raised:** May 2026  
**Resolved:** May 2026

Should the first public release include full release folders in the starter kit?

**Resolution:** Release folders (`planning/releases/`) are included in the example-filled kit only, not the blank kit. The blank kit minimizes ceremony. Release folder structure is demonstrated through the Mini Task Tracker example. See Decision 010.

---

### Question 001 — License

**Status:** Resolved  
**Blocking:** v0.1 public release  
**Raised:** May 2026  
**Resolved:** May 2026

What license will ADDF use?

**Resolution:** CC BY 4.0 for all framework content (documentation, manual, starter kit files, prompts, examples). MIT for code when it is introduced in v0.3+. Operators can use the methodology and license their own work however they choose — no copyleft. Attribution is required only when distributing ADDF files. See Decision 006 and `research/licensing.md`.

---

### Question 003 — Static website only

**Status:** Resolved  
**Blocking:** v0.2 website planning  
**Raised:** May 2026  
**Resolved:** May 2026

Should the first website be static-only? Are v0.2 and v0.4 separate or one deployment?

**Resolution:** v0.2 and v0.4 are one website. The onboarding app is a page within the main site, not a separate deployment. The site is static by default; the onboarding page adds a client-side interactive component. No server is required for either release. See Decision 009 and `research/website-stack.md`.

---

### Question 005 — DECISIONS.md in minimal ADDF

**Status:** Resolved  
**Blocking:** Sprint 002 (Starter Kit)  
**Raised:** May 2026  
**Resolved:** May 2026

Should minimal ADDF include `DECISIONS.md`, or only full ADDF?

**Resolution:** Every project regardless of scale includes both `DECISIONS.md` and `QUESTIONS.md`. No project is too small to record its open questions and durable decisions. Both files are required in the blank starter kit. See Decision 008.

---

*ADDF · `QUESTIONS.md` · maintained as part of the project brain*
