# system/ - the brain, in six short files

This folder is the operating system we run every day with Claude Code, cut down to the parts that made the biggest difference, with everything private taken out. "We" means the people who built it. "You" means you.

Every rule here has a one-line why. The why is the useful part: it is how you judge the cases the rule never saw.

## Reading order

| # | File | What it answers |
|---|---|---|
| 1 | `01-ai-agnostic.md` | Where every record lives, and why no AI or chat ever holds the only copy. |
| 2 | `02-the-laws.md` | The twenty rules that saved us the most pain. |
| 3 | `05-the-records.md` | The seven records the AI keeps for you, and their columns. |
| 4 | `06-session-habits.md` | How to drive Claude Code day to day. |
| 5 | `03-captains-and-processes.md` | How repeat work becomes a process, then a seat. |
| 6 | `04-duet-the-dispatcher.md` | Running it from your phone with Duet. |

Why this order: records and habits are day one. Captains come after a process has run by hand a few times. Duet comes last, because it hands out work, and there has to be work worth handing out.

## What is already wired in this repo

| Piece | Where | What it does |
|---|---|---|
| The records | `records/` | Fix list, to-do, action log, your actions, miss log, handoffs, decisions. Empty, headers only. |
| The writer | `tools/log.py` | Adds rows, newest on top, dated by your computer's clock. |
| The mirror | `tools/sheets_mirror.py` | Copies a record to a Google Sheet tab (setup in 01). |
| The bus | `tools/bus.py` | Jobs in, answers back, for Duet (see 04). |
| The clock | `.claude/hooks/now.sh` | Tells the AI the real time on every message. |
| Helpers | `.claude/agents/` | scout (finds things), builder (does one task), verifier (checks it cold). |
| Skills | `/recap`, `/handoff`, `/new-captain` | The progress report, the handoff note, a new captain folder. |
| Templates | `templates/` | A captain rule book, a process, a decision record. |

## Day one, in five steps

1. Send Claude any message. Its answer should know the real time. If it does not, ask it to run `bash .claude/hooks/now.sh` and check `.claude/settings.json`.
2. Type: `add a fix row: test the fix list`. Then: `close fix 1, evidence: I can see it in records/FIX-LIST.tsv`. Open the file and look.
3. End the chat with `/recap`.
4. When a chat gets long, type `/handoff`, then start a fresh chat that reads it.
5. Week two: the Sheets mirror (01). Week three or later: your first captain (03), then the bus (04).

## Words used in these files

| Word | Meaning |
|---|---|
| repo | A folder whose every change is tracked by git. Yours lives on your Mac and is backed up to GitHub. |
| commit, push | Commit = save a labelled snapshot. Push = send it to GitHub. |
| TSV | A text file where each line is a row and a tab separates the columns. Opens in any spreadsheet. |
| hook | A small script Claude Code runs on an event, like every message you send. |
| skill | A saved prompt you run with a slash, like `/recap`. Lives in `.claude/skills/<name>/SKILL.md`. |
| subagent | A helper Claude starts with fresh context for one job, then reports back. |
| context | What the AI is holding in mind in this chat. It fills up as the chat goes on. |
| headless run | Claude Code started by a script (`claude -p`) with nobody watching. |
| connector | A link that lets Claude reach an outside app (mail, Drive, calendar). |
| service account | A robot Google account your scripts use. You share a sheet with it like with a person. |
| lead | The head AI of one area, with its own folder and rule book. |
| captain | A seat with a rule book that runs one lane of work (see 03). |
