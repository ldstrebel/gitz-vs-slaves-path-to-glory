# Aftermath Agent Flow: The Wake of the World-Eater

This document outlines the step-by-step logic for the AI Agent to process battle results and update the narrative campaign. 

---

## 📥 Stage 1: Ingestion & Analysis
**Trigger:** User provides a filled-out `aftermath-template.md` and potentially a roster export.

1. **Verify Integrity:**
   - Check `aftermath-template.md` for MVP, Favor of the Gods, and Unit Status.
   - Cross-reference with `Campaign Lore/Battle Bible.md` to ensure no units are missing.

2. **Economic Calculation (GP):**
   - **Base:** +5 GP (Participation)
   - **Victory:** +10 GP (Minor) / +20 GP (Major)
   - **Warlord Survival:** +5 GP if the General was not destroyed.
   - *Update:* `Battle Bible.md` (Treasury) and `arc-planning.md`.

3. **Renown & Rank Checks:**
   - **Survivors:** Roll D3 for each.
   - **Casualties:** +1 Renown.
   - **Favoured Warrior:** Roll D6 for the unit nominated in the template.
   - **Thresholds:**
     - **Rank Up:** If renown crosses 6, 15, 30, or 50.
     - **Scars:** If a unit was destroyed, increment Wounds. Check if they hit 5 (Serious) or 9 (Severe).
   - *Reference:* `WH P2G/Path to Glory.md` for Path Tables and Scar effects.

---

## 📝 Stage 2: The Narrative Survey (Output 1)
Post an artifact titled `Battle [X] Aftermath Survey` for the user. **Wait for user response before proceeding.**

1. **Rank Up Choices:**
   - For every unit that ranked up, provide the two ability options from their chosen Path.
   - Ask for a short narrative hook for the choice.

2. **Scar Integration:**
   - If a unit earned a scar, ask for its name and the narrative explanation (e.g., "The Frost-Bitten Hand").

3. **Quest Resolution:**
   - Ask if the active quest was completed (based on battle events).
   - If completed, ask for the reward choice and the next quest.

4. **Arc Compass (Narrative Reflection):**
   - Ask 3 probing questions about the battle's impact on the campaign's themes (Truth, Hope, Despair).
   - Ask for "Thread Updates" based on character growth moments.

---

## 📖 Stage 3: The Campaign Update (Output 2)
Once the survey is finalized, update the following files:

1. **Modify [Battle Bible.md](file:///d:/Code/gitz-vs-slaves-path-to-glory/Campaign%20Lore/Battle%20Bible.md):**
   - Update Treasury and Battle Record.
   - Update Rank Up and Scar tables.
   - Update Muster table (Points, Renown, Rank, Wounds, Scars).
   - Update Threshold Watch.

2. **Modify [character-development.md](file:///d:/Code/gitz-vs-slaves-path-to-glory/Campaign%20Lore/character-development.md):**
   - Add new entries to Path Abilities and Scar History for relevant units.
   - Update current stats header for each unit.

3. **Modify [arc-planning.md](file:///d:/Code/gitz-vs-slaves-path-to-glory/AI%20Planning/arc-planning.md):**
   - Update "Narrative Threads" with the new character beats.
   - Mark the current battle as complete.

---

## ⚔️ Stage 4: Next Battle Setup
1. **Identify Underdog:** Check "All-Time GP Earned" in the Battle Bible.
2. **Roll Twist:** Roll/Select a twist from the `arc-planning.md` table for the underdog.
3. **Generate Manifesto:** Create the "Battle Lore" document for the next engagement based on the current narrative trajectory.

---

## 🛠️ Repeatable Command Logic
To trigger this flow, the user simply needs to say:
> "Process aftermath for Battle [X]"

The agent will then look for the template in `Agent Flows/` and begin Stage 1.
