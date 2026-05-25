[Home](../index.md) → [Lifecycle](index.md) → Step 4: Documentation

# Step 4: Documentation (The Immutable Ledger)

## Goal

Keep the architectural record current as the codebase grows.

---

## Why This Phase Matters

Documentation debt is the silent killer of AI-assisted projects. If context files fall out of sync with code, the AI begins improvising again. An Architect that reads a DOMAIN.md from three sprints ago will give you a blueprint based on a project that no longer exists.

The ADDF framework treats documentation not as an afterthought but as an active part of the sprint process. Every structural sprint produces documentation updates, not just code.

---

## The Action

After every sprint that introduces a structural change, command the Architect to update `docs/data_model.md` and `docs/api.md`. Paste in the current `implementation_log.md` so the Architect can see what actually changed.

---

## The Rule

Any change to the data model, API contract, auth system, or external dependencies requires a new `DECISIONS.md` entry in ADR format before the next sprint begins.

This is not optional. A dependency added without a decision record is a dependency that future AI sessions will not understand. If you later need to audit which sprint introduced a vulnerable library, the ADR tells you why it was added and who approved it.

## See Also

- [DECISIONS.md](../file-reference/decisions.md)
- [File Reference Overview](../file-reference/index.md)
