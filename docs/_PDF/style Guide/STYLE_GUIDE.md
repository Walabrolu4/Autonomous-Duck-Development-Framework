# STYLE_GUIDE.md

**The Autonomous Duck Deployment Framework — complete style guide.**
Visual identity, voice, and application across every medium we ship in.

> Serious about the method. Light about ourselves.

Version 1.0 · maintained as part of the project brain · last reviewed May 2026

---

## Table of contents

1. [How to use this document](#1-how-to-use-this-document)
2. [Brand foundation](#2-brand-foundation)
3. [Logo & mark system](#3-logo--mark-system)
4. [Color](#4-color)
5. [Typography](#5-typography)
6. [Layout, grid & spacing](#6-layout-grid--spacing)
7. [Iconography](#7-iconography)
8. [Motifs & visual language](#8-motifs--visual-language)
9. [Imagery & illustration](#9-imagery--illustration)
10. [Voice & language](#10-voice--language)
11. [Vocabulary](#11-vocabulary)
12. [Microcopy patterns](#12-microcopy-patterns)
13. [Application — Website](#13-application--website)
14. [Application — Slide decks](#14-application--slide-decks)
15. [Application — Documentation](#15-application--documentation)
16. [Application — Marketing & social](#16-application--marketing--social)
17. [Application — Code, repos & READMEs](#17-application--code-repos--readmes)
18. [Asset library](#18-asset-library)
19. [Pre-publish checklist](#19-pre-publish-checklist)
20. [Glossary](#20-glossary)

---

## 1. How to use this document

This file is the single source of truth for anything that carries the ADDF name. Load it into any AI session before producing a deliverable; check any human-authored artifact against it before publishing.

**The order of authority, when something conflicts:**

1. This document.
2. The brand book (`Brand Identity.html`) — the visual reference.
3. `AGENTS.md` and `DOMAIN.md` — the project brain.

If you find a conflict between this guide and an existing artifact, the artifact is wrong. Update the artifact. If this guide is missing the answer, propose an addition in a pull request — don't improvise.

**This document is itself written in the voice it describes.** Re-read sections 10–12 if you want to feel the cadence.

---

## 2. Brand foundation

### 2.1 What we are

ADDF is a **deterministic methodology for AI-assisted software development**. It is a system of files, prompts, and protocols — not a tool, not a platform, not a product. The framework is compute-agnostic: any capable LLM can run it.

### 2.2 What we believe

Three principles. Memorize them. They drive every design and copy decision.

| # | Principle | Implication |
|---|---|---|
| 01 | **The files are the project.** | Markdown on disk is the source of truth. AI sessions are interchangeable compute. |
| 02 | **A duck can't invent your business logic.** | Specifications come from the human; execution comes from the model. |
| 03 | **Cleaner context beats more context.** | Each session reads only the files it needs. |

### 2.3 Who we talk to

The reader is competent. Probably a senior developer or a tech lead. They've used AI coding tools, hit the limits, and are looking for a real methodology — not a magic button. Write for that person. Never write down.

### 2.4 What we are not

- We are not "an AI assistant for developers." Research Mode, Design Mode, and Develop Mode are session contracts, not products.
- We are not a SaaS. There's nothing to sign up for.
- We are not a religion. People can use the parts they want.
- We are not a joke. The duck is a metaphor that does work.

---

## 3. Logo & mark system

### 3.1 The mark

The mark is a left-facing rubber duck with three circuit traces extending from the back, each terminating in an open ring. The duck (rubber duck debugging) and the traces (the AI) are the two metaphors that built the framework.

**Source files (in `assets/`):**

| File | Use |
|---|---|
| `duck-logo.png` | Yolk-yellow duck — for use on Paper, Ink, Pond backgrounds. |
| `duck-logo-ink.png` | Ink duck — for use on Yolk backgrounds. |
| `duck-logo-paper.png` | Paper duck — for use on dark Ink/Pond when extra contrast is needed. |

A vector source (`duck-logo.svg`) is in active production. PNGs are interim assets.

### 3.2 Lockups

| Lockup | Composition | Primary use |
|---|---|---|
| **Mark only** | Duck mark, no wordmark. | App icons, favicons, social avatars, in-product nav, tight corners. |
| **Horizontal lockup** | Mark + `ADDF` wordmark to the right, baseline-aligned with the duck's body. | Site nav, document headers, footer. |
| **Stacked lockup** | Mark above, wordmark below, centered. | Hero panels, deck title slides, posters. |
| **Wordmark only** | `ADDF` or full `Autonomous Duck Deployment Framework` in Instrument Serif. | When the duck has already appeared on the page. |

### 3.3 Color application of the mark

| Background | Mark color | Notes |
|---|---|---|
| Paper (`#F6F1E4`) | Yolk (`#F5C518`) | The default. |
| Ink (`#14110D`) | Yolk | The "reverse" application. |
| Yolk (`#F5C518`) | Ink (`#14110D`) | Never put yolk-on-yolk. |
| Pond (`#1B4D3E`) | Yolk | Use sparingly. |
| Photographic or busy backgrounds | Never. | Place the mark on a solid color field. |

### 3.4 Minimum sizes

| Application | Minimum size (mark) |
|---|---|
| Web favicon | 16 × 16 px |
| App icon | 32 × 32 px |
| Document body | 24 × 24 px |
| Slide titles | 64 × 64 px |
| Print, business card | 0.5 in (12.7 mm) |

Below these sizes, the circuit traces stop reading. If you must go smaller, drop the traces and use a simplified duck silhouette — and request a real vector simplified variant from the brand owner.

### 3.5 Clear space

Reserve clear space equal to the **height of the duck's head** on every side of the lockup. Nothing — type, image, edge of canvas — encroaches.

### 3.6 Don't

- ✗ Don't recolor the mark in any color outside the palette.
- ✗ Don't apply gradients, shadows, glows, outlines, or strokes.
- ✗ Don't rotate, skew, squish, or stretch.
- ✗ Don't place the mark on photographic or noisy backgrounds.
- ✗ Don't combine the mark with other logos in a lockup unless it's a formal partnership and brand has approved it.
- ✗ Don't animate the mark unless it's a brand-approved motion treatment.
- ✗ Don't add emoji or sparkles near the mark. The duck is the joke. There is no other joke.

---

## 4. Color

### 4.1 The palette

| Token | Name | Hex | RGB | OKLCH | Role |
|---|---|---|---|---|---|
| `--yolk` | Yolk | `#F5C518` | 245 197 24 | 0.83 0.16 89 | Primary. The brand color. |
| `--yolk-deep` | Yolk Deep | `#E2B00B` | 226 176 11 | 0.78 0.16 85 | Yolk on yolk — italics, hover states, fine type on yolk fields. |
| `--ink` | Ink | `#14110D` | 20 17 13 | 0.13 0.01 80 | Type, lines, the duck on yolk. |
| `--ink-soft` | Ink Soft | `#2A2620` | 42 38 32 | 0.22 0.01 80 | Secondary type, dividers, muted UI. |
| `--paper` | Paper | `#F6F1E4` | 246 241 228 | 0.95 0.02 91 | Default canvas. Warm, never cool. |
| `--paper-warm` | Paper Warm | `#EFE7D2` | 239 231 210 | 0.92 0.03 92 | Card backgrounds, surface tints. |
| `--pond` | Pond | `#1B4D3E` | 27 77 62 | 0.34 0.05 165 | Success state, secondary accent. |
| `--beak` | Beak | `#E89A1F` | 232 154 31 | 0.72 0.16 65 | Warning state, occasional accent. |
| `--mist` | Mist | `#E6DFCB` | 230 223 203 | 0.89 0.03 91 | Subtle borders, dividers. |
| `--rule` | Rule | `#DDD2B5` | 221 210 181 | 0.86 0.04 89 | Strong borders, table rules. |

### 4.2 Usage ratio

The 60 / 25 / 10 / 5 rule, by surface area:

| Color | Share | Role |
|---|---|---|
| Paper | 60 | Canvas, page backgrounds, default surfaces. |
| Ink | 25 | Type, navigation, primary controls. |
| Yolk | 10 | Hero moments, CTAs, brand emphasis. |
| Pond | 5 | Success states, occasional accents. |

Beak appears only in functional states (warning, caution), not as decoration.

### 4.3 Accessibility

| Foreground | Background | Contrast | WCAG |
|---|---|---|---|
| Ink on Paper | 17.4 : 1 | AAA | ✓ |
| Ink on Yolk | 12.1 : 1 | AAA | ✓ |
| Paper on Ink | 17.4 : 1 | AAA | ✓ |
| Paper on Pond | 8.6 : 1 | AAA | ✓ |
| Yolk on Ink | 11.3 : 1 | AAA | ✓ |
| Yolk on Paper | 1.6 : 1 | ✗ | Never use for type. |
| Yolk-deep on Yolk | 1.3 : 1 | ✗ | Decorative italics only. |

**Rules:**
- Body type (16px+) must hit AA (4.5 : 1).
- Headings (24px+) and bold (18px+) may use AA Large (3 : 1).
- Yolk on Paper is decorative only — never use for any text the reader must read.

### 4.4 What we don't use

- No pure black. Ink is `#14110D`, slightly warm.
- No pure white. Paper is `#F6F1E4`, warm cream.
- No gradients. Solid fields only.
- No drop shadows. Use a 1px Rule border instead.
- No blue, no purple, no pink. The palette has six colors. That is the palette.

---

## 5. Typography

### 5.1 The trio

| Family | Role | Weights | Source |
|---|---|---|---|
| **Instrument Serif** | Display & emphasis | 400, 400 italic | [Google Fonts](https://fonts.google.com/specimen/Instrument+Serif) |
| **Space Grotesk** | UI & body | 400, 500, 600, 700 | [Google Fonts](https://fonts.google.com/specimen/Space+Grotesk) |
| **JetBrains Mono** | Code, labels, eyebrows | 400, 500, 600 | [Google Fonts](https://fonts.google.com/specimen/JetBrains+Mono) |

CSS import (for web):

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
```

### 5.2 Hierarchy

| Style | Family | Size (web px) | Size (deck px @1920×1080) | Line height | Weight | Tracking |
|---|---|---|---|---|---|---|
| Hero display | Instrument Serif | 88–120 | 160–220 | 0.95–1.0 | 400 | -0.025em |
| H1 | Instrument Serif | 56–72 | 96–120 | 1.0 | 400 | -0.02em |
| H2 | Instrument Serif | 40–48 | 72–88 | 1.05 | 400 | -0.02em |
| H3 | Space Grotesk | 24–28 | 44–52 | 1.2 | 600 | -0.01em |
| H4 / Lede | Space Grotesk | 18–22 | 32–40 | 1.4 | 500 | -0.005em |
| Body | Space Grotesk | 16 | 28–32 | 1.55 | 400 | 0 |
| Small body | Space Grotesk | 14 | 24 | 1.5 | 400 | 0 |
| Eyebrow / Label | JetBrains Mono | 11 | 16–18 | 1.4 | 500 | 0.14em uppercase |
| Code (inline) | JetBrains Mono | 0.92em of body | same | inherit | 400 | 0 |
| Code (block) | JetBrains Mono | 13–14 | 22–26 | 1.7 | 400 | 0 |

**Minimum sizes:**
- Web body: 16 px. Never smaller for content the reader must read.
- Slide body: 24 px @ 1920×1080. Never smaller.
- Print body: 10 pt.
- Eyebrows / labels: 11 px web, 16 px deck, 8 pt print. These are not body text — they are decoration with a job.

### 5.3 When to use which face

| Use Instrument Serif when | Use Space Grotesk when | Use JetBrains Mono when |
|---|---|---|
| Setting a section opener | Writing body text | Showing code |
| Speaking with personality | Building UI | Labelling diagrams |
| Quoting an aphorism | Listing bullet points | Marking a file path |
| Writing *Quack!* | Captioning a figure | Setting an eyebrow |
| Italics for emphasis | Buttons, links, form labels | Section numbers (e.g. `§07`) |

**The serif italics are load-bearing.** They're how the brand sounds *out loud*. Use them in moments — not paragraphs.

### 5.4 Letter-spacing & line-height notes

- Headlines (Instrument Serif) need *negative* tracking: `-0.02em` to `-0.025em`. Without it the face looks limp at large sizes.
- Eyebrows / labels (JetBrains Mono uppercase) need *positive* tracking: `0.14em` minimum.
- Tight line-height (< 1.0) on Instrument Serif causes descender overlap. **For multi-line headlines, use `line-height: 1.05`–`1.1`.** For single-line display, you can go to `0.95`.
- Body line-height: never tighter than 1.45 for Space Grotesk. Never looser than 1.65.

### 5.5 What we don't use

- No font besides the three above. Ever.
- No system-font fallback aside from the family-generic stack (`serif`, `sans-serif`, `monospace`).
- No alternative weight imports. The five weights above are the entire set.
- No drop caps. No underlines. No outlined text. No text-shadows.

---

## 6. Layout, grid & spacing

### 6.1 Spacing scale

A modified 4 / 8 scale. All margins and gaps come from this list. **No custom spacing.**

| Token | Value (px) | Use |
|---|---|---|
| `--space-0` | 0 | — |
| `--space-1` | 4 | Tight icon padding |
| `--space-2` | 8 | Inline gap, tag padding |
| `--space-3` | 12 | Form control padding |
| `--space-4` | 16 | Body line breaks, button padding |
| `--space-5` | 24 | Card padding, section gaps |
| `--space-6` | 32 | Component padding, between cards |
| `--space-8` | 48 | Section padding |
| `--space-10` | 64 | Section padding (large) |
| `--space-12` | 96 | Hero padding |
| `--space-16` | 128 | Between major sections |

### 6.2 Grid

| Medium | Grid | Max content width | Gutter |
|---|---|---|---|
| Web (desktop) | 12-column | 1280 px | 24 px |
| Web (tablet) | 6-column | — | 16 px |
| Web (mobile) | 4-column | — | 12 px |
| Deck (1920 × 1080) | 12-column | 1680 px (margin 120) | 32 px |
| Documentation | Single column | 720 px reading width | — |
| Print (Letter) | 6-column | 6.5 in | 0.2 in |

### 6.3 Border radius

| Token | Value | Use |
|---|---|---|
| `--radius-sm` | 4 px | Buttons, tags, code blocks, cards |
| `--radius-md` | 6 px | Terminal blocks |
| `--radius-lg` | 8 px | Hero panels |
| `--radius-pill` | 999 px | Status pills only (use sparingly) |

ADDF is a sharp-edged brand. Most surfaces use 4 px. Pill shapes are rare — they signal "live" or "status".

### 6.4 Borders & lines

- Default border: `1 px solid var(--rule)`.
- Strong border: `1 px solid var(--ink)`.
- Subtle divider: `1 px solid var(--mist)`.

No `border-width > 1 px`. No dashed borders except for callouts and "this is annotated" diagrams.

### 6.5 No shadows

ADDF doesn't use drop shadows for elevation. Use borders, color, and spacing instead. The only exception: the terminal block on dark backgrounds can use a single soft shadow to suggest depth: `box-shadow: 0 24px 56px -24px rgba(20,17,13,0.4);`

---

## 7. Iconography

### 7.1 The icon system

Icons are **monoweight outlines**, 1.5 px stroke, drawn on a 24 × 24 grid with 2 px safe padding inside.

| Property | Value |
|---|---|
| Stroke | 1.5 px |
| Stroke color | `currentColor` (inherits text color) |
| Fill | None, except for solid accent dots (yolk) |
| Stroke linecap | Round |
| Stroke linejoin | Round |
| Style | Outline only, never filled |
| Corners | 1 px corner radius minimum |

### 7.2 What we use icons for

- Indicating an action or state (e.g. checkmark, x, arrow).
- Labelling a diagram.
- Marking a list of features.

### 7.3 What we don't use

- **No emoji** in product UI, marketing copy, or documentation. Emoji are not iconography.
- No 3D, isometric, gradient, glow, neon, or "fun" icon sets.
- No icon at a size where the stroke becomes ambiguous (below 16 × 16).
- No icons inside body text. If you wanted an emphasis, italicize.

### 7.4 The arrow

The arrow `→` is the framework's signature icon. It appears on every CTA, every "next step" link, every flow diagram.

- Use the Unicode character `→` (U+2192) when set in type.
- Use a 1.5 px SVG arrow when used as an icon.
- Never use `>` or `>>` or `➔` as substitutes.

---

## 8. Motifs & visual language

ADDF has four recurring visual motifs. They're optional in any single piece — but if you use them, follow the rules.

### 8.1 The dotted grid background

A regular grid of 1 px ink dots, 24 px apart, at 35 % opacity. Used as the texture inside the yolk hero panel and occasionally on Paper.

```css
background-image:
  radial-gradient(circle at 1px 1px, rgba(20,17,13,0.18) 1px, transparent 0);
background-size: 24px 24px;
```

Don't use on cards, buttons, or small surfaces. Only on full-width hero/feature panels.

### 8.2 Circuit traces (from the mark)

Three lines, each with a single 45° bend, terminating in an open ring. They extend backward from anything that represents the framework's compute (the AI, the Builder, the model swap).

Drawn at 7 px stroke (in 280 × 160 viewBox) or scaled accordingly. Always in monochrome — same color as the duck.

### 8.3 The "Quack!" moment

Instrument Serif italic, large size (240 px+ for big closers, 32 px+ for inline). Used at:

- The footer of long documents.
- The empty state of a fresh project.
- The success message after a clean deploy.
- The hero of a celebration page.

**Limit: one Quack! per page.** Two is too many.

### 8.4 The blinking cursor

A 14 × 16 px ink-colored block that blinks at 1.1 s intervals. Used:

- At the end of a terminal block.
- After an in-progress headline that invites action ("Your move ▮").
- In the empty-state of a search bar.

CSS:

```css
.cursor {
  display: inline-block;
  width: 8px; height: 14px;
  background: currentColor;
  vertical-align: -2px;
  animation: blink 1.1s infinite;
}
@keyframes blink { 50% { opacity: 0; } }
```

The cursor reads as *your turn*. Don't use it decoratively.

---

## 9. Imagery & illustration

### 9.1 Default: no imagery

ADDF is a typographic brand. The default treatment for any topic is type, color fields, and the mark. Most pages should have zero photographs and zero illustrations.

### 9.2 When imagery is unavoidable

If a section truly requires imagery (a person, a screenshot, a real-world reference), follow these rules:

- **Screenshots**: actual UI, no fake mockups. Frame in a Paper-warm card with a 1 px Rule border.
- **Photography**: only if approved by brand owner. Warm tones, never cold. Never stock-photo people pointing at laptops.
- **Diagrams**: ours, in our palette, in our type. Don't import generic SVG diagrams from elsewhere.

### 9.3 What we never illustrate

- No anthropomorphized ducks beyond the mark. The duck doesn't have arms, doesn't hold a laptop, doesn't wink.
- No "developer at computer" stock illustrations.
- No isometric tech illustrations.
- No abstract gradient blobs.

---

## 10. Voice & language

### 10.1 Voice in one sentence

**ADDF writes like a senior engineer explaining a process to a peer: declarative, concrete, occasionally wry, never cute.**

### 10.2 The three voice principles

#### Declarative over suggestive

We tell. We don't suggest, recommend, or invite. The framework has opinions; the writing reflects them.

- ✓ *Close the Builder thread between sprints.*
- ✗ *You might want to consider closing the Builder thread between sprints.*

#### Concrete over abstract

Use file names, command syntax, and specific numbers wherever possible. Abstraction is what LLMs do when they don't know enough.

- ✓ *The Architect reads `AGENTS.md`, `STATE.md`, and `DOMAIN.md` at the start of every session.*
- ✗ *The Architect reviews the relevant project context.*

#### Aphoristic when it earns it

Short, balanced, load-bearing lines appear at moments — section openers, hero copy, principle statements. Never on every page.

- *Chat windows are disposable. The files are permanent.*
- *A rubber duck cannot invent your business logic.*

**At most one aphorism per page.** If everything is a slogan, nothing is.

### 10.3 The tone dial

Voice is fixed. Tone moves on a dial.

| Context | Tone | Example |
|---|---|---|
| Hero copy, taglines | Confident, declarative | *Stop vibe coding. Start shipping on purpose.* |
| Documentation body | Patient, concrete, instructional | *Open `SECURITY.md` and write two lists.* |
| Prompts (for the AI) | Imperative, structured, no fluff | *Execute Pre-Flight Dry Run Protocol. Permission Level: 0.* |
| Error messages | Honest, specific, no apology | *Dry run not approved. Builder will not proceed.* |
| The "Quack!" moment | Wry, brief, earned | *Quack!* |
| Internal notes (retros) | Plain, blame-free, factual | *Builder created an empty-title task in Sprint 2. Constraint added.* |

The dial never swings to *jokey*, *corporate*, *salesy*, or *folksy*.

### 10.4 Sentence-level rules

**Length**: mix deliberately. Open sections with short, declarative sentences. Use longer ones to explain. Maximum length: ~32 words.

**Voice**: active by default. Passive when the actor doesn't matter.

**Person**: second (*you*) in docs and walkthroughs. First-person plural (*we*) sparingly. Never first-person singular.

**Tense**: present for behavior. Imperative for instructions. Future only when describing future steps.

### 10.5 Banned words and phrases

These are banned unless quoting or describing genuine uncertainty:

| Banned | Why | Use instead |
|---|---|---|
| *just*, *simply*, *easy*, *easily* | Belittling | Cut entirely |
| *basically*, *essentially*, *literally* | Filler | Cut entirely |
| *kind of*, *sort of* | Hedging | State directly |
| *amazing*, *powerful*, *seamless*, *robust* | Marketing slop | Be specific |
| *unleash*, *supercharge*, *empower*, *delight* | Vendor pitch | Describe the actual outcome |
| *Let's*, *Let me* | Folksy | Use the imperative |
| *magical*, *magic* | Mystifies the work | Describe the mechanism |
| *AI-powered*, *AI-driven* | Hollow | Describe what the AI does |
| *cutting-edge*, *next-gen*, *revolutionary* | Hype | Cut entirely |
| *best practice* | Disguised opinion | *The rule is* / *The convention is* |
| *unlock* | Marketing-speak | Describe the actual capability |

### 10.6 Em dashes are the signature punctuation

We use them. A lot. No spaces around them.

- *A rubber duck — the debugging mascot — sits on a command line.*
- *Architect plans. Builder builds — and stops before changing files.*

Soft ceiling: two em dashes per paragraph.

### 10.7 Italics, bold, exclamation marks

| Mark | Rule |
|---|---|
| *Italics* | For single-word/phrase emphasis. For the framework's serif voice moments. Never whole sentences. |
| **Bold** | For load-bearing terms on first introduction. For step labels in lists. Avoid in body paragraphs. |
| ! | One per page maximum. Almost always *Quack!* |
| ? | Use sparingly. Real questions only — not rhetorical ones. |
| ... | Avoid. We don't trail off. |
| ; | Allowed in prose. Don't use in microcopy. |

---

## 11. Vocabulary

### 11.1 Canonical framework terms

Use these exactly. Capitalization matters.

| Term | Lowercase OK? | Notes |
|---|---|---|
| **Research Mode** | No | Always capitalized. The investigation mode. |
| **Design Mode** | No | Always capitalized. The specification mode. |
| **Develop Mode** | No | Always capitalized. The implementation mode. |
| **Sprint Pack** | No | The three files: `requirements.md`, `blueprint.md`, `acceptance.md`. |
| **Dry Run** | No | Develop Mode's read-only report produced before any implementation. |
| **Permission Level** | No | The 0–4 scale controlling Develop Mode freedom. |
| **The project brain** | Yes | "the project brain" in flowing prose is fine. |
| **Local File Sovereignty** | No | A proper-noun principle. |
| **Context Engineering** | No | A proper-noun principle. |
| **The Reflection Loop** | Yes | Sometimes "the reflection loop" reads better. |
| **The Pivot Protocol** | No | Capitalize the protocol. |
| **vibe coding** | Yes (always lowercase) | The anti-pattern. Lowercase as a deliberate jab. |

### 11.2 File naming conventions

| Type | Convention | Example |
|---|---|---|
| Project brain files | `UPPER_SNAKE_CASE.md` | `STATE.md`, `DOMAIN.md` |
| Sprint folders | `sprint_NNN` | `sprint_001`, `sprint_023` |
| Sprint files | `lowercase.md` | `blueprint.md`, `dry_run.md` |
| Documentation pages | `lowercase.md` | `docs/architecture.md` |
| Templates | `_underscored/` | `_templates/sprint/` |

Always wrap file names in backticks in prose: `STATE.md`, never STATE.md.

### 11.3 Words we avoid

| Word | Why | Use instead |
|---|---|---|
| *AI* alone (in a noun phrase) | Hollow | Specify: *the model*, *the LLM*, or the mode (*Develop Mode*, *Design Mode*) |
| *workflow* | Generic | *lifecycle*, *protocol*, *sprint workflow* |
| *solution*, *platform*, *ecosystem* | Corporate | *framework*, *methodology*, *system* |
| *users* | Distant | *operators*, *developers*, *the human* (vs the AI) |
| *the dev* | Cutesy | *the developer* |

### 11.4 The "Quack!" question

*Quack!* is the framework's signature.

**Use it for:**
- Footer of long-form documents.
- Empty state of a fresh project.
- Success message after a clean deploy.
- Stinger of a release-note title.

**Don't use it for:**
- Error messages.
- Sprint specs, blueprints, acceptance criteria.
- Commit messages.
- More than once per page.

The rule: *Quack!* releases tension. If there's no tension, don't use it.

---

## 12. Microcopy patterns

### 12.1 Buttons & CTAs

Buttons are verbs in the imperative.

| Context | Primary | Secondary |
|---|---|---|
| Marketing hero | *Your first session →* | *$ git clone addf* |
| Docs nav | *Read the docs →* | *View the lifecycle* |
| Sprint completion | *Close the Develop Mode session* | *Open a retrospective* |
| Authorization | *Authorize Permission Level 1* | *Return to Design Mode* |

- No trailing period on buttons. Arrow `→` for forward actions, right side.
- Never *Click here*. Never *Submit*. Be specific.

### 12.2 Empty states

Empty states explain what should be there, and how to put it there. Never apologetic.

- ✓ *No sprints yet. Generate Sprint 001 with the Sprint Pack Generation Prompt.*
- ✗ *Oops! Nothing here yet. Let's create your first sprint!*

### 12.3 Loading states

State the action, not the wait.

- ✓ *Reading `STATE.md`…*
- ✗ *Loading… please wait…*

### 12.4 Error messages

Honest. Specific. Immediately actionable. Never blame the user. Never cute.

- ✓ *Dry run lists files outside `blueprint.md`. The Builder will not proceed. Resolve before authorizing.*
- ✗ *Whoops! Looks like something went wrong. Try again later!*

Format: **what failed → why → what to do.**

### 12.5 Confirmation prompts

State the consequence in plain language.

- ✓ *Authorize Permission Level 3. The Builder may modify files outside the blueprint. Continue?*
- ✗ *Are you sure? This action cannot be undone.*

### 12.6 Success messages

State what happened. Optionally, what's next. *Quack!* allowed here — once.

- ✓ *Sprint 001 closed. `STATE.md` updated. Next: open Sprint 002.*
- ✓ *Deployed. Quack!*

### 12.7 Tooltips

One sentence. No verb in the imperative (tooltips describe, they don't command).

- ✓ *The Builder produces this report before changing any files.*
- ✗ *Click here to see the dry run!*

### 12.8 Form labels and placeholders

- Labels: short, capitalized like a sentence. *Sprint goal*, not *Sprint Goal* or *SPRINT GOAL*.
- Placeholders: example of valid input. *e.g. Build the core task list*, not *Enter a sprint goal here…*
- Helper text: under the field, in Ink Soft.

---

## 13. Application — Website

### 13.1 Structure

A typical ADDF marketing page has at most five sections, in this order:

1. **Hero** — declarative tagline, lede paragraph, one primary + one secondary CTA, terminal block.
2. **Three principles** — three columns, eyebrow + Instrument Serif headline + body.
3. **The lifecycle** — the 8-step circular diagram, dark panel, yolk highlights.
4. **The dual-mode model** — two columns, Architect vs Builder, with bullet lists.
5. **CTA closer** — yolk panel, big *Quack!*, link to the docs.

No section is optional in the marketing hero. No section is permitted that isn't on this list without brand-owner approval.

### 13.2 Header / nav

```
[ADDF mark + wordmark]    Framework  Lifecycle  Prompts  Templates  GitHub    [Read the docs →]
```

- Sticky on scroll. Background goes from transparent to Paper with a Mist 1 px bottom border.
- Nav links: Space Grotesk, 13.5 px, Ink Soft. Hover → Ink.
- CTA: Ink fill, Paper text, 4 px radius.

### 13.3 Hero

- Background: Paper (default) or Yolk (when extra emphasis is needed).
- Eyebrow above the headline, Mono uppercase with a leading 28 px line.
- Headline: Instrument Serif, 88–96 px, line-height 1.05–1.1.
- Lede: Space Grotesk, 20 px, Ink Soft, max-width 620 px.
- CTAs: one primary (Yolk), one secondary (transparent with Ink border).
- A terminal block sits below — Ink background, Mono text, blinking cursor at the end.

### 13.4 Body sections

- Eyebrow + H2 in a section-head with a 1 px Rule border-bottom.
- Right side of the section-head: a short descriptive paragraph in Ink Soft, max-width 320 px.
- Body content in cards (4 px radius, 1 px Rule border, Paper-warm fill for accent cards).

### 13.5 Footer

- Background: Yolk.
- Massive *Quack!* in Instrument Serif italic, 200 px+.
- Below: meta line in Mono uppercase — file references, version, link to GitHub.

### 13.6 Responsiveness

| Breakpoint | Behavior |
|---|---|
| ≥ 1280 px | Full 12-column layout. |
| 960–1279 px | Section padding reduces from 96 → 64. Hero headline 72 px. |
| 640–959 px | Single column. Cards stack. Nav collapses behind a Mono "menu" link. |
| < 640 px | Single column. Hero headline 48 px. Eyebrows preserved. |

Mobile menu is a full-screen Ink overlay with Mono links. Never a hamburger icon.

---

## 14. Application — Slide decks

### 14.1 Frame

- Aspect: 16 : 9, 1920 × 1080 px.
- Outer margin: 120 px on each side.
- Header band: 60 px high, Ink on Paper or Paper on Ink. Contains slide number (Mono) and slide title (Mono).
- Footer band: 40 px high. Contains the mark (24 px), the section name (Mono), and the page number.

### 14.2 Slide templates

| Type | Composition |
|---|---|
| **Title slide** | Full-bleed Yolk panel. Stacked lockup centered. Below: deck name in Instrument Serif, 96 px. Date and audience in Mono uppercase. |
| **Section divider** | Full-bleed Ink panel. Eyebrow + Instrument Serif headline (top-left aligned), large *Quack!* (bottom-right, optional). |
| **Content slide** | Paper background. Eyebrow + H2 at top. Body content below. One image or chart maximum per slide. |
| **Code slide** | Ink panel. Mono code in Paper. Yolk highlighting on key lines. |
| **Quote slide** | Paper background. Instrument Serif italic quote at 80–100 px. Attribution in Mono uppercase below. |
| **Closing slide** | Yolk panel. Big *Quack!* in Instrument Serif italic. CTA in Mono below. |

### 14.3 Slide copy rules

- One idea per slide. If you have two ideas, you have two slides.
- Max six bullets per slide. Each bullet ≤ 12 words.
- Body type minimum: 24 px. Headline minimum: 48 px.
- Speaker notes are full scripts, conversational. The slide itself stays sparse.

### 14.4 Don't

- ✗ Don't put the agenda on every slide.
- ✗ Don't use slide transitions beyond a hard cut.
- ✗ Don't animate anything except a cursor on a terminal slide.
- ✗ Don't use stock photography or clipart.
- ✗ Don't put more than one *Quack!* in a deck.

---

## 15. Application — Documentation

### 15.1 Page structure

Every doc page follows this rhythm:

1. **Title** (H1, Instrument Serif).
2. **One-sentence summary** (Lede, Space Grotesk 18 px).
3. **Table of contents** (if the page is longer than 3 sections).
4. **The why** (a 2–4 sentence justification).
5. **Sections** (each with: opener → how → rule → example).
6. **The rule** (bold or *italic* paragraph stating the non-negotiable).
7. **Worked example** (real code, real files).
8. **Footer** (optional *Quack!*, version, last reviewed).

### 15.2 Code blocks

```css
font-family: "JetBrains Mono", monospace;
font-size: 14px;
line-height: 1.7;
padding: 22px 26px;
background: var(--ink);
color: var(--paper);
border-radius: 6px;
```

- Comments in `rgba(246,241,228,0.45)`.
- Prompts (`$`, `>`) in Yolk.
- Highlighted lines: left border 3 px Yolk.

Inline code: 0.92× of body size, `rgba(20,17,13,0.06)` background, 2 px radius, 2 px horizontal padding.

### 15.3 Callouts

Three types only:

| Type | Format |
|---|---|
| **Rule** | Left border 4 px Yolk, Paper-warm fill, bold "Rule:" prefix in Ink. |
| **Note** | Left border 4 px Mist, Paper fill, no prefix. |
| **Caution** | Left border 4 px Beak, Paper-warm fill, bold "Caution:" prefix. |

Never use color-coded full-fill callouts. Never use emoji icons in callouts.

### 15.4 Diagrams

- Drawn in the brand palette. Built in SVG when possible (PNG fallback acceptable for export).
- Type labels in Mono.
- Connecting lines: 1.5 px Ink. Yolk only for the "highlighted path" through a diagram.
- One diagram per concept. Don't overlay multiple concepts.

### 15.5 Tables

- Header row: Paper-warm fill, Mono uppercase 11 px, Ink Soft text.
- Body rows: alternating Paper / Paper-warm if needed for legibility (long tables only).
- Cell padding: 18 px vertical, 28 px horizontal.
- No vertical grid lines. Horizontal: 1 px Rule between rows.

---

## 16. Application — Marketing & social

### 16.1 Social post templates

| Network | Template |
|---|---|
| X / Bluesky | Card image (1200 × 675) with Instrument Serif headline + Mono eyebrow. Body text is the aphorism. |
| LinkedIn | Same image format. Body text is a 2–4 paragraph essay in the framework voice. |
| GitHub README | See §17. |

### 16.2 Image cards (1200 × 675)

- Yolk or Paper background.
- 80 px outer padding.
- Mono eyebrow in upper-left.
- Instrument Serif headline, max 12 words.
- Mark + wordmark in lower-left.
- No additional decoration.

### 16.3 Newsletter / release notes

- Subject line: declarative + version. *Sprint 12 — Token budget for retros.*
- Opening line: the aphorism or the upshot in one sentence.
- Body: bullet list of changes, each starting with a verb in past tense. *Added*, *Fixed*, *Removed*, *Renamed*.
- Closer: *Quack!* if the release is a milestone. Plain if it's a minor.

### 16.4 What we never publish

- Listicles ("5 things…").
- Promotional countdowns.
- "We're hiring!" decorative posts.
- Anything with stock emojis as bullets.

---

## 17. Application — Code, repos & READMEs

### 17.1 README structure

```markdown
# ADDF — Project Name

One-sentence description of what this project is.

> An aphorism if the project warrants one. Optional.

## What this is

2–4 sentence explanation.

## Getting started

```
mkdir project-name
cd project-name
git init && git checkout -b main && git checkout -b dev
```

## The project brain

List of the foundational `.md` files in this project.

## Lifecycle phase

Which of the 8 ADDF lifecycle phases the project is currently in.

## Operating modes in use

Which modes (Mode 1–5, Parallel) the team uses.

## License

…

*Quack!*
```

### 17.2 Commit messages

[Conventional Commits](https://www.conventionalcommits.org/) format, with no embellishment:

```
feat(sprint-007): add cross-sprint consistency audit prompt
fix(builder): reject empty-title task creation on keyboard submit
refactor(architect): split blueprint generation into two passes
chore(brain): update STATE.md after Sprint 12 close
docs(style): add §14 deck application guidance
```

No emoji. No exclamation marks. No personal pronouns. Past tense or imperative — be consistent within a repo.

### 17.3 Branch names

`sprint/NNN-short-description`

Examples: `sprint/001-core-task-list`, `sprint/014-cli-multiplex`.

### 17.4 Issue and PR templates

- Title: declarative, ≤ 60 chars.
- Body: structured sections — *Context*, *What changed*, *Verification*, *Out of scope*.
- No "thanks!" footers, no signature blocks.

---

## 18. Asset library

All assets live in `assets/` at the project root.

| Path | What |
|---|---|
| `assets/duck-logo.png` | Yolk duck on transparent. 676 × 409, ready for any Paper/Ink/Pond background. |
| `assets/duck-logo-ink.png` | Ink duck on transparent. For Yolk backgrounds. |
| `assets/duck-logo-paper.png` | Paper duck on transparent. For high-contrast use on Ink/Pond. |
| `assets/duck-logo.svg` | (Pending) Vector master. |
| `Brand Identity.html` | The visual brand book. Refer to this for layout, motif, and color application examples. |

### 18.1 CSS token export

Drop this into the root of any web project:

```css
:root {
  --yolk: #F5C518;
  --yolk-deep: #E2B00B;
  --ink: #14110D;
  --ink-soft: #2A2620;
  --paper: #F6F1E4;
  --paper-warm: #EFE7D2;
  --pond: #1B4D3E;
  --beak: #E89A1F;
  --mist: #E6DFCB;
  --rule: #DDD2B5;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-8: 48px;
  --space-10: 64px;
  --space-12: 96px;
  --space-16: 128px;

  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 8px;
}
```

---

## 19. Pre-publish checklist

Before any external-facing artifact (website page, deck, doc, social post, README) ships:

### Visual
- [ ] All colors from the palette in §4. No custom hex values.
- [ ] Type uses only the three families in §5. Sizes match the hierarchy table.
- [ ] No drop shadows, gradients, glows, or outlines on text or mark.
- [ ] Mark on a solid color field, with clear space, at or above minimum size.
- [ ] No emoji in body, headings, or buttons.

### Language
- [ ] No banned words (§10.5).
- [ ] All framework terms use canonical capitalization (§11).
- [ ] All file names in backticks.
- [ ] Em dashes — not hyphens or commas — for asides.
- [ ] At most one *Quack!* on the page or in the deck.
- [ ] At most one aphorism per page.
- [ ] Every doc section has a rule (§15).

### Structure
- [ ] Hero → principles → lifecycle → dual-mode → CTA order is preserved on marketing pages.
- [ ] One idea per slide on decks.
- [ ] README follows the structure in §17.

### Smell test
- [ ] Read it aloud. Does it sound like a senior engineer talking to a peer? If it sounds like marketing or like a stand-up bit, rewrite.
- [ ] Does the page need the duck? If no — leave it off. The duck is precious by being rare.

If any box is unchecked, the artifact is not ready.

---

## 20. Glossary

| Term | Definition |
|---|---|
| **Research Mode** | The investigation mode. Gathers evidence, surfaces unknowns, identifies risks. Does not decide or build. |
| **Design Mode** | The specification mode. Writes Markdown project memory — sprint packs, decisions, docs, retrospectives. Does not write implementation. |
| **Develop Mode** | The implementation mode. Modifies approved files after Dry Run approval. Does not self-authorize. |
| **Sprint Pack** | The three files defining a sprint: `requirements.md`, `blueprint.md`, `acceptance.md`. |
| **Dry Run** | Develop Mode's read-only report listing every file it intends to create, modify, move, or delete — produced before any implementation begins. |
| **Permission Level** | The 0–4 scale controlling Develop Mode freedom. |
| **The project brain** | The local Markdown files holding project memory. |
| **Mark** | The duck-and-traces logo. |
| **Lockup** | The mark in combination with the wordmark. |
| **Wordmark** | The "ADDF" or full-name text logo, in Instrument Serif. |
| **Eyebrow** | A small Mono uppercase label above a headline. |
| **Aphorism** | A short, balanced, memorable line. Limited to one per page. |
| **The rule** | The non-negotiable in any documentation section. |
| **Quack!** | The framework's signature stinger. One per page, max. |

---

*ADDF · `STYLE_GUIDE.md` · v1.0 · maintained as part of the project brain*

*Quack!*
