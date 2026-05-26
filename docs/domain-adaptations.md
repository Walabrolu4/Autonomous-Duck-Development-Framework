# Domain Adaptations

ADDF is domain-agnostic — the structure stays stable and the domain files adapt.

## Table of contents

1. [Web applications](#web-applications)
2. [Game development](#game-development)
3. [Desktop applications](#desktop-applications)
4. [Data and automation](#data-and-automation)
5. [Documentation and framework projects](#documentation-and-framework-projects)

---

## Web applications

Web application projects use the standard ADDF structure with entities and commands typical to web development.

Typical entities in `DOMAIN.md`:

- routes,
- pages,
- components,
- API endpoints,
- sessions,
- database tables,
- forms,
- permissions.

Typical `COMMANDS.md` entries:

```
npm run dev
npm run test
npm run build
npm run lint
```

**Rule:** Keep the structure stable. Adapt the domain files.

---

## Game development

Game projects use `DOMAIN.md` as a technical game design document — it captures game states, player mechanics, and scene flow that would otherwise be scattered across design documents.

Typical entities in `DOMAIN.md`:

- scenes,
- levels,
- game states,
- player states,
- input actions,
- assets,
- UI screens,
- save data.

The `COMMANDS.md` file captures engine-specific build, test, and export commands. The `SECURITY.md` file defines which asset files are safe to reference in sessions and which contain licensed content that must not be shared.

**Rule:** Keep the structure stable. Adapt the domain files.

---

## Desktop applications

Desktop application projects must account for system permissions, OS-specific behaviors, and local file access patterns — all of which belong in `DOMAIN.md` and `SECURITY.md`.

Typical entities in `DOMAIN.md`:

- windows,
- menus,
- local files,
- system permissions,
- user settings,
- native services.

**Rule:** Keep the structure stable. Adapt the domain files.

---

## Data and automation

Data and automation projects model the transformation pipeline in `DOMAIN.md`. The domain entities are data structures, not user-facing features — and the acceptance criteria in sprint packs tend to focus on output correctness and idempotency.

Typical entities in `DOMAIN.md`:

- input files,
- output files,
- rows,
- transformations,
- validations,
- schedules,
- error records.

**Rule:** Keep the structure stable. Adapt the domain files.

---

## Documentation and framework projects

Projects that produce documentation, frameworks, or developer tools — like ADDF itself — use the same structure but with entities that reflect the deliverables rather than a running application.

Typical entities in `DOMAIN.md`:

- pages,
- sections,
- templates,
- prompts,
- examples,
- downloads,
- versions,
- release packages.

For a concrete example, the ADDF public repository itself uses ADDF for all development. See [Examples](examples.md) for a walkthrough.

**Rule:** Keep the structure stable. Adapt the domain files.

---

[← Wiki Home](index.md) · ADDF v3.5
