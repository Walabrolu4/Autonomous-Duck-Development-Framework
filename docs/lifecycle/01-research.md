[Home](../index.md) → [Lifecycle](index.md) → Step 1: Research & Global Architecture

# Step 1: Research & Global Architecture

## Goal

Build the project brain before writing a single line of code.

---

## Why This Phase Exists

Every failure mode of AI-assisted development traces back to skipping this step. When the AI has no specification to work from, it invents one. The Step 1 output is the specification that every subsequent phase works from. A DOMAIN.md written here prevents the improvisation bias from taking hold in every sprint that follows.

---

## The Tool

Architect LLM. Claude CLI is preferred when available because it is well-suited for structured planning tasks, but any capable LLM works. The framework is the same regardless of model choice — the files you produce are what matter.

---

## The Action

Open the Architect LLM and feed it raw ideas, feature wishlists, client emails, and rough notes. Run the [Project Kickoff Interview prompt](../prompts.md#kickoff-interview). The Architect asks clarifying questions and generates foundational files from your answers.

This is Architect Mode in action: the AI acts as a senior technical lead helping you define the project before any code is written.

---

## Output Files Produced

- `DOMAIN.md` — business logic, entities, and workflows
- `STYLE_GUIDE.md` — naming conventions and code standards
- `docs/architecture.md` — high-level structure
- `STATE.md` — initialized with Discovery Phase status
- `DECISIONS.md` — starter ledger
- `QUESTIONS.md` — starter ledger
- `RISKS.md` — starter ledger

---

## The Rule

Do not proceed to Step 2 until `DOMAIN.md` contains real business definitions, `SECURITY.md` is populated, and there are no `QUESTIONS.md` items marked as sprint blockers.

## See Also

- [Project Kickoff Interview prompt](../prompts.md#kickoff-interview)
- [DOMAIN.md](../file-reference/domain.md)
- [Lifecycle Overview](index.md)
