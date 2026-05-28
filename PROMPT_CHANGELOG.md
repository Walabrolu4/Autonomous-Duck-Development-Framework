# PROMPT_CHANGELOG.md

**The Autonomous Duck Deployment Framework — prompt catalog version history.**

Record every change to a prompt here: additions, modifications, deprecations, and removals. Operators who have copied prompts from an earlier version need to know when to update them.

Format each entry as: date, version, change type, affected prompt(s), and a brief description of what changed and why.

---

## v0.1.0 — Initial catalog (pending)

**Target:** Sprint 003  
**Status:** Not yet started

### Prompts to be created

The following prompts will be created in Sprint 003. This changelog entry will be completed when that sprint closes.

**Research prompts:**
- `research/research-brief.md`
- `research/source-summary.md`
- `research/tool-comparison.md`
- `research/open-questions.md`
- `research/risk-discovery.md`

**Design prompts:**
- `design/project-initialization.md`
- `design/release-planning.md`
- `design/feature-cycle.md`
- `design/sprint-pack-generation.md`
- `design/dry-run-review.md`
- `design/implementation-review.md`
- `design/consistency-audit.md`
- `design/documentation-drift-audit.md`
- `design/resumption.md`

**Develop prompts:**
- `develop/dry-run.md`
- `develop/authorization.md`
- `develop/verification-run.md`
- `develop/implementation-log-update.md`
- `develop/patch-implementation.md`

**Handoff prompts:**
- `handoff/session-checkpoint.md`
- `handoff/incoming-model-resumption.md`
- `handoff/long-break-resumption.md`

**Maintenance prompts:**
- `maintain/quick-patch.md`
- `maintain/refactor-planning.md`
- `maintain/migration-planning.md`
- `maintain/dependency-approval.md`
- `maintain/rollback-planning.md`

---

## Changelog conventions

Each entry follows this format:

```
## vN.N.N — [Date]

### Added
- `prompts/[group]/[name].md` — [Why it was added]

### Modified
- `prompts/[group]/[name].md` — [What changed and why]
  Operators who copied v[X] of this prompt should update the [section] section.

### Deprecated
- `prompts/[group]/[name].md` — [Why deprecated, what replaces it]

### Removed
- `prompts/[group]/[name].md` — [Why removed]
```

---

## Notes on breaking changes

A prompt change is a **breaking change** if:

- The mode declaration changes.
- The required file load list changes.
- The authorization gate behavior changes.
- The expected output format changes substantially.

Breaking changes must be noted explicitly so operators know to update their copied prompts.

A prompt change is **non-breaking** if:

- Wording is clarified without changing behavior.
- Examples are improved.
- Notes are added.

---

*ADDF · `PROMPT_CHANGELOG.md` · maintained as part of the project brain*
