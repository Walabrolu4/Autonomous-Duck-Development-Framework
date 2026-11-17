# Planning and the Exact Dry Run

`PLAN.md` is the boundary between thoughtful design and implementation permission. Its function is not to produce a long essay; it's to make the **real edits and effects visible to the human before they occur**.

## When to use

Use after a bounded sprint and its acceptance checks are selected, before any game-source, test, asset, manifest or deployment configuration is edited.

## First check the inputs

Verify the active sprint ID, `SPRINT.md` revision, selected design and Gate D evidence. Check the actual repository and known files **read-only** within `SECURITY.md` boundaries. A missing dependency or unknown engine installation should be reported, not guessed.

## Fill the plan

The required dry run covers:

| Section | Practical question |
| --- | --- |
| Inputs/assumptions | Which approved sprint revision and project state are we planning for? |
| Exact file operations | What exact files are created, modified, moved or deleted, and why? |
| Commands/side effects | What commands run, where, and what do they write/download? |
| Dependencies/assets | Which versions, licenses, downloads and outside services are involved? |
| Implementation sequence | What's the smallest safe sequence? |
| Verification plan | How will each `AC-##` be tested, and who tests player feel? |
| Risks/rollback | What might break, what should stop work and how is it reversed? |
| Open ambiguities | Which unresolved questions prevent authorization? |
| Gate I | What exact revision/scope did the human approve? |
| Execution record | What actually happened after authorization? |

## Example dry-run scope

```md
| Operation | Exact path | Purpose | Scope constraint |
| --- | --- | --- | --- |
| create | game.js | AC-01 movement | No networking or inventory |
| create | index.html | Playable arena | One page, no external embeds |
| create | tests/game.test.cjs | AC-01/02 logic | Existing Node test runner only |
```

The command section might authorize `node --test tests/game.test.cjs` in the game folder and **no package installation**. Any necessary additional command must appear in a revised plan.

A broad wildcard such as “all files needed” is not a suitable authorized scope.

## Ask for a precise Gate I

After showing the plan, ask: “Do you authorize Sprint 001 `PLAN.md` r1 for these paths and commands, with these exclusions?” Record the **actual reply** and its source. A user may approve only a subset; revise the plan to accurately reflect that rather than stretching the words.

Plan revision `r2` that adds a dependency or a file **requires fresh Gate I**. Preserve earlier revision/approval history; never overwrite it to imply retroactive consent.

## Approvals and technical capability

An agent tool with shell access can technically run a command even before permission exists. That doesn't make it authorized. A validator that sees `gate_i_status: authorized` may check matching fields but cannot verify the human actually typed the response.

Public deployment, purchases, secret access, destructive operations or external messages require **separate explicit special approval**, not just ordinary coding Gate I.

## Common failures

**Plan without acceptance checks:** How can a reviewer judge whether files are necessary? Define `AC-##` first.

**Version mismatch:** Gate I says r1, current plan says r2. Stop and re-approve.

**Execution before authorization:** An agent runs npm install “just to inspect.” Treat the install as a side effect needing review.

## Related

[Approvals](approvals.md) · [Implement stage](../lifecycle/implement.md) · [Security](../quality/security.md)
