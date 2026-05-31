# Research Brief

## Purpose

Start a bounded Research Mode session and produce findings without making final project decisions.

## When to Use

Use this when the project has an unknown that must be investigated before Design Mode writes durable plans.

## Mode

Research Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `QUESTIONS.md`
- Relevant `research/` notes, if any

## Prompt

```text
You are operating in Research Mode for [PROJECT NAME].

Research question:
[QUESTION]

Context:
[CONTEXT]

Constraints:
[CONSTRAINTS]

Read the loaded files before answering. Do not write source code. Do not record decisions. Do not produce final specifications.

Produce a research brief with:
1. Summary
2. Findings
3. Options
4. Tradeoffs
5. Risks
6. Open questions
7. Recommended next step for Design Mode
```

## Expected Output

- A concise research brief.
- New unknowns suitable for `QUESTIONS.md`.
- New risks suitable for `RISKS.md`.
- A recommended next step, not a final decision.

## Notes

Use citations or source references when external material is used.
