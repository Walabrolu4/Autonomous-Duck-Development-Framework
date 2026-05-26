# ADDF Wiki

The Autonomous Duck Deployment Framework — a file-first methodology for coordinating LLM-assisted research, design, development, review, handoff, and long-term project evolution.

## What this wiki covers

ADDF separates four decisions that AI-assisted workflows often collapse into one: how large the work is, where the work sits in the delivery process, what the model is allowed to do, and which files define the current truth. This wiki documents each of those decisions in full — the lifecycle, the modes, the project brain, the sprint loop, and everything a practitioner needs to apply the framework from day one.

The wiki is organized from first principles outward. Start with [Getting Started](getting-started.md) if you are new. Start with [Core Concepts](core-concepts.md) if you want the mental model before the mechanics. Jump directly to any page from the table below.

The source documents live in `_PDF/`. The wiki pages live here in `docs/`. When the README links to a path that differs from the actual wiki file name, the table below notes the mapping.

## Navigation

| Page | Section | What's there |
|---|---|---|
| [Getting Started](getting-started.md) | Foundation | First-session walkthrough — what to do in the first 20 minutes |
| [Core Concepts](core-concepts.md) | Foundation | The four separations and six core principles |
| [The 8-Step Lifecycle](lifecycle/index.md) | Lifecycle | All eight lifecycle steps with entry/exit criteria and mode mapping |
| [Operating Modes](modes/index.md) | Modes | Overview of all three modes and the mode-boundary table |
| [Research Mode](modes/research-mode.md) | Modes | What Research Mode investigates, produces, and must never do |
| [Design Mode](modes/design-mode.md) | Modes | What Design Mode writes, reviews, and must never touch |
| [Develop Mode](modes/develop-mode.md) | Modes | Implementation constraints, dry run requirement, permission levels |
| [Work Scale Model](work-scale.md) | Scale | The five work scales and the scale-to-process mapping table |
| [Sprint Loop](sprint-loop.md) | Sprint | The 11-step controlled implementation workflow |
| [The Project Brain](project-brain.md) | Files | The file-backed memory layer — core files, sprint files, release/feature files |
| [File Reference](file-reference.md) | Files | Templates for every project brain file |
| [Prompt Catalog](prompt-catalog.md) | Prompts | All copy-paste prompts for every mode and workflow |
| [Handoff, Resumption & Model Switching](handoff-protocol.md) | Handoff | How to checkpoint, produce a handoff summary, and onboard an incoming model |
| [Repository Structure](repository-structure.md) | Setup | Standard, minimum viable, and public repo layouts |
| [Initial Setup](initial-setup.md) | Setup | Bash commands, file population order, first session |
| [Develop Mode Permission Levels](permission-levels.md) | Reference | The 0–4 permission level scale and escalation rules |
| [Release Cycles](release-cycles.md) | Cycles | Release plan, folder structure, starting a new version, completion criteria |
| [Feature Cycles](feature-cycles.md) | Cycles | Feature flow, folder structure, feature brief template |
| [Domain Adaptations](domain-adaptations.md) | Reference | How ADDF adapts to web, game, desktop, data, and documentation projects |
| [Examples](examples.md) | Reference | Mini Task Tracker and ADDF public repository walkthrough |
| [Operational Checklists](checklists.md) | Operations | Four gate checklists — pre-session, pre-Develop, pre-authorization, pre-commit |
| [Failure Handling & Troubleshooting](troubleshooting.md) | Operations | Four failure recovery procedures with step-by-step actions |
| [ADDF and Agile](agile-comparison.md) | Reference | What ADDF borrows from Agile/Scrum and what it deliberately omits |
| [Glossary](glossary.md) | Reference | Canonical definitions for all framework terms |

### README link mapping

The `README.md` at the project root links to some paths that differ from the actual wiki file names. The correct targets are:

| README link | Actual wiki file |
|---|---|
| `docs/sprint-workflow.md` | [`docs/sprint-loop.md`](sprint-loop.md) |
| `docs/prompts.md` | [`docs/prompt-catalog.md`](prompt-catalog.md) |
| `docs/file-reference/index.md` | [`docs/file-reference.md`](file-reference.md) |
| `docs/example.md` | [`docs/examples.md`](examples.md) |

The `_PDF/` subfolder contains the source documents and images. Wiki pages reference images from that folder using relative paths such as `_PDF/images/5_8-Step Lifecycle.png`.

---

[→ README](../README.md) · ADDF v3.5
