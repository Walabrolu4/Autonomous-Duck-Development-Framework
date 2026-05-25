[Home](../index.md) → [File Reference](index.md) → PROMPT_CHANGELOG.md

# PROMPT_CHANGELOG.md

## Purpose

PROMPT_CHANGELOG.md is the version history for all prompts used with the framework. When you modify, deprecate, or add a prompt in [Prompt Catalog](../prompts.md), you record the change here. This allows future sessions to understand why a prompt changed and how to behave differently as a result.

---

## Template

```markdown
# PROMPT_CHANGELOG.md

## Prompt Version Log

### Version [NUMBER] - [YYYY-MM-DD]
**Prompt affected:** [Prompt name]
**Change type:** Added / Revised / Deprecated
**Reason:** [Why the change was made]
**Impact:** [How future sessions should behave differently]
```

---

## When to Add an Entry

Add a new entry any time you:

- Modify an existing prompt in `prompts.md` (even a small wording change that affects behavior)
- Deprecate a prompt that is no longer in use
- Add a new prompt to the catalog

The entry tells future sessions — and future you — why the prompt changed. Without this record, a modified prompt looks identical to an original one, and you lose the ability to trace behavior changes back to their cause.

## See Also

- [Prompt Catalog](../prompts.md)
