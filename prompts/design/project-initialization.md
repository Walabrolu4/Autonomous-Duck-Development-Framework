# Project Initialization

## Purpose

Create or complete the core project brain for a new ADDF-managed project.

## When to Use

Use this after initial project notes exist and before sprint planning begins.

## Mode

Design Mode

## Files to Load First

- `AGENTS.md`
- `DOMAIN.md`
- Any requirements, research notes, or project brief supplied by the operator

## Prompt

```text
You are operating in Design Mode for [PROJECT NAME].

Use the loaded files to create or complete the project brain.

Generate or update:
- DOMAIN.md
- STATE.md
- DECISIONS.md
- QUESTIONS.md
- RISKS.md
- COMMANDS.md
- STYLE_GUIDE.md
- SECURITY.md
- GIT_STRATEGY.md
- PROMPT_CHANGELOG.md

Do not write source code. Mark assumptions clearly.
```

## Expected Output

- Complete first-pass project brain files.
- Explicit assumptions.
- Open questions for unresolved items.
- No implementation changes.

## Notes

Use placeholders only where the operator truly has not supplied enough information.
