[Home](../index.md) → [File Reference](index.md) → STATE.md

# STATE.md

## Purpose

STATE.md is the living status board of the project. It tells any AI session — immediately, without reading anything else — what the current goal is, which sprint is active, what the known blockers are, and what the next action is. Because it is always current, an Architect session can restore full project context from STATE.md, DOMAIN.md, and AGENTS.md alone.

---

## Template

```markdown
# STATE.md

## Current Goal
[One sentence: what are we building right now?]

## Active Sprint
Sprint [NUMBER]: [Brief description]
Branch: sprint/[NNN]-[description]

## Active Parallel Sprint (if any)
Sprint [NUMBER]: [Brief description]
Overlap check: [date confirmed]

## Current Status
[Discovery / Planning / In Progress / Verification / Complete / Blocked]

## Known Blockers
[Blocker or "None"]

## Last Completed Step
[What was the last thing finished?]

## Next Intended Step
[What is the very next action?]

## Files Recently Changed
[filename] - [brief note on what changed]
```

---

## Completed Example

This is what a correctly initialized STATE.md looks like before the first sprint begins:

```markdown
# STATE.md

## Current Goal
Build the Mini Task Tracker — a local task management web app for a single user.

## Active Sprint
None yet — in Discovery Phase.

## Current Status
Discovery

## Known Blockers
None

## Last Completed Step
Initialized project directory and populated foundational files.

## Next Intended Step
Run Project Kickoff Interview to generate DOMAIN.md, STYLE_GUIDE.md, docs/architecture.md.

## Files Recently Changed
AGENTS.md - populated with permission rules
SECURITY.md - populated with safe/never-share lists
DOMAIN.md - first draft written
```

---

## The One Non-Negotiable Rule

> **STATE.md must be updated at the close of every session without exception. This is the single habit that makes everything else work. If you do only one thing consistently, make it this.**

If STATE.md is not updated before you close a session, the next session has no reliable anchor. The Resumption Prompt cannot tell you where you left off. The Architect will guess — and those guesses accumulate into drift.

Updating STATE.md is the last action of every session. Not the second-to-last. The last.

## See Also

- [Step 8: Resumption](../lifecycle/08-resumption.md)
- [Sprint Workflow — Step 10](../sprint-workflow.md#step-10--commit-update-reset)
- [Troubleshooting — STATE.md Out of Date](../troubleshooting.md#statemd-is-out-of-date-when-you-return)
