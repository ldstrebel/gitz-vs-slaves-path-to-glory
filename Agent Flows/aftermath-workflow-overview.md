# The Campaign Engine: Master Orchestration Workflow

This document is the master step-by-step logic for the AI Agent to process battle results, chronicle the narrative, update campaign mechanics, and set up the next battle. It references two specialist gems that handle the detail work.

---

## Stage 0: Gather Aftermath Information

**Trigger:** User says a battle has been completed and they are ready to receive the Narrative Survey. They will provide a full summary of the battle following the structure in:  
`D:\Code\gitz-vs-slaves-path-to-glory\Agent Flows\aftermath-userprovidedinfo-template.md`

---

## 📝 Stage 1: The Narrative Survey (Survey Gem)

**Gem:** `D:\Code\gitz-vs-slaves-path-to-glory\Agent Flows\Aftermath Post-Battle Updates Instructions.md`

Follow the full instructions in that file. Summary:

### Step 1: Ingest & Analyze

- Accept Export values as final truth. No added math.
- Calculate GP using the battle's specific reward file.
- Identify rank-up thresholds and scar check thresholds.

### Step 2: The Narrative Survey (Output 1)

- Generate the survey per army: Field Report, Treasury, Rank Ups, Healing Table.
- **Rank Up options are generated using the Phase 1 Mandate (Story-First):**
  - Completely ignore mechanics during option generation.
  - Read `character-development.md` and `arc-planning.md` before writing a single option.
  - Options must describe a *character changing*, not a *fighter improving*.
  - Run the 5-point Internal Check before writing.
- Generate Arc Compass questions (2–3) grounded in this battle's specific events.

### Step 3: PAUSE for User Input

- Output the survey. Wait for the player to fill it out.
- **Do not generate mechanics or update any files until the survey is returned.**

---

## 🧮 Stage 2: Mechanics & File Updates (Quartermaster Gem)

**Trigger:** User returns the completed survey with rank-up choices, healing decisions, and Arc Compass answers filled in.

**Gem:** `D:\Code\gitz-vs-slaves-path-to-glory\Agent Flows\Aftermath Quartermaster Instructions.md`

Follow the full instructions in that file. Summary:

### Step 4: The Campaign Bible (Output 2)

- **Phase 2 Mechanic Translation:** Convert each selected narrative choice into a tier-appropriate, narratively faithful game mechanic. Work from story inward — behavioral truth → physical consequence → legal mechanic.
- Generate the full Campaign Bible per army: Rank Ups Table, Scars Table, Muster Table.

### Step 5: The Next Battle Hook

- Narrative context, environmental special rules, arc seeds from Arc Compass responses.

### Stage 3: The Chronicler (Story Archive)

- Update `campaign-novel.md` with atmospheric prose chapter.
- Update `Previous Battles.md` with mechanical summary archive.

### Stage 4: The Quartermaster (File Updates)

- Update `Campaign Bible.md` (Treasury, Battle Record, Rank Ups, Scars, Muster, Threshold Watch).
- Update `character-development.md` (Path Abilities, Scar History, Current Stats per unit).
- Update `arc-planning.md` (Narrative Threads, Arc Compass Response Log, battle marked complete).

### Stage 5: Recap and Hook next battle

- Inform user of which files were updated and why. This step is CRITICAL for establishing trust that all the required updates were completed. Consider this verification checklist
  - All Units updates across all sources: battle bible, character-development (renown, paths, wounds, scars, key narrative development)
  - Army summary stats updated: battle bible, character-development, campaign notes (GP, treasury, W/L)
  - Lore updated for users (battle-summary, campaign-novel)
  - Planning updated for AI (arc-planning, campaign Notes)

## 🧮 Stage 3: Create Next Battle

- Wait for signal to proceed to next battle creation phase from user. 
- Follow `D:\Code\gitz-vs-slaves-path-to-glory\Agent Flows\Battle Creation Instructions.md`
- Output: a fully generated battle plan

---

## **Verification Checklist (Pre-Flight)**

*Internal check before any response:*

### Survey Gem Checks (Stage 1):

1. **Data Integrity:** Export values accepted as final truth?
2. **GP:** Calculated correctly using battle-specific file?
3. **Narrative Purity:** `character-development.md` and `arc-planning.md` read before writing rank-up options?
4. **Phase 1:** Do options use mechanical vocabulary or describe only physical changes? (If yes — rewrite.)
5. **Specificity:** Are options grounded in named battle moments or unit history?
6. **Arc Compass:** 2–3 questions grounded in this battle's specific events?
7. **Healing Table:** Every wounded unit listed with hero categories?

### Quartermaster Gem Checks (Stage 2):

1. **Phase 2 Integrity:** Does each mechanic feel like a natural consequence of the narrative?
2. **Tier Balance:** Appropriate for tier? Cross-Path Check run?
3. **Scar Integrity:** Scars are penalties only?
4. **Drained Check:** Only applied after confirmed failed heal roll?
5. **File Coverage:** All four files updated?
6. **Arc Compass Log:** Summary block formatted for copy-paste?
7. **Muster Type:** Type column using only General/Hero/Companion/Blank?