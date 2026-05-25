[Home](index.md)

# Dual-Mode Orchestration

## The Two Modes

The framework uses two distinct operational modes for AI sessions. Any capable LLM can play either role. What matters is which mode you invoke, not which model you use. The same Claude session that acts as Architect today can act as Builder tomorrow — the mode is set by the instructions you give it, not by the tool.

---

## Architect Mode {#architect-mode}

Architect Mode runs in any capable LLM — Claude Pro, ChatGPT Plus, Gemini Advanced, a terminal interface, or a browser project sandbox. Its responsibility is to answer **what** and **why**: process definitions, relational field mapping, structural risk mitigation, resolution of logical unknowns, and generation of development blueprints.

**Outputs:** `requirements.md`, `blueprint.md`, `acceptance.md`

**Strict constraint:** The Architect does not write application source files, does not read live runtime logs, and does not touch the codebase.

**Why the Architect cannot write code:** If the Architect writes source code, it is simultaneously deciding what to build and how to build it. That collapses the planning and execution separation that makes this framework work. The Architect sets the standard. The Builder is measured against it. If they are the same session, there is no independent standard.

---

## Builder Mode {#builder-mode}

Builder Mode runs in a local repository-aware coding environment — Cursor, Claude Code, Cline, Codex, or similar. Its responsibility is to answer **how**: consume approved blueprints, generate source files in `/src`, execute local tests, and register environment updates.

**Outputs:** Source files, `dry_run.md`, `implementation_log.md`, test output

**Strict constraint:** The Builder may not invent unapproved business rules. It must execute a read-only dry run before changing any files and must stop after the dry run until permission is granted.

**Why the Builder must stop after the dry run:** The pause between planning and execution is the entire safety model of the framework. If the Builder could skip the dry run, there would be no window to catch scope creep before the code is written. The dry run is the review step. Removing it removes the review.

---

## The File System: The Sovereign Brain {#the-file-system-the-sovereign-brain}

The core brain of the framework lives on your drive in a collection of Markdown tracking files. Because instructions survive independently of any model state, you can run an Architect session in Claude, hit a rate limit, copy the updated tracking files, and continue in ChatGPT or Gemini without context degradation.

**The files are the project. The AI is the tool.**

This is why Local File Sovereignty is the foundational principle. Models are interchangeable. The files are not.

---

## Builder Permission Levels {#builder-permission-levels}

You assign the permission level explicitly at the start of every Builder session. Start at Level 1 for almost every sprint. Levels 3 and 4 are for deliberate, high-stakes changes where you want a maximum audit trail.

| Level | Name | Operational Parameters |
|-------|------|------------------------|
| **0** | Read-Only | Structural analysis and file scanning only. Zero code mutation or file creation permitted. Used for pre-flight dry runs. |
| **1** | Sprint Scope | Standard default. The Builder may modify or create only files explicitly listed in the active sprint blueprint. |
| **2** | Approved Expansion | The Builder may generate minor auxiliary helper modules if surfaced during the dry run and validated by the Architect. |
| **3** | Supervised Refactor | Authorized to mutate adjacent files outside the core blueprint path, provided every change is logged. |
| **4** | Migration | Heavy schema adjustments or complete architecture overhauls. Requires explicit rollback logs before processing begins. |

Level 2 is appropriate when the dry run reveals a helper module the blueprint did not anticipate but the Architect approves. Level 3 is for deliberate refactors. Level 4 is for migrations — `rollback_log.md` must be pre-filled before the Builder begins at this level.

---

## Multi-CLI Protocol and Compute Agnosticism

Models are treated as interchangeable, temporary compute engines. The developer loads the same local configuration files into whichever model is most suited for the task.

- **Claude CLI** — well-suited for schema planning, blueprint assembly, and code-review checks. Its structured reasoning makes it effective for Architect tasks.
  ```
  cat AGENTS.md STATE.md DOMAIN.md | claude "Compile Sprint Pack NNN"
  ```

- **Gemini CLI** — well-suited for high-capacity ingestion during data parsing discovery gates due to its large context window.
  ```
  cat messy_log.csv | gemini "Map data vectors per AGENTS.md rules"
  ```

- **GPT CLI** — well-suited for structural code style verification and rule compliance checks.
  ```
  cat STYLE_GUIDE.md src/app.ts | gpt "Identify design standard fractures"
  ```

These are recommendations, not requirements. The framework works with any combination of models. What matters is that the same local files feed every model — that consistency is what makes models interchangeable.

---

## Token Economics

Keep runtime costs efficient by: parsing compact data payloads rather than full file dumps; splitting large inventory lists across multiple sessions; and routing basic text translation and style tasks to smaller, optimized models such as GPT-4o-mini or Claude Haiku. The [Context Loading Protocol](file-reference/index.md#context-loading-table) defines which files each session type needs — loading only those files is the primary cost-control mechanism.

## See Also

- [Core Concepts](core-concepts.md)
- [Sprint Workflow](sprint-workflow.md)
- [AGENTS.md](file-reference/agents.md)
