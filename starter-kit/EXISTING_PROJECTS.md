# Adopt ADDF Light Games in an Existing Game Project

**Status:** Stage 3 adoption guide · read-only first

ADDF Light Games must **not overwrite** an existing game's code, design documents, configuration, or existing `AGENTS.md` in the name of “initialization.” Installing a methodology is a design choice and a potential file operation; migration needs a bounded plan and explicit human authorization.

## Step 1 — Inspect safely, without modifying anything

Tell the assistant:

> “I want to evaluate ADDF Light Games for this existing game. **Read-only audit only.** Before reading any files, identify likely secrets/credentials/private data to exclude. Inventory the project structure, engine/toolchain, existing agent instructions, current design docs, branches and known run/test commands. Do not copy templates, install packages, change Git, run installers or execute unverified commands. Report the differences and propose the smallest adoption plan.”

If access to the repository itself is unavailable, provide a file list or safe excerpts. Do not upload private credentials or unidentified archives.

## Step 2 — Map rather than replace

The agent produces a small table:

| Existing source | Proposed Light destination | Conflict? | Action proposed |
| --- | --- | --- | --- |
| Existing game design / GDD | `GAME.md` | unknown | Summarize human-owned intent only after review |
| Existing `AGENTS.md` or tool rules | `AGENTS.md` | **yes** | Compare rules; do not weaken protections |
| Existing roadmap/tasks | `planning/BACKLOG.md` | unknown | Preserve history, map only future candidate slices |
| Existing approvals/decisions | `DECISIONS.md` | unknown | Preserve actual choices; don't fabricate new approvals |
| Existing security boundaries | `SECURITY.md` | unknown | Keep stricter exclusions |
| Existing source code/build | no default modification | no by default | Read-only inventory; propose separate sprint later |

The agent marks each entry `copy`, `adapt`, `leave alone`, or `defer`, with paths and reasons. Existing notes remain primary evidence until the human explicitly approves a new authoritative representation.

## Step 3 — Seek explicit approval of the migration plan

Show:
- All paths to create, edit, move or delete (ideally **create-only** where existing names do not conflict).
- What content would be copied and what original information could be lost.
- Existing agent instructions and whether rules conflict.
- Git branch/worktree choice and backup/rollback strategy.
- Any potentially unsafe command, dependency or external access.
- Which proposed file becomes authoritative and why.

The human approves or revises **this exact migration scope**. A generic “use ADDF Light” is not permission to overwrite existing files or apply code changes.

If the project already uses full ADDF, preserve its detailed historical sprint files and decisions. Map them **conceptually** to Light's three-document sprint model; never blindly rename or delete them. See [../spec/VALIDATION_AND_MIGRATION.md](../spec/VALIDATION_AND_MIGRATION.md).

## Step 4 — Create a safe first Light state

After authorized migration:
- Record `project_origin: existing-project` in `GAME.md`.
- Start `STATE.md` at `research` / `discovering` unless verified evidence supports another state.
- Set `active_sprint: none` unless an actual authorized Light sprint exists.
- Leave `authorized: no`, Gate I and A pending; past source code is **not** evidence of current implementation authorization.
- Preserve active human-owned decisions and known project constraints.
- Identify a modest first improvement or research spike; do not refactor unrelated systems.

## Step 5 — Confirm that adoption didn't rewrite project history

The human verifies the diff, existing game still opens, prior rules and documentation remain accessible, and source files were not silently replaced. Only then begin discovery and choose Sprint 001.

## Recovery

If a template was copied over an existing file without approval: **stop**, save the exact diff, and ask the human whether to restore from Git or a verified backup. Do not force-reset, overwrite uncommitted work, or conceal the mistake.

## Current implementation boundary

This is an adoption *procedure*, not an automated migration tool. Stage 4 will write model/provider instructions, Stage 5 will test this path with a real example, and Stage 6 will automate structural validation.
