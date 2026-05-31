# Implementation Log Update

## Purpose

Update `implementation_log.md` after approved Develop Mode changes.

## When to Use

Use after each file is created or modified, or when resuming an interrupted Develop Mode session.

## Mode

Develop Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- Active sprint `dry_run.md`
- Active sprint `implementation_log.md`
- Files changed in the current step

## Prompt

```text
You are operating in Develop Mode for [PROJECT NAME].

Update implementation_log.md for the approved work just completed.

Record:
- File path
- Action taken
- Why it was in scope
- Verification performed, if any
- Issues or follow-up

Do not modify files outside the approved sprint scope.
```

## Expected Output

- Updated `implementation_log.md`.
- Clear record of the file changed.
- Any verification or issue notes.

## Notes

The implementation log is the recovery trail for interrupted sessions.
