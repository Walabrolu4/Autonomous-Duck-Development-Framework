[Home](../index.md) → [Lifecycle](index.md) → Step 8: Resumption

# Step 8: Resumption (The Pivot Protocol in Practice)

## Goal

Return to any paused project after days, weeks, or months in minutes.

---

## Why This Phase Matters

Because project intelligence lives in Markdown files and not in AI memory, there is nothing to reconstruct. Load the key files and continue.

The three-week break in the Mini Task Tracker example costs two minutes to resume — not two hours. This is the direct payoff of Local File Sovereignty. A project using vibe coding would require extensive re-explanation of everything that was decided. A project using ADDF loads three files and the Architect knows exactly where things stand.

---

## The Action

1. Update `STATE.md` before closing any session (this must already be done)
2. When resuming, open a fresh Architect session and load `STATE.md`, `DOMAIN.md`, and `AGENTS.md`
3. Run the [Resumption Prompt](../prompts.md#resumption)
4. The Architect summarizes the current goal, active sprint status, known blockers, last completed step, and next safest action
5. Load the current sprint folder before opening a Builder session

---

## The Rule

> **STATE.md must be updated at the close of every session without exception. This is the single habit that makes everything else work. If you do only one thing consistently, make it this.**

If STATE.md is not updated before you close a session, the next session has no reliable anchor. The Resumption Prompt cannot tell you where you left off. The Architect will need to reconstruct state from other files — which takes time and introduces uncertainty.

Updating STATE.md is the last action of every session. Make it the last action, every time, without exception.

## See Also

- [STATE.md](../file-reference/state.md)
- [Resumption Prompt](../prompts.md#resumption)
- [Troubleshooting — STATE.md Out of Date](../troubleshooting.md#statemd-is-out-of-date-when-you-return)
