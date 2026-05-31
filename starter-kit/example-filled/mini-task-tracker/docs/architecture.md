# Architecture - Mini Task Tracker

## Overview

Mini Task Tracker is a single-page local app. It uses one HTML file, one CSS file, and one JavaScript file. It runs in the browser and has no backend.

## Components

- `index.html` provides task list structure and form controls.
- `style.css` provides layout, spacing, and visual state display.
- `app.js` handles task creation, completion, reopening, localStorage persistence, and DOM rendering.

## Data Flow

User action -> JavaScript handler -> TaskList update -> localStorage update -> DOM re-render.

## Key Decisions

Use localStorage for persistence (see `DECISIONS.md` Decision 001). Use no build tool for v0.1 (see `DECISIONS.md` Decision 003).
