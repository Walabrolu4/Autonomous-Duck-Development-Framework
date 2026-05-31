# Feature Cycle Planning

## Purpose

Plan a feature through research, feasibility, validation, and sprint mapping.

## When to Use

Use this when a release item is large enough to need feature-level planning before sprint work.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `DECISIONS.md`
- `QUESTIONS.md`
- `RISKS.md`
- Relevant release plan and scope files

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Plan feature:
[FEATURE NAME]

Create or update feature planning files:
- feature_brief.md
- research.md
- feasibility.md
- validation.md
- sprint_map.md

Do not write source code. Keep the feature scope bounded by the active release.
```

## Expected Output

- Feature goal.
- Operator impact.
- Feasibility options.
- Validation questions.
- Sprint map.
- Open questions and risks.

## Notes

If the feature can fit in a single sprint without feature planning, say so and recommend sprint pack generation instead.
