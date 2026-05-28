# STYLE_GUIDE.md

**The Autonomous Duck Deployment Framework — project brain style reference.**

This file is the concise style reference for AI sessions. Load it before generating any content — documentation, prompts, starter kit files, or example projects. The complete brand guide is at `docs/_PDF/style Guide/STYLE_GUIDE.md`.

> Serious about the method. Light about ourselves.

---

## 1. Voice

Write like a senior engineer explaining a process to a peer: declarative, concrete, peer-level, precise, and occasionally wry.

The voice is not jokey, corporate, salesy, folksy, or vague.

**Tone by context:**

| Context | Tone |
|---|---|
| Documentation body | Patient, concrete, instructional |
| Prompts (for the model) | Imperative, structured, no filler |
| Error messages | Honest, specific, immediately actionable |
| Hero copy | Confident, declarative |
| `Quack!` | Wry, brief, earned |
| Retrospectives | Plain, blame-free, factual |

---

## 2. Sentence rules

- **Active voice** by default. Passive when the actor doesn't matter.
- **Second person** (`you`) in docs and walkthroughs.
- **Present tense** for behavior. **Imperative** for instructions.
- **Maximum ~32 words** per sentence.
- Mix sentence lengths deliberately. Short declarative openers. Longer sentences to explain.

---

## 3. Banned words and phrases

Never use:

| Banned | Use instead |
|---|---|
| *just*, *simply*, *easy*, *easily* | Cut entirely |
| *basically*, *essentially*, *literally* | Cut entirely |
| *amazing*, *powerful*, *seamless*, *robust* | Be specific |
| *unleash*, *supercharge*, *empower*, *delight* | Describe the actual outcome |
| *Let's*, *Let me* | Use the imperative |
| *magical*, *magic* | Describe the mechanism |
| *AI-powered*, *AI-driven* | Describe what the AI does |
| *cutting-edge*, *next-gen*, *revolutionary* | Cut entirely |
| *best practice* | *The rule is* / *The convention is* |
| *unlock* | Describe the actual capability |
| *workflow* | *lifecycle*, *protocol*, *sprint workflow* |
| *solution*, *platform*, *ecosystem* | *framework*, *methodology* |
| *users* | *operators*, *developers* |

---

## 4. Canonical framework terminology

Use these terms exactly. Capitalization matters.

| Term | Rule |
|---|---|
| **Research Mode** | Always capitalized. |
| **Design Mode** | Always capitalized. |
| **Develop Mode** | Always capitalized. |
| **Sprint Pack** | Always capitalized. |
| **Dry Run** | Always capitalized. |
| **Permission Level** | Always capitalized. |
| **the project brain** | Lowercase in prose is fine. |
| **Local File Sovereignty** | Always capitalized (proper-noun principle). |
| **vibe coding** | Always lowercase (the anti-pattern). |

Do not use Architect Mode or Builder Mode as public ADDF modes.

---

## 5. File and path naming

| Type | Convention | Example |
|---|---|---|
| Project brain files | `UPPER_SNAKE_CASE.md` | `STATE.md`, `DOMAIN.md` |
| Sprint folders | `sprint_NNN` | `sprint_001` |
| Sprint files | `lowercase_snake.md` | `dry_run.md` |
| Documentation pages | `lowercase-kebab.md` | `getting-started.md` |

Always wrap file names in backticks in prose: `STATE.md`, not STATE.md.

---

## 6. Document structure

Every documentation page follows this pattern:

1. **H1 title** — what this document is.
2. **One-sentence summary** — what it covers.
3. **Table of contents** — if the page has more than three sections.
4. **Sections** — each with: opener, how, rule, example.
5. **A rule** — the non-negotiable stated as a bold sentence.
6. **Footer** — file name, version, last reviewed.

Every major section must include a rule. The rule is a short, declarative sentence that states the non-negotiable. Format:

> **Rule:** [State the non-negotiable.]

---

## 7. No emoji

No emoji in documentation, prompts, READMEs, or any public file.

The one exception: `Quack!` is the framework's signature. Use it at most once per page, only at the end of a long-form document, at a success moment, or in an empty state. It is set in Instrument Serif italic on the website; in plain text in Markdown.

---

## 8. Code and file references

Use fenced code blocks for multi-line commands, file trees, and configuration examples. Use inline backticks for file names, paths, commands, and identifiers in prose.

```
# Correct
Load `STATE.md` before running Design Mode.

# Incorrect
Load STATE.md before running Design Mode.
Load *STATE.md* before running Design Mode.
```

---

## 9. Lists, tables, and headings

- Use ordered lists for sequences where order matters.
- Use unordered lists for sets where order doesn't matter.
- Use tables when comparing two or more things across the same dimensions.
- Do not use tables for simple lists.
- Headings are numbered (`## 1.`, `## 2.`) in long reference documents. Unnumbered in short pages.

---

## 10. The arrow

The arrow `→` is the framework's signature directional indicator. Use it for:

- "Next step" links.
- Flow sequences.
- CTAs on the website.

Never use `>` or `->` as a substitute.

---

## Full reference

For typography, color, logo usage, visual rules, diagrams, and the complete vocabulary table, see:

```
docs/_PDF/style Guide/STYLE_GUIDE.md
```

That file is the complete brand guide. This file is the AI-session quick reference.

**Rule:** Load `STYLE_GUIDE.md` before generating any content that will be published.

---

*ADDF · `STYLE_GUIDE.md` · v1.0 · maintained as part of the project brain*
