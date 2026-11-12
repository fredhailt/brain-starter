---
name: recap
description: The honest progress report - what was asked, what is really done with proof, the real percent, what waits on a person versus on something technical, and the one big next task. Use at the end of every multi-step task, and whenever the human says "recap", "what's done", "where are we", "show me the proof", "progress", "status", "how far along", "what's left" or "is it done". Refreshes stale facts first and starts no new work during the recap.
---

# /recap - what is done, with proof

Why this exists: "done" kept meaning about 25 percent done. A recap that has to show proof for every line, and a percent that is never rounded up, is what fixed it. The rule underneath: unit tests passing does not count as proven, and no new work starts during a recap.

## FIRST, REFRESH (a minute, no new work)

Anything that may have changed since you last looked gets looked at again:
- the file or sheet tab you wrote (read it back),
- `git status -sb`, and whether the last commit is pushed,
- the last run of any job you started (its log, its exit code),
- any helper or background task still running,
- the open rows: `python3 tools/log.py fix list`.

A recap built from memory is a guess.

## THEN REPORT, PHONE-SHORT, IN THIS ORDER

1. **THE GOAL** - the human's own words, quoted, with when they said it.
2. **DONE, WITH PROOF** - one line each: what, where the human sees it (the file path, or the sheet and tab with its link), and the proof (the row it landed on, the command output, the commit, the run that exited 0). Not proof: "I wrote it", "the code is there", "tests pass", "it should work". Built but not on the human's surface means not done.
3. **THE PERCENT** - parts done over parts in the goal, as a bar: `######----  6 of 10 (60%)`. Never round up. If the parts were never listed, list them now and say so.
4. **WAITING ON** - split in two:
   - **a person:** who, exactly what, and the row it is filed on (fix number or to-do number). Before listing anything as waiting on the human, ask: can an agent do this instead? Only what survives goes to the human.
   - **something technical:** what, and who or what is on it.
5. **NEXT** - the ONE big next task, then at most three steps, each marked **mine** or **yours**.

Every leftover must already be a fix row with a number (`python3 tools/log.py fix add "..."`). A leftover named only in the recap is lost.

## NEVER

- Start, fix or build anything during a recap.
- Call an item done below 100 percent.
- Hide a failure in a list of wins: a broken or reverted thing leads its section.
- Use a file path or a tool name as if it explained itself; say what it is in plain words.
- Use em dashes.
