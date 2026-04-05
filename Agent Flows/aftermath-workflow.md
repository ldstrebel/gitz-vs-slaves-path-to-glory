# The Campaign Engine: Master Orchestration Workflow

This document outlines the master step-by-step logic for the AI Agent to process battle results, chronicle the narrative, update campaign mechanics, and set up the next battle.

---

## 📝 Stage 1: The Narrative Survey
**Trigger:** User provides a filled-out `aftermath-template.md` and potentially a roster export.

1. **Verify Integrity:** Check `aftermath-template.md` for MVP, Favor of the Gods, and Unit Status. Cross-reference with `Battle Bible.md` to ensure no units are missing.
2. **Economic Generation:** Calculate the GP earned based on Victory/Loss and Warlord survival. Do not update files yet.
3. **Threshold Math:** Check for Rank Ups and Scars based on survivors, casualties, and the Path tables. Do not update files yet.
4. **Generate Survey:** Post an artifact titled `Battle [X] Aftermath Survey` asking the user for:
   - **Narrative Hooks for Rank Ups/Scars:** You MUST provide 2-3 specific, deeply narrative options for the user to choose from. These options must reflect overarching plot developments, interpersonal warband dynamics, psychological trauma, or evolving ideologies based on recent campaign events. DO NOT provide generic "RPG skill tree" combat flavor (e.g. "hits harder", "tougher armor"). Furthermore, **DO NOT include a "Write-in" option.** You must boldly author the options yourself so they actively shape the storytelling and arc planning. 
   - **Hidden Mechanics:** Keep the mechanical impact (the AoS 4.0 rule) of these choices HIDDEN from the survey to preserve the narrative-first choice. You will generate and hardcode the balanced game rules for them only *after* the user selects their narrative path.
   - Details on how the quest was completed (if applicable) and what the next quest is.
   - 3 probing questions about the battle's impact on overarching themes and character relations.
5. **HALT:** You must wait for the user to answer the survey before proceeding to Stage 2.

---

## 📖 Stage 2: The Chronicler (Story First)
**Trigger:** User completes the Aftermath Survey.

1. **Update `campaign-novel.md`:** Write a rich, atmospheric, prose-driven chapter summarizing the battle. Seamlessly weave in the answers from the survey (scar origins, heroic moments, tension between characters).
2. **Update `Previous Battles.md`:** Archive the mechanical summary of the battle (Who fought, the Underdog Twists used, MVP, specific points scored) for historical records.

---

## 🧮 Stage 3: The Quartermaster (Mechanics Updates)
**Trigger:** Executed immediately after Stage 2 is complete.

1. **Modify `Battle Bible.md`:**
   - Update Treasury and Battle Record.
   - Hardcode the new Rank Up and Scar tables.
   - Update Muster table (Points, Renown, Rank, Wounds, Scars).
   - Update Threshold Watch.
2. **Modify `character-development.md`:**
   - Add new entries to Path Abilities and Scar History for relevant units, using the narrative hooks provided in the survey.
   - Update current stats header for each unit.
3. **Modify `arc-planning.md`:**
   - Update "Narrative Threads" with the new character beats.
   - Mark the current battle as complete.

---

## ⚔️ Stage 4: The Architect (Next Battle Setup)
**Trigger:** Executed immediately after Stage 3 is complete.

1. **Identify Campaign Underdog:** Determine the Campaign Underdog based on total Campaign Wins. If wins are tied, the player with the lowest GP is the Underdog (if they have < 90% of the leader's GP).
2. **Generate Dual Twist Tables:** Create two distinct 1D6 Twist Tables (one for each faction) that offer escalating thematic benefits. The twist is rolled each round by the *current match underdog* (with Round 1 defaulting to the Campaign Underdog, and back-to-back double turns automatically triggering the underdog state for the opponent).
3. **Apply GHB Template:** Create the new Battle Lore/Plan document following the GHB 2025-26 10-point tiered scoring template and varied primary objective archetypes (Escort, Sabotage, Asymmetric, Environmental).
4. **Generate Manifesto:** Draft the narrative hooks and character growth moments based on the current campaign trajectory.
5. **Generate Battle Map:** Automatically use the image generation tool to create a tactical top-down battle map reflecting the new layout, and save it in the new battle's folder.

---

## 🛠️ Repeatable Command Logic
To trigger this master orchestration flow, the user simply needs to say:
> "Process aftermath for Battle [X]"
