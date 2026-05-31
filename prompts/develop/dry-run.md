# Dry Run

## Purpose

Start Develop Mode at Permission Level 0 and produce `dry_run.md` only.

## When to Use

Use before any implementation, source change, prompt catalog generation, or approved file modification.

## Mode

Develop Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `COMMANDS.md`
- Active sprint `requirements.md`
- Active sprint `blueprint.md`
- Active sprint `acceptance.md`

## Prompt

```text
You are operating in Develop Mode for [PROJECT NAME].

Permission Level: 0 - Dry Run Only.

Read:
- AGENTS.md
- STATE.md
- COMMANDS.md
- requirements.md
- blueprint.md
- acceptance.md

Produce dry_run.md with exactly these seven sections:
1. Files to create
2. Files to modify
3. Files to move or delete
4. Commands to run
5. Dependencies requested
6. Risks
7. Ambiguities

Do not create, modify, move, or delete any implementation file.
Stop after writing dry_run.md.
Await human authorization.
```

## Expected Output

- `dry_run.md`.
- No implementation changes.
- Clear risks and ambiguities.

## Notes

The model cannot self-authorize. Human authorization is required before Permission Level 1 or higher work begins.
