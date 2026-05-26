# File Reference

Template and purpose for every project brain file.

## Table of contents

1. [AGENTS.md](#agentsmd)
2. [STATE.md](#statemd)
3. [DOMAIN.md](#domainmd)
4. [DECISIONS.md](#decisionsmd)
5. [Sprint Pack — requirements.md](#sprint-pack--requirementsmd)
6. [Sprint Pack — blueprint.md](#sprint-pack--blueprintmd)
7. [Sprint Pack — acceptance.md](#sprint-pack--acceptancemd)

---

## AGENTS.md

`AGENTS.md` is the session rulebook. It is loaded first in every AI session. It defines what each mode is allowed to do and what it must never do, and establishes the Permission Level scale for Develop Mode.

```md
# AGENTS.md

## Framework
This project uses the Autonomous Duck Deployment Framework.

## Central Rule
The question is never which AI does what. The question is what files must exist
before any AI is allowed to act.

## Modes

### Research Mode
Allowed:
- Summarize sources
- Compare options
- Identify risks
- Produce research notes
- List open questions

Forbidden:
- Source code
- Final decisions
- Implementation changes

### Design Mode
Allowed:
- Create and update project brain files
- Write release plans
- Write feature briefs
- Write sprint packs
- Review dry runs
- Review implementation logs
- Write retrospectives
- Write handoff summaries

Forbidden:
- Source code
- Implementation file mutation
- Direct dependency addition

### Develop Mode
Allowed:
- Produce dry_run.md
- Modify approved files after permission
- Create tests
- Run verification commands
- Update implementation_log.md
- Produce handoff_summary.md

Forbidden:
- Skipping dry run
- Touching unapproved files
- Inventing business rules
- Adding dependencies without a decision record
- Skipping verification

## Develop Mode Permission Levels
- Level 0: Dry run only. No implementation.
- Level 1: Approved sprint scope.
- Level 2: Approved expansion.
- Level 3: Supervised refactor.
- Level 4: Migration / high-risk change.

## Session Checkpoint Rule
Before ending a session, switching models, or approaching context limits, update
STATE.md and relevant logs, then produce a handoff summary.
```

---

## STATE.md

`STATE.md` is the living status board. It reflects where the project is right now — the current goal, the active sprint, known blockers, and the next intended action. Update it at the end of every session.

```md
# STATE.md

## Current Goal
[Current objective]

## Active Scale
[Project / Release / Feature / Sprint / Patch]

## Current Mode
[Research / Design / Develop / Human Review]

## Active Release
[Version or "None"]

## Active Feature
[Feature or "None"]

## Active Sprint
[Sprint or "None"]

## Current Status
[Research / Planning / In Progress / Verification / Complete / Blocked / Paused]

## Known Blockers
[Blockers or "None"]

## Last Completed Step
[Last completed action]

## Next Intended Step
[Next action]

## Files Recently Changed
- [file]: [summary]

## Handoff Notes
[Important continuation context]
```

---

## DOMAIN.md

`DOMAIN.md` is the business logic document. It defines the project's entities, workflows, scope boundaries, and non-negotiable rules. It is the primary input for Design Mode when generating Sprint Packs.

```md
# DOMAIN.md

## Project Overview
[What this project does and why it exists.]

## Target Users
[Primary users]

## Core Entities

### [Entity Name]
Definition:
Key fields:
Business rules:
What it is NOT:

## Workflows

### [Workflow Name]
1. [Step]
2. [Step]

Edge cases:

## In Scope
- [Item]

## Out of Scope
- [Item]

## Non-Negotiable Rules
- [Rule]
```

---

## DECISIONS.md

`DECISIONS.md` is the decision log. Entries are never deleted — they are superseded by later entries. Every architecture decision, dependency addition, and significant process change gets a record here.

```md
# DECISIONS.md

Decisions are never deleted. They are superseded by later decisions.

## Decision 001: [Short Title]
**Date:** [YYYY-MM-DD]
**Status:** Accepted / Superseded / Proposed
**Type:** Architecture / Dependency / Data Model / Security / Process / Other

### Context
[Why this decision is needed]

### Decision
[Decision made]

### Tradeoffs
[Costs, limitations, risks]

### Alternatives Considered
[Options rejected or deferred]
```

---

## Sprint Pack — requirements.md

`requirements.md` defines what the sprint must accomplish. It is the first file Design Mode generates and the first file Develop Mode reads.

```md
# requirements.md

## Sprint Goal

## Functional Requirements

## Technical Requirements

## In Scope

## Out of Scope

## Constraints

## Related Decisions

## Open Questions
```

---

## Sprint Pack — blueprint.md

`blueprint.md` defines how the sprint will be implemented. It lists exact file paths to create or modify, the implementation steps, and all assumptions.

```md
# blueprint.md

## Summary

## Files to Create

## Files to Modify

## Implementation Steps

## Assumptions

## Dependencies

## Risks

## Rollback Considerations
```

---

## Sprint Pack — acceptance.md

`acceptance.md` defines what counts as done. Every criterion must be checkable — not "the feature works" but "the verification command passes and the output matches the expected result."

```md
# acceptance.md

## Functional Criteria
- [ ] [Criterion]

## Technical Criteria
- [ ] [Criterion]

## Documentation Criteria
- [ ] [Criterion]

## Verification Commands
1. [command]

## Definition of Done
- [ ] Requirements met
- [ ] Verification complete
- [ ] implementation_log.md updated
- [ ] human_review.md passed
- [ ] STATE.md updated
```

**Rule:** Templates are starting points, not decoration. Remove sections that do not apply.

---

[← Project Brain](project-brain.md) · [← Wiki Home](index.md) · ADDF v3.5
