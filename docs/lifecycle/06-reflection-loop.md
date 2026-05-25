[Home](../index.md) → [Lifecycle](index.md) → Step 6: The Reflection Loop

# Step 6: The Reflection Loop

## Goal

Turn one-time errors into permanent constraints, keep the context window clean, and maintain the backlog.

---

## Why This Phase Matters

AI coding tools repeat mistakes unless explicitly told not to. A Builder that created an empty-title task in Sprint 2 will create another in Sprint 8 unless a constraint in `AGENTS.md` prevents it. The retrospective converts experience into guardrails.

Without a reflection loop, the same mistakes recur. With it, every sprint that encounters a failure makes the next sprint safer.

---

## The Action

After every sprint:

1. The Architect reviews the `implementation_log.md` for issues
2. The human fills in the `retrospective.md` template — what went well, what broke, and what should change
3. Any new constraint discovered is added to `AGENTS.md` immediately
4. `planning/backlog.md` is triaged — items that grew out of scope get added, and existing items are re-prioritized
5. The Builder thread is closed completely

For example: after Sprint 002 of the Mini Task Tracker, the Builder created a task with an empty title via keyboard shortcut — a gap the acceptance criteria had not covered. The constraint added to AGENTS.md was:

```
## Additional Builder Constraints (added Sprint 002 retrospective)
- Always validate non-empty, non-whitespace title before task creation,
  regardless of how form submission was triggered.
```

Every future Builder session reads this. The lesson is permanent.

## See Also

- [retrospective.md](../file-reference/sprint-files.md#retrospectivemd)
- [AGENTS.md](../file-reference/agents.md)
- [Planning Files](../file-reference/planning-files.md)
