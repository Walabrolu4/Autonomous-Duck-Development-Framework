# Patch Implementation

## Purpose

Implement a small approved patch within Develop Mode boundaries.

## When to Use

Use for a tightly scoped correction after a dry run or when the active sprint explicitly authorizes a patch.

## Mode

Develop Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- Active sprint `requirements.md`, if present
- Active sprint `blueprint.md`, if present
- Active sprint `acceptance.md`, if present
- Active sprint `dry_run.md`
- Active sprint `implementation_log.md`
- The approved file or files to patch

## Prompt

```text
You are operating in Develop Mode for [PROJECT NAME].

Permission Level: [LEVEL]

Patch request:
[PATCH REQUEST]

Approved files:
[FILES]

Make only the approved patch. Do not refactor adjacent code. Do not add dependencies. Update implementation_log.md after the change. Run approved verification if available.
```

## Expected Output

- Approved patch applied.
- Updated implementation log.
- Verification result or explanation if not run.

## Notes

If the patch requires touching a file not listed as approved, stop and request updated authorization.
