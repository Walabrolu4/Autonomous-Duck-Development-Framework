# Rollback Planning

## Purpose

Plan how to revert a risky change safely.

## When to Use

Use before high-risk implementation, migration, or refactor work.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `RISKS.md`
- Active sprint files
- Relevant implementation plan or dry run
- Existing `rollback_log.md`, if present

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Plan rollback for:
[CHANGE]

Produce:
1. What could fail
2. Files affected
3. Backup or checkpoint needed
4. Revert steps
5. Verification after rollback
6. Human approval needed
7. rollback_log.md entry template

Do not implement the change or rollback.
```

## Expected Output

- Rollback plan.
- Verification checklist.
- Rollback log template.
- Approval requirements.

## Notes

If rollback cannot be described clearly, the planned change is not ready for Develop Mode.
