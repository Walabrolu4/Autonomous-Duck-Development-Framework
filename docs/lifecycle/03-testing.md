[Home](../index.md) → [Lifecycle](index.md) → Step 3: Testing

# Step 3: Testing (Harness First)

## Goal

Establish a testing harness before functional code scales beyond the prototype.

---

## Why This Phase Matters

The most effective AI development teams invert the vibe coding testing habit. Instead of building first and checking visually after, they build the evaluation framework before the AI writes implementation code.

A visual check is not acceptance. A passing test suite is. If acceptance criteria are not written down before the Builder starts, the AI declares success when the UI looks right — even if the underlying logic is broken.

---

## The Action

Before the Builder writes new functional code for a sprint, mandate that it writes the unit tests first. The `acceptance.md` checklist drives what must be proven before the sprint closes. The Builder then runs every command in `COMMANDS.md` and pastes the raw terminal output into `implementation_log.md`.

---

## The Rule

The Builder must run all commands listed in `COMMANDS.md` and paste terminal output directly into `implementation_log.md`. Visual inspection alone is not acceptance.

"Tests passed" in a summary can mean 1 test passed and 47 were skipped. The raw output tells you what actually ran.

## See Also

- [acceptance.md](../file-reference/sprint-files.md#acceptancemd)
- [implementation_log.md](../file-reference/sprint-files.md#implementation_logmd)
- [COMMANDS.md](../file-reference/commands.md)
