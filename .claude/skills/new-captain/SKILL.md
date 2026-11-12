---
name: new-captain
description: Builds a new captain folder (captains/<name>/) from templates/captain-AGENTS.md - the rule book, a HANDOFF.md, a first process file and a decision record. Asks the human only two things, the lane and the name. Use when the human says "new captain", "make a captain for", "give this its own seat", "set up a captain", or "/new-captain".
---

# /new-captain - a new seat, from the template

Why this exists: a captain is a seat with a rule book (system/03-captains-and-processes.md). Building each one by hand drifted; the template keeps every captain the same shape, and the human only decides what is truly theirs to decide: the lane and the name.

## ASK THE HUMAN ONLY TWO THINGS

1. **The lane:** "What should this captain own, in one sentence?" (for example: "restocking the products we already sell", "the weekly options trade review").
2. **The name:** "What do you want to call it?" Suggest one short, memorable name with your question, so the human can just say yes.

Everything else you work out yourself or fill with a sensible default the human can change later. Do not ask about the voice, the processes or the rules.

## CHECK FIRST

- List `captains/`. If a captain already owns most of this lane (90 percent alike), stop and say so: upgrade that one instead of making a twin.
- Read `templates/captain-AGENTS.md` and `templates/PROCESS-TEMPLATE.md` from disk.
- Search `records/` and the repo for any process already run by hand in this lane; if one exists, it becomes the first process.

## BUILD (the name in lowercase for folders, e.g. `captains/restock/`)

1. `captains/<name>/AGENTS.md` from the template:
   - the lane sentence as given;
   - a voice line that fits the lane (a buyer, a bookkeeper, a trade desk), marked as a default the human can change;
   - NOT MINE rows for any other captains in `captains/`, plus the catch-all row;
   - MY PROCESSES with one row for the first process;
   - the never list kept whole, plus lane-specific nevers (for example, a trading lane: never places a trade; a buying lane: never sends a purchase order);
   - BEV LANES with the one repeat decision the lane obviously makes, or "none yet";
   - RULINGS with one first row: today's date and time from the clock hook, the human's lane sentence in quotes, and "Owns this lane; everything else is NOT MINE".
2. `captains/<name>/HANDOFF.md` with the header block copied from `records/HANDOFF.md` and no entries.
3. `captains/<name>/processes/<first-process>.md` from `templates/PROCESS-TEMPLATE.md`, filled as far as is known, with its finished result named. Leave unknown steps as `<...>` rather than invent them.
4. `records/decisions/YYYY-MM-DD-captain-<name>.md` from `templates/decision-TEMPLATE.md`, and one line at the top of the index in `records/decisions/README.md`.
5. One fix row: `python3 tools/log.py fix add "Run <name>'s first process by hand 3 times, then fill its steps" --area <name>`.
6. Commit and push with explicit paths (`git add captains/<name> records/decisions records/FIX-LIST.tsv`).

## REPORT, PHONE-SHORT

- The folder and its rule book, by path.
- The first process and its finished result, in one line.
- The fix number for the three runs by hand.
- How to talk to it: open a chat on the folder `captains/<name>/`, or say "as <NAME>, ..." in the main chat.

## NEVER

- Ask more than the two questions.
- Give the captain a clock, a scheduled job or any write access in this step. That comes after the process has run by hand.
- Copy another captain's rulings into the new one.
- Use em dashes.
