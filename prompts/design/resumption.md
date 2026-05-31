# Resumption

## Purpose

Reconstruct project state from files after a session reset, model switch, or interruption.

## When to Use

Use at the start of a new session when the model has no reliable chat memory.

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
- Active sprint or release files if present

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Resume from project files only.

Summarize:
1. Project purpose
2. Active release, feature, sprint, or patch
3. Last completed step
4. Current blockers
5. Current risks
6. Next safest action
7. Files to load before Develop Mode

Do not infer from chat memory. Use only loaded files.
```

## Expected Output

- Resumption summary.
- Current state.
- Next action.
- File load list for the next session.

## Notes

If loaded files disagree, identify the conflict and ask for Design Mode correction.
