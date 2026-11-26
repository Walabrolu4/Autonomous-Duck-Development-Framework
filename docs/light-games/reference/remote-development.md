# Remote Development and Access — Devices, Tools, Previews and Testing

**Framework status:** Required **reference chapter** for ADDF Light Games documentation; an **optional workflow** for individual game projects. **No new mandatory game-project file, service, subscription, credential or always-on agent is introduced.**

An iPad, tablet, borrowed computer, school lab or low-powered laptop can act as an interface while a trusted host performs coding, builds and tests. The goal is to **preserve project continuity and actual human playtesting** without confusing a remotely accessible tool with permission for an agent to run it.

## When to use

Use this guide when:
- you want to vibe-code in T3 Code while inspecting the same code in VS Code;
- you need to work from an iPad with your game and coding tools on a Windows, macOS or Linux host;
- you need an interactive browser-game preview or a streamed Unity/Unreal Editor;
- you are choosing between an always-on home workstation and an on-demand cloud environment;
- you are preparing an agent handoff, remote build or human Gate A playtest across devices.

**Not required** for a student working entirely on one computer. The framework must still operate locally with ordinary Markdown files and any supported assistant.

## 1. Understand the three locations

| Location | What runs there | Typical examples |
| --- | --- | --- |
| **Client** | The interface you touch; may show a code editor, agent chat or running preview | iPad Safari, another laptop, school browser |
| **Development host** | Real Git checkout, files, Codex/Gemini agent processes, terminal, installed tools and build commands | Windows 11 desktop, Mac, Linux machine, cloud workspace |
| **Preview/test target** | The actual runtime that renders the game or executes a test | iPad Safari, browser on host, Windows Unity player, remote-desktop stream |

An iPad running a browser client **does not inherently have a local Unity Editor or the project's Node/Python/engine toolchain**. The host does most execution. The preview target may be **different** from the build host: this matters when reporting test evidence.

A cloud agent is another execution environment, not automatically the same files as your home PC. Verify Git commit, active branch and uncommitted changes before assuming both environments share state.

## 2. Tool selection matrix

| Tool / workflow | What it adds | Best use | Important limits |
| --- | --- | --- | --- |
| **T3 Code remote access / T3 Connect** | Agent conversations and supported previews accessible from mobile/web while agents run on a host | AI-directed iteration using an existing coding-agent setup | Host availability, account/device approvals and installed provider support; does not itself authenticate ADDF approval |
| **VS Code Remote Tunnels + vscode.dev** | Browser code editing, Git diff, remote terminal and relevant forwarded developer services | Independent review, debugging, running *authorized* tests from iPad | Authenticated remote host must run; browser extensions and local/remote features differ |
| **T3 + VS Code together** | Agent interface plus a conventional editor on **the same working directory** | Preferred hybrid workflow for ADDF Light | A separate Git worktree or remote environment can make files appear “out of sync” |
| **Safari or other target browser** | Direct HTML5/Phaser/Canvas/Three.js/WebGL input/playtest | Human Gate A on browser games | Mobile viewport, memory, browser restrictions and touch input differ from desktop |
| **Sunshine host + Moonlight client** | Low-latency streaming of a Windows game/desktop with controller support | Unity/Unreal interactive editing, native game playtests | Remote streaming affects latency, video quality and some input behavior; not a native iPad engine |
| **Tailscale or equivalent trusted private network** | Private network path between owned devices | Reach approved local services without public router port forwarding | Configure access controls and authentication; not a substitute for app-level permissions |
| **GitHub Codespaces or supported cloud coding agent** | Cloud-hosted files and execution without needing home PC awake | Off-device coding, builds and browser previews | Distinct workspace, quotas/costs, secrets policy, graphical engine limits |

This is a *capability map*, **not** an endorsement that every item works on every platform/version, or that consumer AI subscriptions can be shared through an unauthorized proxy.

## 3. Recommended iPad + Windows hybrid workflow

### Prepare your host

1. On the Windows PC, identify the **exact game repository**, active Git branch, and working tree. Keep any existing human edits intact.
2. Install/configure your preferred **first-party coding agents** on that host using their supported sign-in methods. T3 Code is optional; ADDF does not require Claude, Codex, Gemini, OpenClaw or API keys.
3. Set up T3 Code's supported remote access, if using it. In current T3 documentation, host setup is under **Settings → Sharing & access**; enable remote connection for the intended environment, authenticate, and require approval for new devices where available.
4. Enable **VS Code Remote Tunnels** on that same trusted host. Microsoft documents the command **Remote Tunnels: Turn on Remote Tunnel Access...** and the authenticated browser client at https://vscode.dev.
5. If the host is a Windows PC using WSL2, choose whether the project and tools run in **Windows or the WSL2 filesystem**; open the exact same environment/path in both interfaces.
6. Prevent unplanned sleep when you genuinely need remote access. Use an explicit security-conscious power policy rather than broadly disabling security controls.

**No remote setup occurs automatically by installing ADDF Light.** Initial login, device pairing, background services, network configuration and host permissions remain user-controlled operations.

Official references:
- T3 Code remote access: https://github.com/pingdotgg/t3code/blob/main/docs/user/remote-access.md
- VS Code Remote Tunnels: https://code.visualstudio.com/docs/remote/tunnels
- VS Code for the Web: https://code.visualstudio.com/docs/remote/vscode-web

### Work from the iPad

1. Open the host-connected T3 Code client using its supported mobile app or https://app.t3.codes, if configured. Confirm the correct **environment**.
2. Open https://vscode.dev in Safari, connect through the authenticated Remote Tunnel, and select the **same project root** and branch/worktree.
3. Put the agent interface and editor side by side with iPadOS multitasking if your device supports it. A third browser window can hold the playable preview.
4. In T3 Code, ask the agent to read `SECURITY.md`, `AGENTS.md`, `STATE.md`, then the relevant sprint records. You can remain in the **same visible conversation** while progressing between workflow stages.
5. Review `SPRINT.md` and the exact `PLAN.md` revision in VS Code **before granting Gate I**. The host application's write-access permission is not equivalent to ADDF Gate I.
6. After approving the precise scope, let the agent edit the specified files, and inspect the **actual Git diff** in VS Code. Run only explicitly approved verification commands.
7. Open the game preview on the iPad, test the gameplay yourself, and supply real observations for `REVIEW.md` and Gate A.

**Critical detail: Git worktrees.** T3 Code may create an isolated working tree. Two programs showing the same repository *name* may still point to **different physical directories/branches**. Resolve the agent's exact workspace path, check `git status` and `git rev-parse --show-toplevel` where permitted, and open that path in VS Code. Do not copy or overwrite files blindly to “sync” them.

## 4. Run a browser game and access its preview

For a dependency-free HTML/JS prototype, a simple HTTP server **on the host** is usually enough. For example, after a human has authorized the relevant command in a game project's `PLAN.md`:

```powershell
# Run in the folder containing index.html (Windows host with Python installed)
python -m http.server 8000 --bind 127.0.0.1
```

The address `http://127.0.0.1:8000` refers to the **host**, not automatically to the iPad. Typing it directly into iPad Safari ordinarily points at the iPad itself and will not reach the PC.

Use **one approved connection mechanism**:
- **T3 preview / its supported remote preview tunnel**, if the installed version exposes the running port.
- **VS Code's authenticated port-forwarding/preview functionality**, verifying the URL and access level.
- **A private network path such as Tailscale**, with a deliberately scoped/accessible bind and firewall rule, or a private HTTPS service. Do **not** expose the test server publicly just to load it on a tablet.

Never bind a development server to every network interface or make its forwarded URL public without review. A local Python server is suitable for a small static game, **not** production deployment or exposure of the project's whole repository.

For Phaser/Vite/other tooling, use the *project's actual approved dev-server command* instead of assuming every project uses Python. Confirm the served root excludes credentials and private files.

Useful official references:
- Microsoft port forwarding: https://code.visualstudio.com/docs/debugtest/port-forwarding
- Tailscale private access: https://tailscale.com/docs/how-to/connect-to-devices
- Tailscale Serve (restricted private HTTPS): https://tailscale.com/docs/use-cases/application-testing/share-local-dev-server-with-team

## 5. Automated tests, browser playtests and game engines

| Project | Execute on host | Inspect/play from iPad | What counts as evidence |
| --- | --- | --- | --- |
| **HTML5, Canvas, Phaser, Three.js** | Approved JavaScript unit/build/test commands and dev server | Safari preview, touch/keyboard/controller as applicable | Recorded command output plus actual device/browser playtest notes |
| **Unity** | Unity editor/build pipeline on Windows/macOS (licensed and installed as needed) | Compatible WebGL build in Safari; or remote desktop/streamed editor | Engine/build log and human observations, with platform limitations |
| **Unreal** | Unreal editor/build/cook/test on Windows/macOS/Linux host | Stream actual host app/game; test native builds on their intended platform | Host verification plus separate streamed playtest, noting latency |
| **Godot or other native game** | Engine/headless checks or native game on host | Compatible web export or remote stream where supported | Distinguish browser export from native execution |
| **CLI tests / CI** | Host terminal or authorized CI runner | Read test logs and diffs | Test names, exact command, result, environment and known untested cases |

Example test command **only if it belongs to the approved game/project plan**:

```bash
node --test examples/completed-game/tests/game.test.cjs
```

A green build from the host means those tests passed **there**. It does not prove that a player could interact with the game in iPad Safari, nor that touch or controller input is correct. A human testing in Safari can supply Gate A for the **observed** experience; record if the target platform was different.

For Unity/Unreal/editor-heavy work, an iPad cannot run the full desktop editor natively. Sunshine on the host and Moonlight on the iPad can stream it as an optional path:

- Sunshine: https://app.lizardbyte.dev/Sunshine/
- Moonlight: https://moonlight-stream.org/
- Moonlight iPad app: https://apps.apple.com/us/app/moonlight-game-streaming/id1000551566

When evaluating controls, remember that remote streaming introduces network/video/input latency. Confirm important timing-sensitive mechanics again on the target hardware before claiming broad acceptance.

## 6. ADDF authorization remains unchanged

**Remote access is an execution environment, not a workflow stage or permission level.** All existing human gates apply:

| Gate | Remote-work interpretation |
| --- | --- |
| **D — Design** | Human chooses the testable experience and significant design alternatives |
| **I — Implementation** | Human authorizes **exact game files, commands, package/install effects, ports/network exposure and other side effects** under the current `PLAN.md` revision |
| **A — Acceptance** | Human actually plays or inspects the resulting artifact and records the verdict; the agent cannot self-accept |

If remote setup itself requires new privileged services, credentials, device enrollment, unattended execution, firewall changes or a public URL, those actions need **separate, explicit user authorization**. They are not silently bundled into a harmless game-code Gate I.

A host permission dialog may ask whether an agent can write a file or execute a command. ADDF Gate I is a **separate project-specific authorization**. Both must be respected.

At handoff or provider switch, verify the latest real game state, branch/worktree and plan revision **even if the T3 UI carries over the visible conversation**. No new conversation is required merely to switch Research/Design/Develop capability.

### Minimal project-specific checklist (optional)

You do **not** need a `REMOTE_ACCESS.md` in every game repository. When a project actually uses remote access, note relevant verified details in its existing `SECURITY.md`, `STATE.md` or an **optional local runbook**, without adding secrets:

- target host/runtime and which worktree is canonical;
- trusted connection method (not passwords, auth tokens or pairing links);
- approved server ports/commands and who may expose them;
- expected preview device/browser and accessibility controls;
- shutdown/revocation instructions and what counts as Gate A evidence;
- known limitations (iPad input, remote latency, offline host).

## 7. Security and availability checklist

Before working remotely, verify:

1. **Authentication:** use supported identity flows, device approval and MFA where available. Keep remote access private to trusted devices.
2. **Network:** prefer authenticated tunnels or private networks. Never publish a raw agent server, remote editor, debug port, file server or game-project root on the open internet.
3. **Secrets:** store tokens in provider/OS credential stores; never in `STATE.md`, prompts, Git, log captures or remote share links.
4. **Authorization:** distinguish host/tool permissions from Gate I. Avoid blanket unattended commands or write access.
5. **Source safety:** verify Git status and active worktree before every material operation; preserve unrelated human edits.
6. **Preview isolation:** serve only the intended build output; keep development environments and test data out of public previews.
7. **Recovery:** know how to revoke device access, disable T3 Connect, turn off VS Code tunnels and stop forwarded servers.
8. **Host reality:** a PC that is sleeping, switched off, disconnected or logged out of a needed service may be unreachable.
9. **Untrusted devices:** do not persist credentials or open sensitive project files on unmanaged school or shared machines unless permitted by policy.

A VPN such as Tailscale controls connectivity; it does not replace the game's `SECURITY.md`, provider login controls, or human consent. See [Security](../quality/security.md) and [Agent permissions](../agents/permissions.md).

## 8. Validate a remote workflow before relying on it

Record outcomes honestly as **passed**, **failed**, **not tested** or **user-reported**.

1. From the iPad, connect to the **intended host** in T3 and to the same project through VS Code.
2. Verify the same branch, current commit and worktree; inspect a harmless source file in both views.
3. Ask the agent to make a **documentation-only proposed change**. Confirm it is visible in VS Code without accidental duplication.
4. Present an implementation request **without Gate I**. The agent must stop without changing game code.
5. Authorize a specific, low-risk `PLAN.md` revision. Verify only the approved files change.
6. Run a listed test on the host and inspect its actual output from the iPad.
7. Open a private browser preview on the iPad and playtest at least one original acceptance criterion.
8. Record manual observations in `REVIEW.md`, preserve remaining blockers and obtain actual human Gate A.
9. If changing provider in the **same visible T3 conversation**, confirm the incoming model re-reads/reconciles source state and does not treat chat continuity as approval.
10. Disconnect and reconnect safely; confirm access can be revoked and no unexpected public service remains exposed.

An **unverified** mobile connection, remote host, preview or manual playtest is not a successful end-to-end remote-development test merely because the docs describe it.

## 9. Troubleshooting

**T3 and VS Code show different code:** Check the exact directory, active Git worktree, branch, and uncommitted files. Do not force-sync blindly.

**The server works on Windows but not on iPad:** Host `localhost` is not the tablet's `localhost`; use an authenticated preview/forwarding mechanism or deliberately configured private network route.

**VS Code opens but the terminal is missing:** Check that the browser session is actually connected through the **Remote Tunnel**, not only browsing a remote GitHub repository. Browser-only editing lacks the same execution capabilities.

**AI keeps coding after switching models:** Stop; re-read `SECURITY.md`, `STATE.md`, `PLAN.md`, real Gate I evidence and source diff. Tool/model switching grants no implementation permission.

**A Unity/Unreal game is hard to control remotely:** Stream the actual host desktop/game or export a compatible browser build; document latency and retest on target hardware.

**Your home PC is off:** Use an explicitly approved cloud runner (e.g., Codespaces) or wait until the host is online. A browser client does not make a shut-down PC run builds.

## Related and documentation boundaries

[Quick Reference](../guides/quick-reference.md) · [File-first handoff](../agents/handoff.md) · [Playtesting](../quality/playtesting.md) · [Testing](../quality/testing.md) · [Security](../quality/security.md) · [Troubleshooting](troubleshooting.md)

This chapter is part of the **Light framework reference/wiki and generated manual**, and is relevant to the Stage 7B compatibility review. It does **not** authorize Stage 7B implementation, production deployment or Stage 8 branding.
