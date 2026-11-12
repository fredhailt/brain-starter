# 05 - The records

Seven records, all in `records/`. The lists are tab-separated files with the newest row on top; `tools/log.py` writes them and dates every row from your computer's clock. Mirror any of them to a sheet when you want them on your phone (01).

You never have to type in them. You say it in chat; the AI writes the row.

## Two lists, two owners

| List | Whose | What goes on it |
|---|---|---|
| FIX LIST | the AI's | Everything unfinished an agent can finish: broken things, promised work not done. |
| MY TO-DO | yours | Only what truly needs you: your word, your click, your signature, your credential, a real decision. |

A fix row that truly needs you stays open on the fix list (the AI's record) AND gets one row on your to-do pointing back at it ("fix #12"). When you have done it, the AI closes both.

*Why two lists:* when every ask landed on one long list, the AI's work buried the five things only you could do.

## FIX LIST (`records/FIX-LIST.tsv`)

Columns: **# | STATUS | WHAT IS WRONG** | AREA | WHERE TO SEE IT | WHO DOES IT | OPENED | DAYS OPEN | CLOSED ON | EVIDENCE

- **#** comes from the tool (highest plus one), never picked by hand.
- **STATUS:** OPEN, WAITING ON YOU, or CLOSED.
- **CLOSED** only with its evidence: what proves it is fixed. The row is never deleted.
- **DAYS OPEN** is recounted on every write, so an old row cannot hide.
- An obvious fix under 15 minutes is done now and never filed. A reminder is never a row.
- Commands: `python3 tools/log.py fix add "..."`, `fix done 12 "<evidence>"`, `fix list`.

## MY TO-DO (`records/MY-TO-DO.tsv`)

Columns: **# | STATUS | WHAT TO DO** | WHERE (link) | HOW | WHY | WHEN | RECOMMENDED ANSWER | ADDED | DAYS OPEN | FIX #

Every row is a complete ask:
- **What** to do, as the exact words to type or the button to press.
- **Where,** with the link.
- **How,** as numbered steps if it takes more than one click.
- **Why** it matters and what it unlocks; **when** it is needed.
- **The recommended answer,** so you approve instead of think.

Before anything lands here the AI checks: is it already done (search the mail by sender and item, read the open rows)? Can an agent do it instead? A row waiting more than 14 days gets re-asked in one line.

*Why:* "what, how, where, why, when, and your answer" is what turns a vague ask into a two-second yes.

## ACTION LOG (`records/ACTION-LOG.tsv`)

Columns: **WHEN | WHAT | RESULT** | KIND | WHO | TARGET | LINK | UNDO

- One row for every write the AI makes outside this repo (a sheet, a Drive file, an API, a draft in a real inbox), written AFTER the write lands, with the real result. Never "OK" for a write that did not land.
- **UNDO** is required: exactly how to reverse it.
- Reads are not logged. Changes inside the repo are already in git.
- **The AI's actions only.** The tool refuses a row whose WHO is you.
- Command: `python3 tools/log.py action add --what ... --target ... --result ... --undo ...`

*Why:* it is how you see from your phone what the machine did and whether it broke something.

## MY ACTIONS (`records/MY-ACTIONS.tsv`)

Columns: **WHEN | WHAT I DID | RESULT** | WHERE | NOTE

Your own done things: an email you sent, an order you placed, a call you made, a trade you entered. You say it in chat ("I sent the PO to the brand"), the AI writes the row, past tense only.

Command: `python3 tools/log.py did add "..."`

*Why:* the system needs to know what you did, or it will ask you to do it again.

## MISS LOG (`records/MISS-LOG.tsv`)

Columns: **WHEN | WHAT WENT WRONG | SHAPE** | FIXED IN | CAUGHT BY | MODEL

- One row every time the AI gets something wrong in a way that could happen again.
- **FIXED IN** is required: the rule file, skill or tool that was changed. "Not yet" is refused. Fix it where it lives first, then log it.
- **SHAPE** is one of five: `no-check` (built or asked without checking), `no-look` (handed over without looking), `over-scope` (did more than asked), `jargon` (spoke in terms you could not use), `wrong` (the facts or reasoning were wrong).
- Command: `python3 tools/log.py miss add "..." --fix "<where>" --shape no-look`

*Why:* nothing should be corrected twice. Counting the shapes shows which habit to fix, and the MODEL column shows whether a model is the problem.

## decisions/ (`records/decisions/`)

One file per build or system change, written the same turn it lands: `YYYY-MM-DD-short-name.md` from `templates/decision-TEMPLATE.md`.
- **What** was built.
- **Why,** in the words of whoever asked for it, quoted with the date.
- **The rules** it runs under.
- **How to repeat it** from scratch on a new machine, step by step.

One line per decision in `records/decisions/README.md`, newest on top.

*Why:* "write it down so this can be repeated or handed to someone else later." Six weeks on, nobody remembers why a thing is the way it is.

## HANDOFF.md (`records/HANDOFF.md`)

A dated entry at the top for every session that stops before the work is finished: the goal, what is done with proof, what is next (one big task, then steps), the files touched, the open fix numbers. Written by `/handoff`. The next fresh chat reads the newest entry first.

*Why:* a long chat gets worse; a fresh chat with a good note does not.
