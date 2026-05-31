# Implementation Review

## Purpose

Review completed implementation against the sprint pack and acceptance criteria.

## When to Use

Use this after Develop Mode reports implementation complete.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- Active sprint `requirements.md`
- Active sprint `blueprint.md`
- Active sprint `acceptance.md`
- Active sprint `dry_run.md`
- Active sprint `implementation_log.md`
- Files created or modified by the sprint

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Review the implementation against the sprint pack.

Check:
- Files created and modified match blueprint.md and dry_run.md.
- Acceptance criteria can be verified by a human.
- No out-of-scope files were changed.
- No unsafe content or protected information appears.
- implementation_log.md records the work.

Do not mark human review approved.
```

## Expected Output

- Review findings.
- Missing or risky items.
- Recommended corrections.
- Draft human review file if requested.

## Notes

Lead with issues and file references when problems are found.
