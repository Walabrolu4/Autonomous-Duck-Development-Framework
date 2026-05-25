[Home](../index.md) → [Lifecycle](index.md) → Step 5: Full-Scale Development

# Step 5: Full-Scale Development

## Goal

Execute the complete product build through back-to-back Feature Sprints.

---

## Why This Phase Matters

At scale, improvisation bias compounds. A Builder that invents one database key in Sprint 3 may reference it in Sprint 7, Sprint 12, and Sprint 18. The [Cross-Sprint Consistency Audit](../prompts.md#consistency-audit) exists specifically to catch this drift before it becomes irreversible.

---

## The Action

Execute [Mode 2 Feature Sprints](../modes/feature-sprint.md) in sequence. Close the Builder chat completely between every sprint. Every third sprint, run the Cross-Sprint Consistency Audit to check that the codebase still matches what DOMAIN.md says.

---

## The Rule

Each new Builder session begins by loading only the freshly updated STATE.md and the current sprint folder. The context reset between sprints is non-negotiable.

---

## Why Close the Builder Chat Between Sprints

A long Builder chat accumulates context bleed. Old sprint decisions, abandoned approaches, and previous implementation details fill the context window and start influencing the next sprint. Starting fresh means the Builder reads only what you intentionally loaded — no carryover noise.

The next sprint should behave as if it is the first sprint, because it reads only current files — not conversation history.

## See Also

- [Mode 2: Feature Sprint](../modes/feature-sprint.md)
- [Cross-Sprint Consistency Audit prompt](../prompts.md#consistency-audit)
- [Sprint Workflow](../sprint-workflow.md)
