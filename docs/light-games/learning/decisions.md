# Decisions: Keep Human Agency and Durable Reasoning

A decision record makes it possible for another model—or the same developer next month—to understand **what was chosen, why, what was rejected and when to reconsider it**.

## When to use

Use when the person chooses a significant mechanic, platform, architecture, scope constraint or high-impact behavior, or when a new playtest reverses a previously approved choice.

## Decision tiers

| Tier | Example | Authority |
| --- | --- | --- |
| **T0 routine** | Formatting, local variable naming, harmless implementation detail inside approved scope | Agent may choose |
| **T1 material** | Core mechanic, control feel, platform, feedback style, difficulty progression | Human Gate D |
| **T2 high-impact** | Paid services, public exposure, privacy/credential handling, destructive migration | Human Gate D plus stronger Gate I and separate permissions where needed |

Tier depends on **consequence**, not the number of code lines.

## The record format

Use stable `D-001`, `D-002`, etc. Include:
- the specific question and why it mattered;
- genuine options and tradeoffs;
- sources or experiment evidence, labeled when unverified;
- AI recommendation, explicitly separate from the human choice;
- actual human response and rationale where given;
- effects on scope, criteria and implementation;
- superseded decision, if any;
- an observable revisit trigger.

If a user says “not sure,” mark it deferred, not chosen. Don't fabricate a decision just to fill the starter template.

## Decision example

**D-004 — Immediate or accelerating movement?** The user selected immediate movement because Sprint 001 is intended to isolate obstacle readability. Acceleration remains a candidate for a later feel-tuning experiment. The agent links D-004 from the active `SPRINT.md` and updates `GAME.md` without treating the choice as Gate I.

A later playtest might show oversensitive controls. Create **D-005** referencing D-004 as superseded rather than replacing the original rationale.

## Choice and execution are distinct

A user can approve a design without approving the proposed source operations. Conversely, approval of a narrow code plan cannot be stretched to change the player experience materially. Maintain Gate D and Gate I in different files with their own references.

For an existing project, don't “migrate” earlier approvals into new scope without checking the original evidence and current worktree.

## Avoid excessive logging

Log material choices, not every trivial constant or naming decision. A file with hundreds of T0 entries is hard to use and makes important choices less visible.

## Common failures

**AI recommendation becomes a decision:** The agent writes `human_choice: choose A` before any real answer. Keep pending.

**Silent reversal:** New direction is documented but old decision is deleted. Preserve supersession.

**Source-less confidence:** An inference is cited as fact. Label it honestly.

## Related

[Decision protocol](../../../spec/DECISION_PROTOCOL.md) · [Approval gates](../sprints/approvals.md) · [Backlog](../sprints/backlog.md)
