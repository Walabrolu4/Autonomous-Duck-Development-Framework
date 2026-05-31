# Incoming Model Resumption

## Purpose

Resume work as a new model using only project files.

## When to Use

Use when a different model or fresh session takes over active work.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `DOMAIN.md`
- `STATE.md`
- `DECISIONS.md`
- `QUESTIONS.md`
- `RISKS.md`
- `planning/backlog.md`
- Active sprint files
- Latest handoff or implementation log, if present

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Resume as an incoming model.

Use only loaded files to determine:
- Current project state
- Active mode and sprint
- Last completed step
- Approved scope
- Remaining work
- Risks and ambiguities
- Next safest action

Do not act until you summarize the state and ask for or receive the next instruction.
```

## Expected Output

- Resumption summary.
- Remaining work list.
- Next safest action.
- Warnings about any missing files.

## Notes

If project files conflict, report the conflict instead of guessing.
