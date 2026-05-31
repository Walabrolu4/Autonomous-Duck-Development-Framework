# Open Questions

## Purpose

Identify unknowns that should be tracked before planning or implementation continues.

## When to Use

Use this when a session uncovers ambiguity, missing requirements, scope uncertainty, or unresolved terminology.

## Mode

Research Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `QUESTIONS.md`
- Relevant sprint or release files

## Prompt

```text
You are operating in Research Mode for [PROJECT NAME].

Review the loaded context and identify open questions.

For each question, provide:
- Question
- Why it matters
- What it blocks
- Suggested owner
- Suggested next action

Do not answer by inventing facts. Do not make decisions.
```

## Expected Output

- Prioritized open questions.
- Suggested updates for `QUESTIONS.md`.
- Blocking status for each question.

## Notes

Questions should be specific enough that a future session can resolve them.
