# Quick Patch

## Purpose

Plan and execute a very small approved correction.

## When to Use

Use for typo fixes, tiny documentation corrections, or narrow file updates that do not need a full sprint.

## Mode

Develop Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- File to patch
- Relevant acceptance or review note

## Prompt

```text
You are operating in Develop Mode for [PROJECT NAME].

Quick patch request:
[PATCH REQUEST]

Approved file:
[FILE]

Confirm the patch is narrow. Make only the requested change. Do not refactor. Do not add dependencies. Report the diff summary.
```

## Expected Output

- Narrow patch.
- Diff summary.
- Verification note.

## Notes

If the change touches more than one file or changes behavior, stop and recommend sprint planning.
