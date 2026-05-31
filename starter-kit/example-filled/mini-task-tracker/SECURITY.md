# SECURITY.md - Mini Task Tracker

## 1. Files Never to Load Into AI Tools

- `.env`
- `.env.*`
- `*.env`
- `*.key`
- `*.pem`
- `secrets/`
- `credentials.*`
- `*.secret`

## 2. AI Tools in Use on This Project

| Tool | Provider | Notes |
|---|---|---|
| Claude | Anthropic | Design and Develop Mode sessions. |

## 3. Session Hygiene Rules

1. Check this file before loading project context into an AI tool.
2. Do not paste credentials, access keys, private infrastructure details, or personal contact information into an AI session.
3. Share only the minimum file context needed for the current session goal.
4. At session close, record durable project changes in the correct project file.
5. If protected information is exposed, stop work, rotate affected credentials, and record the incident outside the AI session.
