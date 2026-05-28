# RISKS.md

**The Autonomous Duck Deployment Framework — known risks and mitigations.**

Record risks that could derail the project, damage the brand, or undermine the methodology's credibility. When a risk is resolved or retired, mark it as such and record how it was addressed.

---

## Risk 001 — Terminology drift

**Severity:** High  
**Probability:** High  
**Status:** Active  
**Raised:** May 2026

### Description

The framework uses precise terminology (Research Mode, Design Mode, Develop Mode; sprint pack; dry run; permission level; Local File Sovereignty). AI sessions generating documentation, prompts, or examples may introduce synonyms, paraphrases, or older terms (Architect Mode, Builder Mode) that conflict with the canonical vocabulary.

Terminology drift across the website, docs, prompts, starter kit, and examples would confuse new operators and undermine the framework's claim to be a rigorous methodology.

### Mitigation

- `STYLE_GUIDE.md` contains the canonical vocabulary table. Load it in every Design Mode session.
- Review every generated file against the vocabulary table before committing.
- The consistency audit prompt (`prompts/design/consistency-audit.md`) must be run before any release.
- `AGENTS.md` explicitly forbids using Architect Mode or Builder Mode as mode names.

---

## Risk 002 — Documentation outpacing structure

**Severity:** Medium  
**Probability:** Medium  
**Status:** Active  
**Raised:** May 2026

### Description

The framework documentation is extensive. If documentation is written before the underlying structure (starter kit format, sprint folder layout, prompt catalog organization) is finalized, the documentation will need to be rewritten when the structure changes. This is expensive and creates inconsistency risk.

### Mitigation

- Sprint 001 (project brain) and Sprint 002 (starter kit) establish the canonical structure.
- Sprint 003 (prompt catalog) and Sprint 007 (example project) follow structure, not precede it.
- Design Mode sessions that draft documentation must confirm the structure they reference is finalized.
- Documentation that references a file path must be verified against the actual repository structure before merging.

---

## Risk 003 — Scope creep from v0.2+ features into v0.1

**Severity:** Medium  
**Probability:** High  
**Status:** Active  
**Raised:** May 2026

### Description

The full roadmap (website, CLI tool, onboarding app, expanded examples) is defined and tempting. There is a real risk that sprint work begins pulling in v0.2 or v0.3 deliverables before v0.1 is complete and stable, resulting in an incomplete first release.

### Mitigation

- `DOMAIN.md` explicitly lists what is in scope and out of scope for v0.1.
- Sprint acceptance criteria must not include items from the out-of-scope list.
- Any request to add website or CLI work to a v0.1 sprint must be challenged against the scope definition.
- The rule: ship the manual structure before shipping automation.

---

## Risk 004 — Secrets committed to a public repository

**Severity:** Critical  
**Probability:** Low  
**Status:** Active  
**Raised:** May 2026

### Description

The repository will be public. Any committed secret (API key, token, credential, private infrastructure path, personal contact detail) becomes permanently accessible.

Even files committed and immediately deleted remain in git history. A single accidental commit of a `.env` file requires a full repository history rewrite.

### Mitigation

- `SECURITY.md` defines the never-load and never-commit rules.
- `AGENTS.md` lists the never-load boundary.
- The `COMMANDS.md` validation section includes a command to grep for common secret patterns before committing.
- Add a `.gitignore` rule for all `.env` files before the first commit.
- Consider adding a pre-commit hook to detect secrets in Sprint 001.

---

## Risk 005 — AI-generated content contradicts the framework

**Severity:** High  
**Probability:** Medium  
**Status:** Active  
**Raised:** May 2026

### Description

AI sessions used to generate documentation, prompts, and example files may produce content that contradicts ADDF's own rules — for example, suggesting a model self-authorize a permission level, or generating a prompt that bypasses the dry run gate. If this content is committed and published, the framework's credibility is compromised.

This risk is especially high for AI-generated prompts, where subtle wording changes can change the authorization semantics.

### Mitigation

- Every Design Mode session must load `AGENTS.md` and `DOMAIN.md` before generating content.
- All generated prompts must be reviewed by the operator against the dry run rule and permission level sequence.
- The dry run rule is non-negotiable: Develop Mode never touches an implementation file without an approved dry run.
- Prompts that would allow a model to bypass the dry run gate must be rejected and rewritten.

---

## Risk 006 — The example project is too simple or too complex

**Severity:** Medium  
**Probability:** Medium  
**Status:** Active  
**Raised:** May 2026

### Description

Mini Task Tracker is the sole example in v0.1. If it is too trivial, operators won't understand how ADDF scales. If it is over-engineered, it becomes a barrier rather than a teaching tool.

### Mitigation

- Mini Task Tracker must show exactly Project, Release, Feature, and Sprint scale — no more.
- The example shows one completed sprint with dry run, implementation log, and retrospective.
- The example explicitly explains how Research, Design, and Develop Mode were used.
- The example shows how the project resumes from files after a break.
- Keep the app itself (a localStorage-backed task list) minimal. The example is about the ADDF file trail, not the application.

---

## Risk 007 — Brand inconsistency across output surfaces

**Severity:** Medium  
**Probability:** Medium  
**Status:** Active  
**Raised:** May 2026

### Description

The framework ships across multiple surfaces: GitHub README, Markdown docs, PDF manual, starter kit, prompt catalog, website, and slide decks. Without consistent enforcement of the style guide, each surface can drift into different voice, tone, and terminology — undermining the professional credibility of the methodology.

### Mitigation

- The `STYLE_GUIDE.md` project brain file summarizes the non-negotiable rules.
- The full brand guide (`docs/_PDF/style Guide/STYLE_GUIDE.md`) is the complete reference.
- The pre-publish checklist in the style guide must be completed before any surface is released.
- Design Mode sessions producing content must load `STYLE_GUIDE.md`.

---

## Risk 008 — Handoff protocol not tested before v0.1

**Severity:** High  
**Probability:** Medium  
**Status:** Active  
**Raised:** May 2026

### Description

The handoff protocol is a core framework claim. If it ships in v0.1 as documentation only — without being actually tested by handing work between two different models using the files — the protocol may contain gaps that are not discovered until an operator attempts to use it.

### Mitigation

- Sprint 008 (Handoff and Resumption Package) must include at least one actual handoff test: a model produces a session checkpoint, and a second model (or fresh session) resumes from it using only the files.
- The Mini Task Tracker example must show a handoff scenario.
- The handoff prompts must be validated before v0.1 release.

---

## Risk 009 — Version misalignment between artifacts

**Severity:** Medium  
**Probability:** Medium  
**Status:** Active  
**Raised:** May 2026

### Description

The project ships multiple versioned artifacts: framework manual, starter kit, prompt catalog, diagrams, and (later) website and CLI. If these fall out of sync — the starter kit references a file structure not yet in the manual, or the prompt catalog uses v3.5 terminology but the manual reflects an older version — operators get contradictory guidance.

### Mitigation

- `VERSION.md` tracks the current version of each artifact.
- Sprint 009 (Release Package) includes a version audit across all artifacts.
- Release acceptance criteria require all artifact versions to be updated together.

---

## Retired risks

*None yet.*

---

*ADDF · `RISKS.md` · maintained as part of the project brain*
