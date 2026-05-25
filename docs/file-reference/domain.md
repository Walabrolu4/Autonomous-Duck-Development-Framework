[Home](../index.md) → [File Reference](index.md) → DOMAIN.md

# DOMAIN.md

## Purpose

DOMAIN.md is the business logic specification. It defines what the project is, what the core entities are, how they behave, and what the project explicitly does not handle. Every rule, entity, or workflow not written in DOMAIN.md is a gap the AI may fill with its own invention. The Architect reads DOMAIN.md before generating any blueprint. The Builder reads it to know the boundaries of what it can build.

---

## Template

```markdown
# DOMAIN.md Business Logic and Definitions

## Project Overview
[Two to three sentences describing what this project does and why it exists.]

## Core Entities

### [Entity Name]
Definition: [Exact meaning in this project]
Key fields: [Important properties]
Business rules: [How this entity behaves]
What it is NOT: [Clarify common confusions]

## Workflows

### [Workflow Name]
1. [Step 1]
2. [Step 2]
Edge case: [What happens if X fails?]

## Out of Scope
This project explicitly does NOT handle:
- [Item 1]
- [Item 2]
```

---

## What Happens If You Skip It

If DOMAIN.md is empty or incomplete, the AI fills the gaps with plausible guesses. It invents database keys that may not match your schema, creates permission levels that clash with your business logic, and takes the path of least resistance — not the path that matches your intent.

These guesses compound over time. A key invented in Sprint 3 is referenced in Sprint 7 and Sprint 12. By Sprint 18, the AI is maintaining logic it invented that may directly contradict the actual business rules you intended. Writing DOMAIN.md before the first Architect session is how you prevent the improvisation bias from taking hold.

---

## Completed Example

For a fully completed DOMAIN.md showing exactly what this looks like in practice, see the Mini Task Tracker example in [Step 1: Research & Architecture](../example.md#step-1--research--architecture).

## See Also

- [Complete Example](../example.md)
- [Getting Started — Step 4](../getting-started.md#step-4--write-your-domainmd)
- [Core Concepts](../core-concepts.md)
