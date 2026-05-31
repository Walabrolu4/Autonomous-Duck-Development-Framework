# Tool Comparison

## Purpose

Compare tools, libraries, services, or approaches before a decision is recorded.

## When to Use

Use this when the project might adopt a dependency, tool, workflow, or platform and needs evidence before Design Mode writes a decision.

## Mode

Research Mode

## Files to Load First

- `AGENTS.md`
- `STATE.md`
- `DOMAIN.md`
- `DECISIONS.md`
- `QUESTIONS.md`
- Relevant research notes or source summaries

## Prompt

```text
You are operating in Research Mode for [PROJECT NAME].

Compare:
[OPTION A]
[OPTION B]
[OPTION C, IF ANY]

Evaluation criteria:
[CRITERIA]

Do not select a final decision. Do not add dependencies. Produce evidence Design Mode can use to write or reject a decision.
```

## Expected Output

- Comparison table.
- Pros and cons.
- Fit against project constraints.
- Risks.
- Open questions.
- Recommended decision path for Design Mode.

## Notes

If a new dependency is likely, flag that it will require a `DECISIONS.md` entry before Develop Mode authorization.
