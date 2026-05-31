# Implementation Authorization

## Purpose

Provide the exact human authorization message that permits Develop Mode to proceed after dry run approval.

## When to Use

Use only after the human has reviewed `dry_run.md` and any dry run review conditions are resolved.

## Mode

Develop Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- Active sprint `requirements.md`
- Active sprint `blueprint.md`
- Active sprint `acceptance.md`
- Active sprint `dry_run.md`
- Active sprint `dry_run_review.md`, if present

## Prompt

```text
Dry run approved.
Permission Level [LEVEL] authorized.
Proceed according to requirements.md, blueprint.md, acceptance.md, and dry_run.md.
```

After receiving this message, Develop Mode must:

1. Modify only approved files.
2. Follow the authorized permission level.
3. Avoid new dependencies unless approved.
4. Update `implementation_log.md`.
5. Run approved verification commands.
6. Stop if a new ambiguity appears.

## Expected Output

- Authorized implementation within the approved scope.
- Updated implementation log.
- Verification results.
- Handoff notes if work stops before completion.

## Notes

Only the human can send this authorization. The model cannot self-authorize or escalate permission level.
