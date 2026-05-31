# Migration Planning

## Purpose

Plan a high-risk migration with rollback needs.

## When to Use

Use for structural changes, schema changes, format migrations, or major dependency shifts.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `DECISIONS.md`
- `RISKS.md`
- Relevant architecture, data, or dependency files

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Plan migration:
[MIGRATION]

Produce:
1. Migration goal
2. Files and systems affected
3. Required decisions
4. Rollback plan
5. Verification plan
6. Risks
7. Recommended permission level

Do not implement.
```

## Expected Output

- Migration plan.
- Decision needs.
- Rollback plan.
- Verification plan.

## Notes

High-risk migrations usually require Permission Level 4 and explicit human approval.
