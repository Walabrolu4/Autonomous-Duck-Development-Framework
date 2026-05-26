# Research Mode

Research Mode is the evidence-gathering mode — it investigates the problem space so that Design Mode can plan against known ground.

## Table of contents

1. [When to use Research Mode](#when-to-use-research-mode)
2. [What Research Mode may produce](#what-research-mode-may-produce)
3. [What Research Mode must not do](#what-research-mode-must-not-do)
4. [The Research Mode prompt](#the-research-mode-prompt)

---

## When to use Research Mode

Use Research Mode when the team needs to:

- understand a domain or problem space before committing to a direction,
- compare tools, libraries, or approaches,
- summarize external documentation or prior art,
- evaluate technical or business constraints,
- identify risks before design begins,
- or list unknowns that would block architecture decisions.

Research Mode is the first mode in the lifecycle for any work that contains meaningful unknowns. If the problem is well-understood and scope is clear, skip Research Mode and start in Design Mode.

**Rule:** Do not design against unknowns you have not named.

---

## What Research Mode may produce

```
research_notes.md
source_summary.md
tool_comparison.md
open_questions.md
risk_notes.md
research_summary.md
```

These files go in the `research/` folder or the relevant sprint or feature folder. They are inputs to Design Mode — not binding project decisions.

---

## What Research Mode must not do

Research Mode must not:

1. write source code,
2. mutate implementation files,
3. make final architecture decisions,
4. add dependencies,
5. or convert uncertain findings into binding project rules.

Research findings are evidence. They become decisions only after Design Mode processes them and the human approves.

**Rule:** Research Mode gathers evidence. It does not decide or build.

---

## The Research Mode prompt

Load this prompt at the start of any Research Mode session. Replace the bracketed placeholders with the actual topic, context, and constraints.

```
You are operating in Research Mode.

Research:
[topic]

Context:
[context]

Constraints:
[constraints]

Do not write code.
Do not make final project decisions.

Produce:
1. Summary
2. Findings
3. Options
4. Tradeoffs
5. Risks
6. Open questions
7. Recommended next step for Design Mode
```

The full prompt catalog — including prompts for every other mode and workflow — is at [Prompt Catalog](../prompt-catalog.md).

The natural next step after Research Mode is [Design Mode](design-mode.md).

---

[← Modes Overview](index.md) · [← Wiki Home](../index.md) · ADDF v3.5
