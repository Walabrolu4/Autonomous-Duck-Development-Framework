# Autonomous Duck Deployment Framework

## What Is the Autonomous Duck Deployment Framework?

The Autonomous Duck Deployment Framework (ADDF) is a deterministic system for AI-assisted software development built around two core mechanisms: **Local File Sovereignty** (the project brain lives in local Markdown files, not in AI chat sessions) and **Dual-Mode Orchestration** (a strict separation between an Architect LLM that plans and a Builder LLM that implements). Any capable LLM can play either role. What matters is mode, not model.

---

## The Problem It Solves

Unstructured AI-assisted development — sometimes called vibe coding — fails predictably for three reasons:

- **Context bleed:** Long chat threads fill with old decisions and abandoned directions. The AI loses track of what was agreed, and regression bugs appear that cannot be explained.
- **Improvisation bias:** When the AI lacks a strict specification, it invents one. It creates database keys that don't match your schema, permission levels that clash with your business logic, and takes the path of least resistance — not the path you intended.
- **The missing anchor:** Conversation history becomes project memory. That memory is fragile, unsearchable, and eventually destroyed by token limits or session loss. When you close the tab, your project context is gone.

ADDF solves all three by moving project memory into local files and enforcing a planning gate (the dry run) before any code is written.

---

## The Central Rule

> **The question is never which AI does what. The question is what files must exist before any AI is allowed to act.**

If the required documentation does not exist before a session begins, the session does not begin. Chat windows are disposable. The files are permanent.

---

## How to Navigate This Wiki

**New to ADDF?** Start with [Core Concepts](core-concepts.md) to understand the key terms, then follow [Getting Started](getting-started.md) for a step-by-step first session.

**Starting a new project?** Go to [Setup and Scaffolding](setup.md) to initialize the directory, then [Getting Started](getting-started.md) to run your first sprint.

**Mid-sprint or returning to a project?** Go directly to [Sprint Workflow](sprint-workflow.md) for the 10-step loop, or [Troubleshooting](troubleshooting.md) if something has gone wrong.

**Looking up a file, prompt, or term?** Use the Quick Links below.

---

## Quick Links

| Resource | What's There |
|----------|-------------|
| [Getting Started](getting-started.md) | Step-by-step first session walkthrough |
| [Core Concepts](core-concepts.md) | The 8 terms every reader must understand |
| [Sprint Workflow](sprint-workflow.md) | The 10-step daily operating loop |
| [Prompt Catalog](prompts.md) | All 9 copy-paste prompts |
| [File Reference](file-reference/index.md) | Templates for every tracking file |
| [Operating Modes](modes/index.md) | Choosing the right mode for each task |
| [The 8-Step Lifecycle](lifecycle/index.md) | The full project arc from idea to resumption |
| [Complete Example](example.md) | Mini Task Tracker — all 8 steps in practice |
| [Troubleshooting](troubleshooting.md) | What to do when things go wrong |
| [Glossary](glossary.md) | Full definitions of all framework terms |
