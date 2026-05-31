# Risk Discovery

## Purpose

Surface project risks before they become implementation problems.

## When to Use

Use this before sprint planning, before adopting dependencies, or after a major scope change.

## Mode

Research Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `RISKS.md`
- `SECURITY.md`
- Relevant sprint or release files

## Prompt

```text
You are operating in Research Mode for [PROJECT NAME].

Review the loaded context and identify risks in these categories:
1. Scope
2. Security
3. Terminology drift
4. Implementation complexity
5. Dependency or tooling risk
6. Handoff and resumption risk

Do not modify implementation files. Do not make decisions.
```

## Expected Output

- Risk list with severity and probability.
- Mitigation ideas.
- Suggested updates for `RISKS.md`.
- Open questions that need follow-up.

## Notes

Flag any risk involving protected information or unsafe file loading immediately.
