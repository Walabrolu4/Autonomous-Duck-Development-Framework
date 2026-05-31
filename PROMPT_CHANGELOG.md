# PROMPT_CHANGELOG.md

**The Autonomous Duck Deployment Framework - prompt catalog version history.**

Record every change to a prompt here: additions, modifications, deprecations, and removals. Operators who copied prompts from an earlier version need to know when to update them.

---

## v0.1.0 - 2026-05-31

### Added

**Research prompts:**
- `prompts/research/research-brief.md` - Initial Research Mode prompt for bounded research briefs.
- `prompts/research/source-summary.md` - Initial Research Mode prompt for source summaries.
- `prompts/research/tool-comparison.md` - Initial Research Mode prompt for tool and approach comparison.
- `prompts/research/open-questions.md` - Initial Research Mode prompt for open question discovery.
- `prompts/research/risk-discovery.md` - Initial Research Mode prompt for risk discovery.

**Design prompts:**
- `prompts/design/project-initialization.md` - Initial Design Mode prompt for project brain creation.
- `prompts/design/release-planning.md` - Initial Design Mode prompt for release planning.
- `prompts/design/feature-cycle.md` - Initial Design Mode prompt for feature cycle planning.
- `prompts/design/sprint-pack-generation.md` - Initial Design Mode prompt for sprint pack generation.
- `prompts/design/dry-run-review.md` - Initial Design Mode prompt for dry run review.
- `prompts/design/implementation-review.md` - Initial Design Mode prompt for implementation review.
- `prompts/design/consistency-audit.md` - Initial Design Mode prompt for consistency audits.
- `prompts/design/documentation-drift-audit.md` - Initial Design Mode prompt for documentation drift audits.
- `prompts/design/resumption.md` - Initial Design Mode prompt for resumption from project files.

**Develop prompts:**
- `prompts/develop/dry-run.md` - Initial Develop Mode prompt for Permission Level 0 dry runs.
- `prompts/develop/authorization.md` - Initial Develop Mode authorization prompt with exact approval message.
- `prompts/develop/verification-run.md` - Initial Develop Mode prompt for approved verification runs.
- `prompts/develop/implementation-log-update.md` - Initial Develop Mode prompt for implementation log updates.
- `prompts/develop/patch-implementation.md` - Initial Develop Mode prompt for approved patch implementation.

**Handoff prompts:**
- `prompts/handoff/session-checkpoint.md` - Initial handoff prompt for session checkpoints.
- `prompts/handoff/incoming-model-resumption.md` - Initial handoff prompt for incoming model resumption.
- `prompts/handoff/long-break-resumption.md` - Initial handoff prompt for long-break resumption.

**Maintenance prompts:**
- `prompts/maintain/quick-patch.md` - Initial maintenance prompt for quick patches.
- `prompts/maintain/refactor-planning.md` - Initial maintenance prompt for refactor planning.
- `prompts/maintain/migration-planning.md` - Initial maintenance prompt for migration planning.
- `prompts/maintain/dependency-approval.md` - Initial maintenance prompt for dependency approval.
- `prompts/maintain/rollback-planning.md` - Initial maintenance prompt for rollback planning.

---

## Changelog Conventions

Each entry follows this format:

```md
## vN.N.N - [Date]

### Added
- `prompts/[group]/[name].md` - [Why it was added]

### Modified
- `prompts/[group]/[name].md` - [What changed and why]

### Deprecated
- `prompts/[group]/[name].md` - [Why deprecated, what replaces it]

### Removed
- `prompts/[group]/[name].md` - [Why removed]
```

## Notes on Breaking Changes

A prompt change is a breaking change if:

- The mode declaration changes.
- The required file load list changes.
- The authorization gate behavior changes.
- The expected output format changes substantially.

Breaking changes must be noted explicitly so operators know to update copied prompts.

---

ADDF - `PROMPT_CHANGELOG.md` - maintained as part of the project brain
