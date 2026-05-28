# COMMANDS.md

**The Autonomous Duck Deployment Framework — project commands.**

Load this file when a session needs to run, build, test, package, or deploy any part of the repository. Commands are grouped by task. Update this file when commands change.

---

## 1. Prerequisites

Before running any command, verify the following are installed:

```
Node.js 18+ (for website and CLI tool, v0.2+)
Python 3.11+  (for CLI tool alternative, v0.3+)
git
```

For v0.1, no build tools are required. The v0.1 deliverables are Markdown files and static assets.

---

## 2. Repository setup

Clone the repository:

```
git clone https://github.com/[org]/autonomous-duck-deployment-framework.git
cd autonomous-duck-deployment-framework
```

Check current state:

```
cat STATE.md
```

Check active sprint:

```
ls planning/sprints/
```

---

## 3. Documentation commands

### Preview documentation locally (v0.1)

No build step required for v0.1. Documentation is plain Markdown. Use any Markdown viewer.

With VS Code:

```
code .
```

With a Markdown previewer (optional):

```
npx serve docs/
```

### Validate Markdown links (optional)

```
npx markdown-link-check docs/*.md
npx markdown-link-check *.md
```

---

## 4. Website commands (v0.2+)

*The website is out of scope for v0.1. These commands are placeholders.*

### Install dependencies

```
cd website
npm install
```

### Run development server

```
cd website
npm run dev
```

### Build for production

```
cd website
npm run build
```

### Preview production build

```
cd website
npm run preview
```

### Deploy

```
[TBD — deployment target to be decided in v0.2 planning]
```

---

## 5. CLI tool commands (v0.3+)

*The CLI init tool is out of scope for v0.1. These commands are placeholders.*

### Run the init tool (Node.js)

```
node tools/addf-init/index.js
```

### Run the init tool (npx, once published)

```
npx create-addf-project
```

### Run the init tool (Python, alternative)

```
python tools/addf-init/addf_init.py
```

### Test the init tool

```
cd tools/addf-init
npm test
```

---

## 6. Release packaging commands

### Create a starter kit ZIP

```
cd starter-kit
zip -r ../releases/addf-starter-kit-v[VERSION].zip blank/ example-filled/ README.md
```

### Create a prompt catalog ZIP

```
zip -r releases/addf-prompt-catalog-v[VERSION].zip prompts/
```

### Create an examples ZIP

```
zip -r releases/addf-examples-v[VERSION].zip examples/
```

### Create a full release package

```
[TBD — scripted in Sprint 009]
```

---

## 7. Git commands (common)

### Start a new sprint branch

```
git checkout -b sprint/NNN-short-description
```

### Stage and commit project brain updates

```
git add AGENTS.md DOMAIN.md STATE.md DECISIONS.md QUESTIONS.md RISKS.md
git commit -m "chore(brain): update project brain for sprint NNN"
```

### Tag a release

```
git tag -a v0.1.0 -m "v0.1.0 Public Proof"
git push origin v0.1.0
```

### View recent history

```
git log --oneline -20
```

---

## 8. Validation commands

### Check for secrets or private paths (basic)

```
git grep -i "api_key\|api-key\|secret\|password\|token" -- "*.md" "*.json" "*.yml"
```

### Check for `.env` files accidentally staged

```
git status | grep ".env"
```

---

## 9. Rollback commands

### Revert last commit (before push)

```
git revert HEAD
```

### Restore a single file to last commit

```
git checkout HEAD -- [filename]
```

### Rollback notes

For sprint-level rollbacks, see `planning/sprints/sprint_NNN/rollback_log.md`.

---

*ADDF · `COMMANDS.md` · maintained as part of the project brain*
