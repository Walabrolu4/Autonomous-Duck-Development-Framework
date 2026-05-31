# Sprint Pack Generation

## Purpose

Generate `requirements.md`, `blueprint.md`, and `acceptance.md` for a sprint.

## When to Use

Use this before any Develop Mode dry run or implementation work.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `DECISIONS.md`
- `QUESTIONS.md`
- `RISKS.md`
- `planning/backlog.md`
- Relevant release or feature files

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Generate the sprint pack for:
Sprint [NUMBER] - [TITLE]

Create:
- planning/sprints/sprint_[NUMBER]/requirements.md
- planning/sprints/sprint_[NUMBER]/blueprint.md
- planning/sprints/sprint_[NUMBER]/acceptance.md

The blueprint must list exact files to create or modify. Acceptance criteria must be human-verifiable.

Do not write source code.
```

## Expected Output

- Sprint requirements.
- Blueprint with exact file paths.
- Acceptance criteria.
- Updated `STATE.md` and `planning/backlog.md` if the sprint opens.

## Notes

For prompt catalog work, the blueprint must list each prompt file by exact path.
