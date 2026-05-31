# Release Planning

## Purpose

Create or update release-level planning files.

## When to Use

Use this when a project needs a release goal, scope boundary, sprint breakdown, and acceptance direction.

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

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Plan release [RELEASE].

Create or update:
- planning/releases/[RELEASE]/release_plan.md
- planning/releases/[RELEASE]/scope.md
- planning/backlog.md
- STATE.md

Do not write source code. Keep out-of-scope items explicit.
```

## Expected Output

- Release goal.
- In-scope and out-of-scope lists.
- Sprint breakdown.
- Dependencies and blockers.
- Updated backlog and state.

## Notes

If scope changes conflict with existing decisions, propose a `DECISIONS.md` update instead of silently changing direction.
