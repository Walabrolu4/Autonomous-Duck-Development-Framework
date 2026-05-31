# Session Checkpoint

## Purpose

End a session with durable notes so the next session can resume from files.

## When to Use

Use before stopping work, switching models, or handing work to another operator.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- Active sprint files
- Active `implementation_log.md`, if present
- Relevant changed files

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Create a session checkpoint.

Record:
1. What was completed
2. What remains
3. Files changed
4. Verification performed
5. Open questions
6. Risks
7. Exact next action
8. Files the next session must load first

Write the checkpoint to the approved handoff or sprint file.
```

## Expected Output

- Durable checkpoint summary.
- Clear next action.
- File load list for the incoming session.

## Notes

Do not rely on chat history. The checkpoint must stand alone.
