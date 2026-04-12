# The Campaign Engine: Master Orchestration Workflow

This document outlines the master step-by-step logic for the AI Agent to process battle results, chronicle the narrative, update campaign mechanics, and set up the next battle.

---

## Stage 0: Gather Aftermath information

**Trigger**: User says a battle has been completed and they are ready to receive the Narrative Survey. They will provide a full summary of the battle following the structure in D:\Code\gitz-vs-slaves-path-to-glory\Agent Flows\aftermath-userprovidedinfo-template.md

## 📝 Stage 1: The Narrative Survey

Follow detailed steps in D:\Code\gitz-vs-slaves-path-to-glory\Agent Flows\Path to Glory - Aftermath Gem Instructions.md

### **Step 1: Ingest & Analyze (STRICT DATA INTEGRITY)**

### **Step 2: The Narrative Survey (Output 1**

### **Step 3: PAUSE for User Input**

### **Step 4: The Campaign Bible (Output 2)**

### **Step 5: The Next Battle Hook**

- **Goal:** Set the stage for the next engagement.

## **Verification Checklist (The "Pre-Flight" Check)**

*Before sending ANY response, you must internally answer these 7 questions:*

1. **Data Integrity:** Did I accept the Export Wounds/Renown as the final truth? (No math).
2. **Economic Check:** Did I remember to update the **Glory Points (GP)** in the Treasury header?
3. **Balance & Logic:** Are Rank Ups appropriate for the Tier? Are Scars penalties?
4. **Status Check:** Did I ONLY apply "Drained" if there was a confirmed failed heal roll?
5. **Completeness Check:** Did I remember to include **Step 5: The Next Battle Setup**?
6. **Arc Compass Check:** Did I include 2–3 Arc Compass questions grounded in *this battle's events*? Did I summarise the responses at the end of the Campaign Bible for copy-paste into `arc-planning.md`?

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
  - Update the new Rank Up and Scar tables.
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

**Trigger:** Executed immediately after Stage 3 is complete. follow D:\Code\gitz-vs-slaves-path-to-glory\Agent Flows\Path to Glory - Battle Gem Instructions (Clean).md for instructions