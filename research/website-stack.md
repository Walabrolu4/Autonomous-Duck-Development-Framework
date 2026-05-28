# Research — Website Stack

**Question:** Q003 — Static Website Only  
**Mode:** Research Mode  
**Date:** 2026-05-28  
**Status:** Complete — no decision made

---

## What Q003 is actually asking

Q003 has two sub-questions bundled together:

1. Should the v0.2 website be built static-only, or does it need server-side behavior?
2. Are the v0.2 website and v0.4 onboarding app separate deployments, or the same deployment with a static-first phase?

These are related but distinct. Research is organized around both.

---

## What the requirements say

### v0.2 website (requirements §8, §21)

The requirements explicitly describe v0.2 as:

```txt
Static website
Homepage
Start Here page
Framework page
Scale Model page
Lifecycle page
Modes page
Project Brain page
Starter Kit page
Prompt Catalog page
Examples page
Downloads page
```

Goal: "A visitor can learn and download from a clean public site."

None of the v0.2 pages require a server. The download section provides pre-built static file assets (ZIPs, PDFs, Markdown). All content is authored and pre-rendered.

### v0.4 onboarding app (requirements §14)

The requirements describe the onboarding app as:

- browser-based,
- "generate files client-side if possible" (§14.3 — already answered by the requirements),
- "The first onboarding app must not send project details to a backend" (§14.4).

The app flow is: questionnaire → file preview → ZIP download → copy Design Mode prompt. All of this is client-side JavaScript. No server is required.

**Implication:** the onboarding app is not a "dynamic" feature in the server-side sense. It is an interactive client-side JavaScript component — a rich island of behavior in an otherwise static site.

---

## Framework options

### Option A — Astro

Astro is the current default for documentation and content-driven sites in 2026. It shipped Astro 6 in February 2026 following a Cloudflare acquisition in January 2026. It has 59,000+ GitHub stars and 2.7M weekly npm downloads.

Relevant characteristics:

- Ships zero JavaScript to the browser by default. Pages are HTML.
- Islands architecture: interactive React/Vue/Svelte/Solid components can be embedded in otherwise static pages and hydrated only when needed.
- Native Markdown/MDX content collections with fast incremental builds.
- Official integrations for GitHub Pages and Netlify. GitHub Actions deployment in a few lines of config.
- Lighthouse 100 is realistic for content pages.
- A questionnaire-driven file generator (the v0.4 app) is a natural fit as an Astro island — one interactive component on an otherwise static `/onboarding` page.

Fit for ADDF:
- v0.2: static Astro site, all pages pre-rendered, no JavaScript in the browser for content pages.
- v0.4: one or more interactive islands added to the existing site. No new deployment, no new host, no rewrite.

Risks:
- Learning curve if contributors are not already familiar with Astro. However, Astro's `.astro` file format is close enough to HTML + JavaScript imports that onboarding is fast.
- Cloudflare acquisition (Jan 2026) is recent. The framework remains MIT-licensed and open source, but long-term governance is uncertain. This is a low-probability risk for a project that generates static HTML.

### Option B — Next.js

Next.js can export fully static sites with `output: 'export'`. It also supports server-side rendering, incremental static regeneration, edge functions, and full dynamic routing.

Relevant characteristics:

- Significantly more JavaScript in the browser than Astro. The React runtime alone adds overhead that Astro avoids for static pages.
- Excellent if you need to add server-rendered pages later (e.g., analytics API, form handlers, user accounts). ADDF has no such plans.
- Larger configuration surface, more dependencies.
- Used by many documentation sites, but recommended primarily when static and dynamic pages need to coexist in the same codebase at scale.

Fit for ADDF:
- v0.2 would work, but v0.2 requires nothing that justifies the overhead.
- v0.4 onboarding app is client-side only — Next.js server features are not needed.
- Over-specified for this use case.

### Option C — Plain HTML / CSS

A static site written in raw HTML, CSS, and minimal JavaScript. No build step for content pages.

Relevant characteristics:

- Simplest possible setup. No dependency chain. No framework lock-in.
- No build tooling to maintain or upgrade.
- Adding interactive behavior (the v0.4 app) requires hand-rolling the JavaScript or bringing in libraries ad hoc.
- No component reuse across pages — navigation, header, footer, and shared layout would need to be duplicated or templated with a minimal preprocessor.
- No Markdown-to-HTML pipeline. The full manual is long-form Markdown content. Hand-converting it is error-prone and hard to maintain.

Fit for ADDF:
- Viable for v0.2 if the site is truly minimal (3–4 pages). Not viable at the documented page count (13+ required pages in §8.2).
- The v0.4 onboarding app could still be built as a vanilla JS module in this setup, but integration into the site's layout would need manual work.

### Option D — Hugo

Hugo is the fastest static site generator by build time. It is widely used for documentation sites.

Relevant characteristics:

- Go-based, no Node.js required for builds.
- Excellent for pure content sites. Its template language (Go templates) is unfamiliar to most JavaScript developers.
- Adding client-side JavaScript components (the v0.4 app) is possible but Hugo provides no native component model. JavaScript is embedded manually.
- Strong choice if the team is already Go-fluent. Unusual choice otherwise.

Fit for ADDF:
- Viable for v0.2. Not recommended for v0.4 integration without additional JavaScript tooling.

---

## Client-side ZIP generation (the onboarding app's core technical need)

The v0.4 onboarding app needs to:

1. Collect operator answers.
2. Generate Markdown file content from templates.
3. Bundle the files into a downloadable ZIP.

This is fully solvable client-side in 2026:

**JSZip** (current: v3.10.1) — creates, reads, and edits ZIP archives in the browser via a JavaScript API. Well-established, widely used. Requires FileSaver.js (or `URL.createObjectURL`) to trigger the browser download.

**client-zip** — lightweight alternative (6.4 kB minified, 2.6 kB gzipped). Dependency-free. Reported as approximately 40x faster than JSZip for large archives. Uses streaming ZIP generation.

Both libraries work in all modern browsers and require no server involvement. The generated ZIP never leaves the operator's browser. This aligns directly with the requirements (§14.3: "avoid collecting sensitive data"; §14.4: "must not send project details to a backend").

---

## Deployment options

### GitHub Pages

- Free for all public repositories, no tiers, no billing.
- Zero-config for static sites already on GitHub — enable it in repository settings.
- GitHub Actions deploy pipeline is official and well-documented for both Astro and plain HTML.
- Purely static — no serverless functions, no edge functions, no form processing.
- Soft bandwidth limit: 100 GB/month. Sufficient for an open-source documentation site in early life.
- Repository size cap: 1 GB. Not a concern for Markdown + ZIP assets.
- The onboarding app being client-side only means this is not a limitation for v0.4.

Fit for ADDF: strong. The site is fully static. The onboarding app is client-side. GitHub Pages covers both without any hosting cost.

### Netlify (free tier)

- 100 GB bandwidth/month, 300 build minutes/month, 125,000 serverless function invocations.
- Preview deployments for every pull request — useful for reviewing content changes.
- Native Astro support with official adapter.
- Form handling built in (not needed for ADDF — no user submissions).
- More dashboard overhead than GitHub Pages.

Fit for ADDF: viable. Preview deployments are the primary advantage over GitHub Pages. No server features are needed, so the serverless function allowance is unused capacity.

### Vercel

- Very similar to Netlify. Originally built around Next.js; has strong Astro support.
- Free for hobby/open-source projects.
- Preview deployments per branch.

Fit for ADDF: viable. No advantage over Netlify for this use case.

---

## The one-vs-two deployment question

The core question in Q003's second sub-question is whether v0.2 and v0.4 should be:

**Path 1 — Same deployment (v0.2 grows into v0.4)**
Build v0.2 in Astro. When v0.4 is ready, add an interactive island (React or Svelte component) to a `/get-started` or `/setup` page. The onboarding app lives at a route within the existing site. One repository, one deployment, one domain.

Tradeoffs:
- The v0.4 work is additive — no migration, no domain change, no new infrastructure.
- The onboarding app shares the site's navigation, branding, and download links automatically.
- Risk: if the site framework choice turns out to be wrong for v0.4, it cannot be changed without rewriting v0.2 content.
- Requires the v0.2 framework to support client-side JavaScript islands without a full rewrite.

**Path 2 — Separate deployments**
Build v0.2 as a static site (any stack). Build v0.4 as a separate app (separate repo, separate host, separate subdomain). They are different URLs.

Tradeoffs:
- v0.2 framework choice has no consequences for v0.4.
- v0.4 can be built with whatever stack is most appropriate for a wizard-style interactive app (plain HTML + vanilla JS, Vue, Svelte, React).
- Maintaining two deployments, two domains, and two codebases adds overhead.
- User experience requires navigating across domains (e.g., `addf.io` → `app.addf.io`).

---

## What the requirements imply but do not state

The requirements say the onboarding app is the "browser-based version of the init tool" (§14.1) — it is described as parallel to the CLI, not as a separate web product. This framing suggests the intent is a single site with a section for the onboarding app, not a separate product.

The requirements also describe an "Onboarding App" page in the site information architecture (§8.2) under "Optional later pages" — implying a page within the existing site, not an external URL.

Neither of these points is a decision. They are observations about the requirements as written.

---

## Open questions this research cannot answer

The following would need a human decision before the website sprint can be planned:

1. **Framework preference.** Is there an existing framework preference in the project? If the operators and contributors are JavaScript developers, Astro is the natural pick. If there is a strong preference for plain HTML, that changes the v0.4 integration story.

2. **Domain and hosting account.** GitHub Pages hosting is decided by the repository host (GitHub). Netlify or Vercel require a separate account and DNS configuration. Where will the domain be managed?

3. **One-vs-two deployment.** This is the open decision in Q003. The research above identifies the tradeoffs; it does not resolve them.

4. **v0.4 timeline relative to site stability.** If v0.4 follows quickly after v0.2, the one-deployment path has lower switching cost. If v0.4 is 12+ months after v0.2, the separate deployment path becomes more defensible.

---

## Summary of findings

| Topic | Finding |
|---|---|
| Does v0.2 need a server? | No. All v0.2 content is static. |
| Does v0.4 need a server? | No. Requirements explicitly say "generate files client-side if possible" and prohibit sending data to a backend. |
| Is client-side ZIP generation viable? | Yes. JSZip and client-zip are mature, browser-native, no server required. |
| Best framework for v0.2 content site (2026)? | Astro — ships zero JS by default, islands for later interactivity, fast builds, official GitHub Pages/Netlify support. |
| Can v0.2 and v0.4 share a deployment? | Yes — Astro islands architecture supports adding interactive components to a static site without a new deployment. |
| Can v0.2 be on GitHub Pages? | Yes. GitHub Pages is free, supports Astro, and the site is fully static. |
| Does the onboarding app require Netlify/Vercel? | No. Client-side file generation works on GitHub Pages. |

---

*ADDF · `research/website-stack.md` · Research Mode · 2026-05-28*
