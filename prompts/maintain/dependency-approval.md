# Dependency Approval

## Purpose

Review and record a dependency decision before implementation authorization.

## When to Use

Use when a dry run or plan proposes a new library, package, service, API, or tool.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `DECISIONS.md`
- `RISKS.md`
- Active sprint `dry_run.md`
- Research notes or tool comparison, if present

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Review dependency request:
[DEPENDENCY]

Evaluate:
1. Purpose
2. Alternatives
3. License and maintenance risk
4. Security risk
5. Impact on setup and release
6. Decision recommendation

If approved, draft a DECISIONS.md entry. Do not install anything.
```

## Expected Output

- Dependency review.
- Approve / reject / defer recommendation.
- Draft decision entry if approved.
- Risks and follow-up.

## Notes

Develop Mode cannot proceed with a new dependency until the decision is recorded and human authorization is given.
