[Home](../index.md) → [File Reference](index.md) → Planning Files

# Planning Files

## backlog.md

**Purpose:** The running list of features, bugs, and tech debt items that are known but not scheduled for the current sprint. Items are added during retrospectives, mid-sprint discoveries, and the Cross-Sprint Consistency Audit. The Architect consults the backlog when generating sprint packs to ensure nothing important is forgotten.

```markdown
# Backlog

## Backlog Item 001: [Short title]
**Date added:** [YYYY-MM-DD]
**Type:** Feature / Bug / Refactor / Tech Debt
**Priority:** High / Medium / Low / Unprioritized
**Status:** Unprioritized / Accepted / Scheduled for Sprint [NNN] / Rejected

### Description
[What is this item and why it matters]
```

Items are added to the backlog whenever:

- A retrospective identifies a known issue that falls outside the current sprint scope
- The dry run or Sanity Audit reveals scope that is too large for the current sprint
- The Cross-Sprint Consistency Audit identifies drift that needs a dedicated sprint to address

---

## FILE_INVENTORY.md

**Purpose:** A manifest of the source asset files that exist in the project, including their purpose and the data shapes they work with. Useful for data ingestion sessions (Mode 4) and for auditing what the codebase contains.

```markdown
# FILE_INVENTORY.md Source Asset Manifest

## Source Files
| File Path           | Purpose                        | Key Data Shapes          |
|---------------------|-------------------------------|--------------------------|
| src/[path]          | [What this file does]          | [Input/output types]     |

## Last Updated
[YYYY-MM-DD] — Sprint [NNN]
```

Update FILE_INVENTORY.md after any sprint that creates or significantly modifies source files. The Architect uses it during Mode 4 data ingestion sessions to understand the existing data landscape before mapping new sources.

## See Also

- [Step 6: Reflection Loop](../lifecycle/06-reflection-loop.md)
- [File Reference Overview](index.md)
