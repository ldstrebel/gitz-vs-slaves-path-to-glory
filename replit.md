# Gitz vs Slaves — Path to Glory Campaign Manager

## Overview
A Warhammer Age of Sigmar Path to Glory campaign management system. This is a document-browser web app that renders all campaign markdown files in a dark fantasy UI.

## Architecture
- **Backend:** Python 3.11 + Flask (`app.py`) — serves a single-page document browser
- **Rendering:** Python `markdown` library renders `.md` files as HTML
- **Frontend:** Inline HTML/CSS in Flask (dark fantasy gold-on-brown theme)
- **Port:** 5000

## Project Layout
```
app.py                          # Flask app — document browser
Agent Flows/                    # AI Gem instruction files
  Path to Glory - Aftermath Gem Instructions.md
  Path to Glory - Campaign Gem Instructions.md
AI Planning/
  arc-planning.md               # Living arc themes & Arc Compass log
  Campaign Notes.md
Campaign Lore/                  # Source-of-truth campaign documents
  Battle Bible.md               # Army rosters, GP, rank-ups, scars
  battle-summary.md             # Battle-by-battle reference
  campaign-novel.md             # Living prose narrative
  Previous Battles.md
WH P2G/                         # Core rules reference
  Path to Glory.md
  P2G Aftermath.md
  P2G Quests.md
  path-to-glory-index.md
Pairing                         # Campaign engine session recap
README.md
```

## Running
```bash
python3 app.py
```
Runs on `0.0.0.0:5000`.

## Deployment
Configured for autoscale using gunicorn:
```
gunicorn --bind=0.0.0.0:5000 --reuse-port app:app
```

## Campaign System
The campaign uses a multi-agent narrative engine with:
- **Campaign Engine Gem** — generates battleplans, asymmetric VP, underdog mechanics
- **Aftermath Engine Gem** — processes battle reports, manages rank-ups/scars, runs Arc Compass
- **Arc Planner** — living reference for narrative arcs and character development

The four-step loop: BATTLE → REPORT → AFTERMATH → UPDATE → PLAN
