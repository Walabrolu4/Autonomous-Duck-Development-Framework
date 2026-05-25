[Home](index.md)

# Domain Adaptations

## How the Framework Adapts

The ADDF framework structure is identical across all project types. What changes is the content of the key files — specifically `DOMAIN.md`, `COMMANDS.md`, and `STYLE_GUIDE.md`. The Architect Mode / Builder Mode separation, the dry run gate, the sprint workflow, and the permission levels work the same way regardless of the domain. You do not adapt the process; you adapt what you write in the files.

---

## Web Application (Next.js / React)

`DOMAIN.md` entities map to routes, API endpoints, and context components. Each route should be defined as a domain boundary with its own entity, data shape, and business rules.

`COMMANDS.md` holds the npm scripts: `npm run dev`, `npm run test`, `npm run build`, `npm run lint`, and a rollback command.

The Architect treats each route as a domain boundary — blueprint steps map to components and API handlers. The Builder generates files inside `src/components/`, `src/pages/` (or `app/`), and `src/utils/`.

---

## Game Development (Unity / Godot)

`DOMAIN.md` functions as a technical Game Design Document. Entities track scenes, game states, event handlers, and asset flows. Define win/loss conditions, player state, and scene transitions explicitly — the Architect needs these to generate sound blueprints.

`COMMANDS.md` includes build, test, and export commands for the target engine:
- Unity: `dotnet build`, `Unity.exe -batchmode -quit -buildTarget [target]`
- Godot: `godot --export "[target]" [output path]`

---

## Desktop Applications (Electron / Tauri)

`DOMAIN.md` must include explicit local filesystem configuration parameters: which directories the app may read, which it may write, and what the safe machine-access bounds are.

`SECURITY.md` must explicitly define which local filesystem paths the app is permitted to access. Desktop apps interact with the OS more directly than web apps — the security boundary must be defined before the Architect can produce safe blueprints.

---

## Data Ingestion & Automation (Python ETL)

This domain depends heavily on [Mode 4: Data Ingestion](modes/data-ingestion.md). Every session involving raw data files requires the security gate first.

`DOMAIN.md` defines data shapes (input schema, expected types, rejection criteria), transformation rules, and the boundary between valid and invalid records. Be specific — a field described only as "date" will be interpreted differently than "ISO 8601 date string, UTC, may be null for in-progress records."

`SECURITY.md` must explicitly define which data files may be uploaded to an AI session and which must be redacted first.

---

## Starter Template Library

The `_templates/` folder stores pre-built project scaffolds from completed projects. The folder is populated as you build — it is not pre-installed.

```
_templates/
├── web-app/          # Next.js + TypeScript core defaults
├── game-unity/       # Unity structural asset configurations
├── game-godot/       # Godot script node structures
├── desktop-electron/ # Electron main/renderer processes
└── data-parser/      # Python data handling validation routines
```

To start a new project from a template:

```bash
cp -r _templates/web-app/* /path/to/[PROJECT_NAME]/
# Then run global find-and-replace for [PROJECT_NAME]
```

Your first completed project becomes your first template. Over time, `_templates/` accumulates proven starting points with pre-filled `AGENTS.md` constraints, `DOMAIN.md` patterns, and `COMMANDS.md` scripts that reflect what actually worked in production.

## See Also

- [Mode 4: Data Ingestion](modes/data-ingestion.md)
- [Setup and Scaffolding](setup.md)
- [SECURITY.md](file-reference/security.md)
