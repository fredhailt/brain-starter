# AGENTS.md - the rule book

Every AI that opens this folder reads this file first: Claude Code (through `CLAUDE.md`), Codex, and any other coding tool. One file, one set of rules, no second copy to drift.

## Who you're working for

A salesman with a full-time job, building a side income with about $5,000 to $10,000 to start. Strong on the phone, getting good at Claude Code, new to options and new to Amazon. Explain what you're doing in plain English, and say what a technical word means the first time you use it.

The three lanes in this folder:
- **Options** (`options/`): learning first, paper trading second, real money only after the gate in `options/07-paper-trading-with-claude.md`.
- **Amazon wholesale** (`amazon/`): finding brands, calling them, the first order, selling through FBA.
- **Other businesses** (`ideas/`): ones an AI is genuinely good at helping run.

## Rules, always

1. **If you can do it, you do it.** Don't hand the human manual steps you could take yourself. A question reaches him only when you truly can't act, and it comes with your recommended answer.
2. **Check first.** Before building anything or asking where something is, search this folder, the records and the web. Reuse or upgrade what exists. A thing 90 percent like one that exists is a duplicate.
3. **Never guess a number.** Every fee, price, rate or sales figure gets a source and a date. Do the math in code (Python), never in your head.
4. **No money moves without the human's word for that one thing.** You never place a trade, place an order, pay, or transfer. Draft it, show it, stop. He clicks the final button.
5. **Nothing goes to another person without his yes.** You draft emails and messages; he sends them.
6. **Credentials are his alone.** Never type, store or ask for a password, API key, card, bank, SSN or tax ID in a chat or a file. Keys go in a `.env` file that git ignores, typed in by him.
7. **No browser bots on Amazon Seller Central, a broker, or an ad platform.** Those accounts can be flagged or banned for it. Use official APIs (read-only first), or read his screenshots and advise.
8. **Options: paper first.** No real-money options trade until the paper gate is passed and he says go. Every trade idea goes through `/trade-check` and lands in `options/trade-log.csv`. This is education, never personal financial advice.
9. **Amazon: work and this business never mix.** No company data, no work CRM or ZoomInfo exports, no work logins, no company Claude account.
10. **Every write to the outside world is logged.** A sheet edited, an email drafted to a real inbox, an API write: one row in `records/ACTION-LOG.tsv` with the result and how to undo it.
11. **Nothing is deleted.** Archive or rename instead. Ask before overwriting anything.
12. **Newest at the top** of every list that grows (trackers, logs, the fix list), with the date.
13. **Save the work every time something works:** commit, then push to `origin` (his own private repo). Never push to `upstream`, the starter repo this came from.
14. **Done means proven.** Say what you checked and how he can check it himself in one sentence. Anything left over goes on `records/FIX-LIST.tsv` with a number, never only in the chat.
15. **No em dashes** in anything you write. Hyphens, or restructure the sentence. (A house style; it also keeps the writing plain.)

## How we work

- **Plan, then build.** Anything with more than two steps: show numbered steps with a check at the end, then build one step at a time.
- **One job per chat.** When a chat gets long, write a dated entry at the top of `records/HANDOFF.md` (`/handoff`) and start a fresh one.
- **The second time he asks for the same kind of thing, offer to turn it into a skill** in `.claude/skills/`.
- **Captains and processes:** a captain is a seat with its own rule book; a process is the work, and it isn't finished until its named result exists. See `system/03-captains-and-processes.md`. Build the process first, then name the captain.
- **The big three:** every record that matters lives as a file here, is pushed to GitHub, and (once set up) is mirrored to a Google Sheet. See `system/01-ai-agnostic.md`.
- **End every task with `/recap`:** the goal, what is done with proof, the honest percent, what waits on him, the next task.

## Where things live

| Folder | What's in it |
|---|---|
| `system/` | How the whole AI operating system works, and why. |
| `options/` | How options work, the wheel, the jade lizard, the tastytrade way, the small-account playbook, paper trading with Claude. |
| `amazon/` | Amazon wholesale from setup to the nightly wrap-up, plus the trackers. |
| `ideas/` | Other businesses worth starting. |
| `records/` | His fix list, to-do, action log, miss log, handoffs and decisions. |
| `templates/` | Blank captain, process and decision files. |
| `tools/` | Small scripts: `log.py` for the records, `sheets_mirror.py` for Google Sheets, `bus.py` for jobs handed over from Duet. |
| `.claude/` | Skills (slash commands), helper agents, and the clock hook. |
