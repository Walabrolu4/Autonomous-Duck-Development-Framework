# Dry Run Review

## Purpose

Review a Develop Mode dry run against the approved sprint pack.

## When to Use

Use this after Develop Mode produces `dry_run.md` and before the human authorizes implementation.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- Active `requirements.md`
- Active `blueprint.md`
- Active `acceptance.md`
- Active `dry_run.md`

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Review the dry run against the sprint pack.

Check:
1. Every file in dry_run.md is allowed by blueprint.md.
2. Every command is necessary and safe.
3. Dependencies are declared and have decisions if needed.
4. Risks and ambiguities are explicit.
5. Acceptance criteria remain human-verifiable.

Do not authorize implementation yourself.
```

## Expected Output

- Approved, rejected, or conditional review recommendation.
- Required corrections.
- Dependency decision needs.
- Recommended permission level for the human to authorize.

## Notes

The human must send the authorization message. The model cannot self-authorize.
