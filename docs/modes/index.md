# Operating Modes

Every AI session runs in one explicit mode — the mode answers what the model is allowed to do.

## Table of contents

1. [The three modes](#the-three-modes)
2. [Mode boundaries](#mode-boundaries)
3. [Declaring a mode](#declaring-a-mode)

---

## The three modes

ADDF has three operating modes. Each is a distinct write-permission contract between the human operator and the model.

**Research Mode** investigates and synthesizes information. It gathers evidence, compares options, summarizes sources, and names risks. It does not decide or build.

**Design Mode** writes the project memory. It converts research, intent, and feedback into durable Markdown artifacts — domain files, sprint packs, retrospectives, and handoff notes. It does not write source code.

**Develop Mode** changes the actual project. It is the only mode allowed to write code or modify implementation assets. It must produce a Dry Run and wait for authorization before touching any file.

![Three Operating Modes](_PDF/images/2_Three Operating Modes.png)

---

## Mode boundaries

| Mode | Primary action | Writes | Must not write |
|---|---|---|---|
| Research Mode | Investigate | Research notes, summaries, open questions | Code, final decisions |
| Design Mode | Specify | Markdown project memory | Source code, implementation files |
| Develop Mode | Implement | Approved code, tests, implementation logs | Unapproved files, invented rules |

A lifecycle step may involve more than one mode. A session has one explicit mode.

**Rule:** Mode controls write permission.

---

## Declaring a mode

Declare the mode at the top of every AI session, before any other instruction. The declaration sets the permission contract for that session.

Examples:

```
You are operating in Research Mode.
```

```
You are operating in Design Mode for [PROJECT_NAME].
```

```
You are operating in Develop Mode.
Permission Level: 0.
```

The prompts in the [Prompt Catalog](../prompt-catalog.md) begin with mode declarations and include everything else the model needs to orient itself.

**Rule:** Declare the mode before the model acts.

---

### Mode pages

- [Research Mode](research-mode.md)
- [Design Mode](design-mode.md)
- [Develop Mode](develop-mode.md)

For the permission level system that governs Develop Mode, see [Develop Mode Permission Levels](../permission-levels.md).

---

[← Wiki Home](../index.md) · ADDF v3.5
