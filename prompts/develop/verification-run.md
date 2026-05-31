# Verification Run

## Purpose

Run approved verification commands and report results without expanding scope.

## When to Use

Use after approved implementation changes or before sprint close.

## Mode

Develop Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- Active sprint `requirements.md`
- Active sprint `blueprint.md`
- Active sprint `acceptance.md`
- Active sprint `dry_run.md`
- Active sprint `implementation_log.md`
- `COMMANDS.md`

## Prompt

```text
You are operating in Develop Mode for [PROJECT NAME].

Run only the verification commands approved in dry_run.md or listed in COMMANDS.md for this sprint.

For each command:
- State why it is being run.
- Run it.
- Report the result.
- Note failures without broadening scope.

Do not modify files unless the approved verification step explicitly requires it.
```

## Expected Output

- Command list.
- Raw or summarized results.
- Pass/fail status.
- Follow-up items for failures.

## Notes

If verification requires a new command not approved in `dry_run.md`, stop and ask for approval.
