[Home](../index.md) → [File Reference](index.md) → DECISIONS.md

# DECISIONS.md

## Purpose

DECISIONS.md is the immutable architecture decision ledger. Every significant technical choice — a new dependency, a schema change, an auth decision, a scope boundary — gets a permanent record here in ADR (Architecture Decision Record) format. Future AI sessions read these records to understand why the codebase looks the way it does. Without DECISIONS.md, a future Architect has no way to know whether a pattern in the codebase was intentional or accidental.

---

## The Immutability Rule

Decisions are never deleted from DECISIONS.md — only superseded by new entries. If you change an earlier decision, you add a new entry with status "Superseded by Decision NNN" and explain what changed and why.

This matters for future AI sessions. If a sprint three months from now proposes cloud sync, the Architect will find the original localStorage decision and understand the reasoning that led to it. Without that record, the Architect has to guess — and it may guess wrong.

---

## Template (ADR Format)

```markdown
# DECISIONS.md Architecture Decision Ledger
Decisions are never deleted - only superseded by new entries.

## Decision 001: [Short title]
**Date:** [YYYY-MM-DD]
**Status:** [Accepted / Superseded by Decision NUMBER]
**Type:** Architecture / Dependency / Data Model / Security / Other

### Context
[What situation forced this decision?]

### Decision
[What was decided?]

### Tradeoffs
[What this costs or complicates]
```

---

## Completed Example

After Sprint 001 of the Mini Task Tracker, this entry was added to DECISIONS.md:

```markdown
## Decision 001: localStorage for persistence
Date: 2026-01-15
Status: Accepted
Type: Data Model
Context: The app needs to persist tasks across browser refreshes without a backend.
Decision: Use browser localStorage for version 1.
Tradeoffs: localStorage is limited to approximately 5MB and is not synced across
devices. This is acceptable because the app is explicitly single-device
(see DOMAIN.md Out of Scope). Cloud sync is deferred to a future version.
```

This entry is permanent. If a future sprint proposes cloud sync, the Architect finds this record and understands the original reasoning.

---

## When a New Entry Is Required

Add a new DECISIONS.md entry before the next sprint begins whenever any of the following occur:

- A new third-party dependency is introduced
- A database schema or data model changes
- An auth system or permission rule changes
- The scope boundary in DOMAIN.md changes

The [Dependency Approval Gate](../sprint-workflow.md#step-5--dependency-approval-gate) (Sprint Workflow Step 5) exists specifically to catch new dependencies and create DECISIONS.md entries before the build begins.

## See Also

- [Sprint Workflow — Step 5](../sprint-workflow.md#step-5--dependency-approval-gate)
- [File Reference Overview](index.md)
