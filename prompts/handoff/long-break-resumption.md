# Long-Break Resumption

## Purpose

Resume after a long break by reconstructing broader project context.

## When to Use

Use when days, weeks, or major project changes have passed since the last ADDF session.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `DOMAIN.md`
- `STATE.md`
- `DECISIONS.md`
- `QUESTIONS.md`
- `RISKS.md`
- `CHANGELOG.md`
- `VERSION.md`
- `planning/backlog.md`
- Active release and sprint files

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Resume after a long break.

Reconstruct:
1. Project purpose
2. Current release
3. Completed sprints
4. Active sprint or next sprint
5. Open decisions and questions
6. Current risks
7. Stale or possibly outdated files
8. Recommended restart sequence

Do not write source code.
```

## Expected Output

- Long-break resumption summary.
- Restart checklist.
- Stale-file warnings.
- Recommended next Design Mode or Develop Mode action.

## Notes

Prefer a conservative restart path when state is stale.
