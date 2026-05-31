# Documentation Drift Audit

## Purpose

Find mismatches between documentation, project brain files, sprint outputs, and release scope.

## When to Use

Use after several sprints, before release close, or when docs may no longer match current project truth.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `DOMAIN.md`
- `STATE.md`
- `DECISIONS.md`
- `planning/backlog.md`
- Relevant `docs/`
- Relevant release and sprint files

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Audit documentation drift.

Compare docs against:
- DOMAIN.md
- DECISIONS.md
- STATE.md
- planning/backlog.md
- active release scope
- recent sprint outputs

Do not write source code.
```

## Expected Output

- Drift findings.
- Source of truth for each conflict.
- Recommended documentation updates.
- Questions where the source of truth is unclear.

## Notes

If a decision is missing, recommend a `DECISIONS.md` entry before rewriting docs.
