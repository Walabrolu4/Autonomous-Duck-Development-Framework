# Consistency Audit

## Purpose

Audit project files for consistency after generation or major updates.

## When to Use

Use before sprint close or release close, especially after many Markdown files are generated.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `DOMAIN.md`
- `STATE.md`
- Files generated or modified in the sprint
- Relevant docs, release files, and sprint files

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Run a consistency audit over the loaded files.

Check:
- Mode names
- Terminology
- File paths
- Required sections
- Version references
- Scope boundaries
- Security-sensitive patterns

Produce a PASS / FAIL / WARNING verdict for each checked file.
```

## Expected Output

- Audit summary.
- Per-file verdict table.
- Specific fixes for each FAIL.
- No implementation changes unless separately requested.

## Notes

Intentional safety examples such as `secrets/` should be marked as intentional when they appear in security templates.
