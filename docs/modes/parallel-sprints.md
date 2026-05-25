[Home](../index.md) → [Operating Modes](index.md) → Parallel Sprints

# Parallel Sprints

## Use For

Two or more feature sprints running simultaneously, where the features are completely independent and share no files.

---

## Conditions Required

All three conditions must be confirmed before running parallel sprints:

1. **Zero overlapping files in blueprints** — each sprint's `blueprint.md` must list completely different files. If Sprint A touches `src/TaskForm.tsx`, Sprint B may not.
2. **Each sprint has its own branch, sprint folder, and Builder session** — they must be completely isolated from each other.
3. **The [Architect Sanity Audit](../prompts.md#sanity-audit) confirms zero file overlap** — run this audit with both blueprints loaded before authorizing either Builder session.

---

## Warning

> **A single overlapping file in two blueprints can cause a merge conflict that invalidates both sprints. Use conservatively.**

Parallel sprints compound the risk of conflict. The overlap does not need to be large — a shared utility file, a shared config, or a shared type definition is enough to create a conflict that requires both sprints to be partially reverted and rerun.

When in doubt, run sprints sequentially. Parallel sprints save time only when the independence conditions are genuinely met and audited.

## See Also

- [Architect Sanity Audit prompt](../prompts.md#sanity-audit)
- [Mode 2: Feature Sprint](feature-sprint.md)
- [Sprint Workflow](../sprint-workflow.md)
