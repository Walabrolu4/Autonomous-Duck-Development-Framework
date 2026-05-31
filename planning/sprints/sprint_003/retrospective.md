# Sprint 003 - Retrospective

**Sprint:** 003  
**Title:** Prompt Catalog  
**Release:** v0.1 Public Proof  
**Date:** 2026-05-31  
**Mode at close:** Design Mode

---

## What the Sprint Produced

- `prompts/README.md` as the v0.1.0 prompt catalog index.
- 27 copy-ready prompt files:
  - 5 Research Mode prompts in `prompts/research/`.
  - 9 Design Mode prompts in `prompts/design/`.
  - 5 Develop Mode prompts in `prompts/develop/`.
  - 3 handoff and resumption prompts in `prompts/handoff/`.
  - 5 maintenance prompts in `prompts/maintain/`.
- Updated `docs/prompt-catalog.md` to point to canonical individual prompt files.
- Updated `README.md` to use current ADDF mode terminology and link to the prompt catalog.
- Updated `PROMPT_CHANGELOG.md` to record v0.1.0 prompt creation.
- Updated `starter-kit/blank/PROMPTS.md` with a pointer to the full public prompt catalog.
- Updated release and sprint tracking files.
- Created `planning/sprints/sprint_003/implementation_log.md`, `consistency_audit.md`, and `human_review.md`.

## What Worked Well

- The blueprint listed each prompt file by exact path, which made implementation direct and auditable.
- A consistent prompt file template kept all 27 prompts aligned with requirements section 11.4.
- The Develop Mode prompt set preserved the dry run and authorization gate clearly.
- The consistency audit caught the important acceptance checks: exact paths, required headings, mode names, authorization wording, maintenance folder naming, and discoverability.
- Converting `docs/prompt-catalog.md` into a catalog overview avoided maintaining duplicate full prompt text in two places.

## What Was Unclear or Needed Correction

- The requirements category name is "Maintenance Prompts," while existing project memory used the path `prompts/maintain/`. The sprint resolved this by using `prompts/maintain/` consistently and documenting it in the audit.
- `starter-kit/blank/PROMPTS.md` already contained starter prompts, so duplicating all 27 prompt files there would have created a second source of truth. The sprint added a pointer instead.
- The root `README.md` still contained older terminology and needed correction while adding prompt catalog discoverability.
- Prompt distribution format was an open question. Sprint 003 resolved it for v0.1 by shipping individual prompt files plus index/docs navigation; packaging remains Sprint 009 scope.

## Rule Change

For catalog-style sprints, the blueprint must name every generated file by exact path and the implementation must include a consistency audit that compares the generated file list against the blueprint.

Supporting rule: when a starter artifact overlaps with a full public artifact, prefer a pointer to the canonical public artifact instead of duplicating full content in both places.

## Acceptance Result

Acceptance criteria were fully met.

Human review marked all 11 acceptance sections Pass, recorded no blocking issues, and approved Sprint 003 closure. The consistency audit reports no open issues.

## Questions

No new open questions were added.

`Question 010 - Prompt distribution format` was resolved by this sprint: v0.1 ships individual prompt files with a catalog index and documentation links. A downloadable prompt catalog ZIP remains Sprint 009 release packaging work.

## Next Sprint

Sprint 004 - Website information architecture is now active. The next intended step is to create the Sprint 004 sprint pack for the v0.2 website information architecture work.

---

*ADDF - `planning/sprints/sprint_003/retrospective.md` - Design Mode - 2026-05-31*
