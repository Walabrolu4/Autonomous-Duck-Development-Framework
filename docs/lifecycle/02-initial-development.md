[Home](../index.md) → [Lifecycle](index.md) → Step 2: Initial Development

# Step 2: Initial Development (The Prototype)

## Goal

Build the first working version of the core feature set under strict Architect control.

---

## The Tools

Architect LLM for blueprint generation; Builder agent for execution.

---

## The Action

The sequence:

1. Human reviews ledger files (DOMAIN.md, DECISIONS.md, QUESTIONS.md, RISKS.md)
2. Architect generates the Sprint Pack (requirements.md, blueprint.md, acceptance.md)
3. Human checks the [Blueprint Review Gate](../sprint-workflow.md#step-2b--human-blueprint-review-gate) — verifies every Architect assumption
4. Builder performs a Level 0 Pre-Flight Dry Run and stops
5. Architect runs the [Sanity Audit](../prompts.md#sanity-audit) on the dry run output
6. Builder executes at Level 1 on the designated sprint branch

For the complete 10-step loop, see [Sprint Workflow](../sprint-workflow.md).

---

## The Rule

The Builder generates only the files listed in the blueprint, on the designated branch. No business logic is invented. No files outside the blueprint scope are touched.

---

## Why the Builder Cannot Invent Business Logic

If the Builder invents a database key, API endpoint, or permission rule that is not in DOMAIN.md, that invention becomes part of the codebase. Future sprints reference it. It compounds. Eventually the AI is maintaining logic it invented that may contradict your actual business rules.

The dry run gate exists to catch this before it happens. The Builder lists what it intends to do. You review it. You approve. Only then does it act.

## See Also

- [Sprint Workflow](../sprint-workflow.md)
- [Mode 2: Feature Sprint](../modes/feature-sprint.md)
- [Builder Pre-Flight Dry Run prompt](../prompts.md#dry-run)
