# Refactor Planning

## Purpose

Plan a supervised refactor before implementation.

## When to Use

Use when structure needs improvement but behavior should remain unchanged.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `DECISIONS.md`
- Relevant docs and files proposed for refactor

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Plan a refactor:
[REFACTOR GOAL]

Produce:
1. Current structure
2. Proposed structure
3. Files affected
4. Behavior that must not change
5. Risks
6. Verification plan
7. Recommended permission level

Do not implement.
```

## Expected Output

- Refactor plan.
- File list.
- Risk and rollback notes.
- Verification plan.

## Notes

Refactors that touch adjacent files require explicit authorization before Develop Mode work.
