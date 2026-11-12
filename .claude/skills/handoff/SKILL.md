---
name: handoff
description: Writes a dated handoff entry at the top of records/HANDOFF.md so a fresh chat can pick up exactly where this one stopped. Use when the human says "handoff", "write the handoff", "wrap this up", "start fresh", "new chat", or when this chat passes about a third of its context with the work not finished. Also files every leftover as a fix row.
---

# /handoff - the note the next fresh chat starts from

Why this exists: somewhere past 30 to 40 percent context a chat gets quietly worse. A fresh chat that starts from a good note does better than a long tired one. The note is the only thing that carries over, so it has to be complete and honest.

## STEPS

1. **Read the real clock.** Take the time from the clock hook's line in this turn (REAL CLOCK). Never write a remembered time.
2. **Refresh, do not guess.** Read back anything you are about to call done: the file, the sheet tab, the command output, `git status -sb`.
3. **File every leftover first.** Each unfinished piece becomes a fix row: `python3 tools/log.py fix add "<what is left, in plain words>" --area <area>`. Note the numbers it prints.
4. **Write the entry** at the top of `records/HANDOFF.md` (or the `HANDOFF.md` in this captain's folder when the chat is a captain's), directly under the line `---` that ends the header block. Insert; never edit or remove an older entry. Use exactly this shape:

```
## YYYY-MM-DD H:MM AM/PM - <short title of the job>
GOAL: <the ask, in the human's words>
DONE (with proof): <each item: what, where to see it, the proof>
PERCENT: <parts done> of <parts> (<n>%)
NEXT: <the one big next task>, then <up to 3 steps>
WAITS ON: <a person: who and what, with its fix or to-do number> / <technical: what>
FILES TOUCHED: <paths>
OPEN ROWS: <fix numbers from step 3>
```

5. **Commit and push it** with explicit paths: `git add records/HANDOFF.md records/FIX-LIST.tsv` (plus any files this chat changed and has not committed), commit, push.
6. **Tell the human,** phone-short: the title, the percent, the one next task, and the exact line to paste into a fresh chat:
   `Read the <H:MM AM/PM> entry of records/HANDOFF.md ("<title>") and work its NEXT line.`
   Name the entry by its time and title, never "the top entry": another chat may write above it before the new chat reads it.

## NEVER

- Write a handoff from memory without reading the results back.
- Leave a leftover only in the note: every one is a fix row with a number.
- Overwrite or tidy older entries.
- Use em dashes.
