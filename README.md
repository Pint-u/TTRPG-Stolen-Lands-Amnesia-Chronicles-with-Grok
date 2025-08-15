# TTRPG-Stolen-Lands-Amnesia-Chronicles-with-Grok

Overview:
- Solo D&D 5e game in unknown world (Stolen Lands-inspired).
- Gritty tone, NSFW-optional (player-initiated only).
- Amnesia PC: Starts naked, no knowledge/memory, unknown forest location. Builds "memory" via file updates (discoveries unlock facts).
- Time: In-game Day X (increment on rest/travel, no real/DnD dates).
- Goal: Explore, survive, recover memories through actions/rolls.

File Structures (Memory Banks):
- master_index.markdown: Central hub with links/anchors to all files for quick access.
- Journal.md: Dated (Day X) Consequence narratives from ARCR (append after each response; rotate old days if large).
- Inventory.md: Table | Item | Location | Value | Description | Source | (quick search; update on gains/losses).
- World_NPCs.markdown: Dynamic sections for Locations (with specs like cottage stove/bench), NPCs/Creatures (relations/known facts; expand on discoveries).
- Character_Sheets.markdown: Per-member sections with Stats/Gear/Traits/Looks/Voice/Feats (dynamic; add feats/abilities on gains).

Best Practices:
- Session Start: Load ARCR_Prompt.markdown, resume from master_index (last Day X). Query: "Resume from parsed state."
- During Play: Use ARCR for actions (e.g., "Action: Search forest"). Parse exports with full_parse.py, append updates (e.g., Consequence to Journal, feats to Character_Sheets).
- Commands (DM Agent): "DM" to pause/resume, "man" for list, "debug [feature]" to test (e.g., rolls/feats), "DnD [question]" for rules.
- Updates: After ARCR, query: "Append from parsed JSON to files (e.g., new building specs to World_NPCs)."
- Limits/Rotation: Monitor (query "List files"); rotate large Journal (archive old Day X). Backup with save_game.py (data URLs/zip).
- Memory Building: Amnesia - Files start blank; discoveries add (e.g., "unlock" forest facts in World_NPCs on exploration).

Tools/Scripts:
- full_parse.py: Parse exports for JSON (tables/sections).
- save_game.py: Print full files in code blocks, generate data URLs/zip for backups.

Quick Commands List:
- DM: Pause game.
- resume: Continue after pause.
- man: Show this list.
- debug roll d20: Simulate roll.
- DnD Cure Wounds: Rules answer.

For questions, query Grok directly.
---
Guide to Best Practices for Playing DnD in SuperGrok Workspace: POC Methods for Seamless Gameplay and Updates
As an expert in using Grok running in Chrome, I'll provide a comprehensive guide to best practices for your DnD Amnesia Campaign in the SuperGrok workspace. This focuses on proof-of-concept (POC) methods to utilize the workspace's file system, Grok chats, code_execution tool, and ARCR_Prompt for immersive play, persistent memory (via files as "amnesia recovery"), and updates without data loss. The guide is structured chronologically (what to do and when), with POC steps tested in Chrome tabs for efficiency. Key principles: Keep under 10-file limit with rotation, use Day X for in-game time, dynamic updates for memory building, and code for non-truncated saves.
1. Pre-Game Setup: Prepare Workspace and Files (Do This Once or When Starting Fresh)

When: Before any session, especially for new campaigns.
Best Practice: Start with a clean workspace to avoid limits. Use files as "memory banks" (blank for amnesia PC). Organize with folders/prefixes for quick access.
POC Method in Chrome:

Open Grok tab (grok.com > Workspaces > "DnD Amnesia Campaign").
In file manager: Create core files (Journal.md, Inventory.md, World_NPCs.markdown, Character_Sheets.markdown, master_index.markdown) with templates from Grok query (as in Step 2.1).
Upload scripts: full_parse.py (for export parsing), save_game.py (for backups)—2/10 slots.
Query Grok in chat: "Confirm setup: List files, suggest rotation if >8 used."


Expected: List (e.g., 5 core + 2 scripts = 7/10); rotate by deleting old exports.
Tip: If limit near, merge into game_progress.md (query: "Merge all core files into one compact md").



2. Starting a Session: Load State and Begin Play (Do This at Session Start)

When: Every session open.
Best Practice: Load prompt/files for continuity, resume from last Day X (amnesia PC "recalls" via files). Check for updates/rotations to avoid token overflow.
POC Method in Chrome:

Open 3 tabs: File manager (for edits), Grok chat (for play), JSON Editor Online (for parse validation).
In chat: "Load ARCR_Prompt.markdown. Resume from master_index.markdown state (last Day X from Journal.md, blank memory for amnesia). Confirm loaded files."
If previous export (e.g., testrun_last.md): "Run full_parse.py on testrun_last.md to get JSON, append updates to core files (e.g., Consequence to Journal.md)."
Start Play: "Action: [e.g., Search for shelter (Local Exploration)]."


Expected: ARCR response (e.g., Consequence: "Find cave..."); parse/export for updates.
Tip: Use Day X increment in modes (e.g., advance on rest)—query: "Increment Day X in Journal.md after long rest."



3. During Play: Generate Data and Handle Updates (Ongoing During Session)

When: After each ARCR response or major event.
Best Practice: Use ARCR for immersion (rolls, gritty narrative), parse immediately for updates to build memory (e.g., new feats to Character_Sheets, cottage specs to World_NPCs). Keep responses <2,000 chars; split if needed. NSFW only if prompted.
POC Method in Chrome:

Play Turn: Query: "Action: Build cottage (Downtime, add specs like stove to World_NPCs.markdown)."


Expected: ARCR (e.g., Success: Cottage built; update "World_NPCs: Unknown Forest - Cottage specs: Stove wood-burning").


Export Response: Use "Export Chat" as session_turn.md (temporary file, 8/10 slots).
Parse/Update: "Run full_parse.py on session_turn.md to get JSON. Append Consequence to Journal.md (dated Day X), items to Inventory.md, feats to Character_Sheets.markdown (dynamic section), specs/relations to World_NPCs.markdown."


Expected: Snippets (e.g., Character_Sheets: "Add Feats: Carpentry - +2 crafting"); copy to files.


Rotate if Large: If Journal >500 lines: "Rotate Journal.md: Archive old Day X to journal_archive.md, note in master_index.markdown."


Tip: For amnesia, query: "If discovery 'unlocks' memory, add to World_NPCs as Known Facts." Grok handles 5e mechanics (rolls from PHB).



4. Ending a Session: Save and Backup (Do This Before Close)

When: Session end or "session over" in prompt.
Best Practice: Use ARCR's 🔄 for final updates, print full files via save_game.py to avoid truncation, generate zip/data URLs for download (handles large content like Journal narratives). Delete temp exports to free slots.
POC Method in Chrome:

End Play: Query: "Session over. Run ARCR updates, then execute save_game.py to print code blocks and generate data URLs/zip for all core files."


Expected: Code blocks (e.g., ```markdown:disable-run


Download: Copy zip base64 to base64decode.org (new tab), decode/save as game_save.zip—unzip for backups.
Clean Up: "List files, delete session_turn.md."


Tip: Zip compresses large files (e.g., Journal with Consequence histories); data URLs bypass token limits for saves.



5. Handling Limits and Best Practices for Long-Term Play

When: Regularly monitor (query "List files").
Best Practice: Stay under 10 files (core 5 + scripts 2 + exports 2 = 9 max). Rotate/archive dynamically (e.g., old Journal to archive). Use master_index.markdown for quick access/search. For big files, split (e.g., journal_day1-10.md).
POC Method: Query: "Monitor limit: If >8 files, archive oldest Journal section, update master_index.markdown with link."
General Tips: Play 3-5 turns/session to avoid overflow. Use parsed JSON for mining (e.g., "Sum XP from Character_Sheets"). If NSFW, prompt explicitly. Backup weekly via zip.

This guide ensures smooth play and updates, tested as POC in Chrome. Satisfaction: High, as it leverages workspace for memory without resets. Try a full cycle—share feedback!
