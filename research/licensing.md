# Research — Licensing

**Question:** Q001 — License  
**Mode:** Research Mode  
**Date:** 2026-05-28  
**Status:** Complete — no decision made

---

## What Q001 is asking

ADDF needs a license before v0.1 public release. The project contains multiple content types that may warrant different licenses:

- Framework specification and documentation (manual, website content, wiki docs)
- Code (CLI init tool, web onboarding app)
- Starter kit template files (operators copy these into their own projects)
- Prompt catalog (methodology text, operators load these into AI sessions)
- Example projects (worked Mini Task Tracker files)

The three options raised in Decision 006 are:

| Option | Code | Documentation |
|---|---|---|
| A | MIT | CC BY 4.0 |
| B | Apache 2.0 | CC BY 4.0 |
| C | MIT (uniform) | MIT (uniform) |

This research examines each option and surfaces an additional consideration not in the original list.

---

## The licenses explained

### MIT

A short permissive license originating at MIT in the late 1980s. Allows any use, modification, and distribution — including commercial and proprietary — provided the copyright notice and license text are included in any copy or substantial portion.

Requirements on users: keep the copyright notice and license text.  
Patent coverage: none explicit. Users rely on implied patent licenses, which are weaker and jurisdiction-dependent.  
Compatibility: compatible with almost everything.

### Apache 2.0

A permissive license similar to MIT but longer and more explicit. Adds two things MIT does not have:

1. **Explicit patent grant.** Contributors grant users a license to any patents they hold that are necessarily infringed by the work. This is written into the license text, not implied.
2. **Patent retaliation clause.** If a licensee initiates patent litigation asserting that the licensed work infringes a patent, their patent license terminates. This deters patent trolling.

Requirements on users: keep copyright and license notices; include the `NOTICE` file if the project has one; state significant changes made.  
Compatibility: compatible with MIT, but projects under Apache 2.0 cannot be relicensed to MIT without dropping the patent clauses.

### CC BY 4.0

Creative Commons Attribution 4.0 International. A license designed for creative works — documentation, images, writing, data — not software code. Permits any use and adaptation including commercial, with one requirement: attribution (credit the author, link the license, indicate changes).

CC explicitly recommends against using CC licenses for software code. The license does not address patent rights, which makes it inappropriate for code. It is the standard choice for specification text, documentation, educational materials, and framework methodology.

In the developer ecosystem: Semantic Versioning (semver.org) is licensed CC BY 4.0. Earlier versions were CC BY 3.0.

Requirements on users: attribution when distributing or adapting the work.

### MIT-0 (not in original options — surfaced by research)

"MIT No Attribution" — a variant of MIT that removes the attribution requirement entirely. Purpose-built by AWS for code that is intended to be used as reference, teaching samples, examples, or templates that developers will copy and modify. No license notice needs to be kept.

Relevant to ADDF because starter kit files are specifically designed to be copied into operator projects. If those files carry a standard MIT notice, operators must technically preserve that notice in their own repositories — adding clutter to files that exist to serve the operator's project, not ADDF's.

MIT-0 is OSI-approved (Open Source Initiative).

### CC0

Public domain dedication. The author waives all rights to the maximum extent possible. No attribution required. No conditions on use.

Used by some projects for template content and sample files. GitHub's own license-templates repository releases templates under CC0. More aggressive than MIT-0 — the author gives up the ability to assert copyright entirely.

---

## How comparable projects license their content

| Project | Type | License |
|---|---|---|
| Semantic Versioning (semver.org) | Specification text | CC BY 4.0 |
| Conventional Commits | Specification + implementation repo | MIT (full repository) |
| Keep a Changelog (keepachangelog.com) | Methodology documentation | MIT |
| GitHub license-templates | Template files | CC0 |

Pattern observed: projects that are primarily methodology specifications tend to use CC BY for the specification text. Projects that have implementation code tend to apply MIT uniformly for simplicity. Template files intended for copying are sometimes CC0 to remove attribution friction.

---

## Content type analysis for ADDF

ADDF contains four distinct content types. Each has a different relationship with the license:

### 1. Framework documentation

The full manual, website content, wiki docs, diagrams, README. This is the specification and explanation of the methodology.

Operators read this content. They do not copy it into their own projects. Attribution requirements are reasonable — if someone republishes or adapts the manual, crediting ADDF is appropriate.

Suitable licenses: CC BY 4.0 (standard for this content type), MIT (simpler, uniform).

### 2. Code

The CLI init tool (v0.3) and the web onboarding app (v0.4). These are software artifacts.

Operators use the tools. They do not typically copy the tool source code into their own projects. Attribution requirements are standard for open source code.

CC licenses are explicitly inappropriate for code. MIT or Apache 2.0 are the right choices.

Difference between them for ADDF specifically: the patent clause in Apache 2.0 matters if the project owner or contributors hold software patents, or if ADDF's methodology is ever argued to infringe existing patents. For a small open-source methodology framework with no patent portfolio, this is a low-probability concern. Apache 2.0 provides better protection if the project grows and attracts contributors who may hold patents.

### 3. Starter kit template files

`starter-kit/blank/` and `starter-kit/example-filled/` — the files operators copy into their own repositories and then fill in with their own project details.

This is the most distinctive content type. Unlike documentation (read but not copied) or code (run but not copied), starter kit files are explicitly designed to be copied wholesale. After copying, they become the operator's own project brain files. The `AGENTS.md` in an operator's project is theirs, customised to their project, with ADDF's content replaced.

If starter kit files are MIT-licensed, operators must technically preserve the copyright notice in every file — even after replacing all the content with their own project's information. This creates friction.

If starter kit files are MIT-0 or CC0, operators have no obligations after copying. The files become fully theirs.

This distinction is not covered by Options A, B, or C in Decision 006. It is an additional question: whether the starter kit gets its own license tier.

### 4. Prompt catalog

The prompt files in `prompts/`. Operators copy these and paste them into AI session interfaces. They also load them into context. Some prompts may be shared with collaborators.

Prompts are methodology text — closer to documentation than code. However, like starter kit files, they are designed to be copied and reused. If they carry CC BY attribution requirements, an operator sharing their prompts with a colleague is technically required to include a credit to ADDF.

MIT-0 or CC0 would remove this friction. CC BY 4.0 would preserve attribution requirements.

---

## The attribution friction question

Whether attribution requirements on starter kit files and prompts constitute meaningful friction depends on how ADDF is used.

**If most operators are individuals or small teams** using ADDF privately or in their own repositories: a copyright notice in a file they copy and customise is low friction. They will likely ignore it or remove it without thinking about license implications.

**If ADDF is adopted by organizations or consultancies** who use ADDF templates commercially or redistribute adapted versions: CC BY 4.0 attribution on documentation is appropriate and signals that the methodology has an author. MIT-0 on templates removes the friction for code-adjacent files.

**If prompt catalog files are shared or published** (e.g., operators who write about their ADDF usage and share their prompts publicly): CC BY 4.0 would require them to credit ADDF, which is reasonable for a publicly distributed methodology. MIT-0 would not require it.

---

## Summary of options with complete analysis

### Option A — MIT (code) + CC BY 4.0 (docs)

Applies MIT to: CLI tool, web onboarding app.  
Applies CC BY 4.0 to: manual, website content, diagrams, prompts, starter kit files.

Pros:
- Standard pattern for frameworks that contain both code and methodology content.
- CC BY 4.0 ensures attribution when the manual or prompts are adapted and republished.
- Well-understood by contributors and adopters.

Cons:
- CC BY 4.0 on starter kit files means every operator who copies the files inherits an attribution obligation. The files are designed to be customised into the operator's own project, which makes carrying attribution requirements awkward.
- Requires two license files or clear documentation of which license applies where.
- CC BY is not OSI-approved for code — must be clearly scoped to non-code content.

### Option B — Apache 2.0 (code) + CC BY 4.0 (docs)

Same as Option A except Apache 2.0 replaces MIT for code.

Additional pros over Option A:
- Explicit patent grant protects users of the CLI and onboarding app.
- Patent retaliation clause deters bad-faith litigation.
- Better choice if contributors may hold patents.

Additional cons over Option A:
- Apache 2.0's `NOTICE` file requirement adds maintenance overhead.
- More complexity for early-stage project. Most ADDF users are small operators unlikely to benefit from the patent clause.

### Option C — MIT (uniform, all content)

Applies MIT to everything: code, documentation, starter kit files, prompts.

Pros:
- Single license. No decision required about which content belongs to which license.
- MIT is universally understood.
- Conventional Commits and Keep a Changelog both use this approach successfully.

Cons:
- MIT technically requires keeping copyright notices in every copied file. Starter kit files will be copied and customised — the notice will either be preserved without purpose or removed without legal clarity.
- MIT is not designed for creative/documentary content. It works, but CC BY 4.0 is a cleaner signal that the content is methodology, not software.

### Option D — MIT (code) + CC BY 4.0 (docs) + MIT-0 (starter kit and prompts)

Not in the original options. Surfaced by this research.

Applies MIT to: CLI tool, web onboarding app.  
Applies CC BY 4.0 to: manual, website content, wiki documentation, diagrams.  
Applies MIT-0 to: starter kit files, prompt catalog.

Pros:
- Starter kit files and prompts are explicitly no-obligation. Operators can copy, customise, and share them without any license compliance requirement.
- Framework documentation retains attribution requirements for adaptation and republication.
- Code retains a standard permissive license.
- MIT-0 is OSI-approved and designed precisely for this use case (template code intended for copying).

Cons:
- Three license tiers adds explanation overhead. The repository needs clear documentation of which files fall under which license.
- Less common pattern — contributors may not be familiar with MIT-0.
- Requires a `LICENSE` file that clearly maps content types to licenses, or separate license files per directory.

---

## Open questions this research cannot answer

1. **Does the project owner want attribution when prompts or starter kit files are republished?** If yes, CC BY 4.0 on prompts is appropriate. If no, MIT-0 or CC0 is cleaner.

2. **Is patent protection a meaningful concern?** Apache 2.0 over MIT matters only if contributors may hold patents or if the project anticipates patent risk. For a small framework, this is a low-probability scenario but not zero.

3. **How will the `LICENSE` file be structured?** A multi-license project needs a clear statement of which license applies where, either in `LICENSE`, `README.md`, or both.

4. **Should starter kit files carry any notice at all?** Even MIT-0 or CC0 files can carry a comment pointing to the ADDF website without creating legal obligations. This is a question of how much ADDF wants to be credited in the files operators use day-to-day.

---

## Summary table

| Option | Code | Docs | Starter kit + Prompts | Complexity | Attribution on templates |
|---|---|---|---|---|---|
| A | MIT | CC BY 4.0 | CC BY 4.0 | Two licenses | Yes — required |
| B | Apache 2.0 | CC BY 4.0 | CC BY 4.0 | Two licenses | Yes — required |
| C | MIT | MIT | MIT | One license | Yes — technically required |
| D (new) | MIT | CC BY 4.0 | MIT-0 | Three licenses | No — not required |

---

*ADDF · `research/licensing.md` · Research Mode · 2026-05-28*
