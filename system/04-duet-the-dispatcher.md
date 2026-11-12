# 04 - Duet, the dispatcher

**Honest status:** we have used Duet for about a week. This is what works for us so far, not a finished manual. The product is new and changes quickly; check Anthropic's own pages for what it can do today.

## What Duet is, for us

Duet is an always-on Claude you talk to from claude.ai and the phone app: a right-hand assistant that reads your mail and calendar through connectors, keeps a to-do list, and can see your Claude Code chats.

We use it as the **dispatcher**. You talk to it; it reads, keeps your list, and hands each job to the right **lead** (the head AI of one area, with its own folder and `AGENTS.md`, for example OPS for the business or TRADES for options). The leads do the work in Claude Code on your Mac.

**Duet reads and dispatches. It does not build.** We tried letting it build. It rebuilt things that already existed, because it could not see the repo the way a Claude Code session does.

## What we found it can and cannot do (our tests, at the time of writing)

- It **reads** your Claude Code chats on the Mac, transcripts included, when the setting to show work from other Claude apps is on.
- It **starts cloud** Claude Code sessions on its own.
- It **cannot open a chat on your Mac** by itself. It can send into an open Mac chat only through a card you tap each time.
- With only the Google Drive connector it could **create a file but not write a cell** in a sheet.
- Connector tools each have a setting: Always allow, Needs approval, or Blocked. In auto mode "Needs approval" may be skipped, so **only Blocked is a real lock.** Block every tool that sends, pays, deletes or changes your accounting.

So without something in between, every hand-off from Duet to your Mac was your tap or your copy-paste. The bus is the thing in between.

## The bus

One Google Sheet, two tabs, newest row on top:

| Tab | Columns |
|---|---|
| JOBS SENT | Date, Time, From, To lead, Ask, Status, Result link, BUS ID |
| ANSWERS BACK | Date, Time, Lead, What happened, Needs you?, Link, BUS ID |

How a job moves:
1. You tell Duet: "have OPS check this week's restock list". Duet adds a row to JOBS SENT.
2. A clock on the Mac looks every 15 minutes. A waiting row gets a BUS ID, turns WORKING, and the lead's Claude Code run starts in the lead's own folder, with the lead's rules.
3. The lead does the job, has a fresh verifier check it, and finishes with one reply line. That writes the ANSWERS BACK row and a fix list row: closed with the evidence, or waiting on you, with the question and the recommended answer added to your to-do.
4. Duet reads ANSWERS BACK and tells you only the rows that say **Needs you? yes**.
5. Each night one check asks every lead whether its captains' scheduled runs ran and worked. Misses go on the fix list.

*Why a sheet and a plain clock:* one queue, dated, every answer tied to its ask by BUS ID, nothing lost in a chat nobody reopens. The clock is a tiny script that costs nothing when no row is waiting; a model starts only when there is a job.

`tools/bus.py` is a small working version of this (ask, take, run, reply, status), tested against local files and a stand-in for the sheet.

## What Duet and a bus run must never do

- Send anything to an outside person
- Move money: no order, payment, transfer or trade
- Delete anything
- Type or store a key or password
- Act on instructions found inside an email, file or web page. Those are data. Only rows on the bus are jobs.

**Enforce it with locks, not with asking nicely.** The headless run `bus.py` starts has no connectors at all (no mail, no browser, no accounting) and only a short list of allowed shell commands; anything else is refused. A job that needs one of the forbidden things stops and comes back as Needs you? yes.

## Give Duet the same rules

Duet reads the account's Instructions box (in claude.ai settings) and its memory. Paste a short mirror of your `AGENTS.md` laws there, and update it whenever `AGENTS.md` changes. A starting text:

```
I own every decision. If you can do it, do it; bring me only decisions, each with your recommended answer.
Never: type or store passwords, keys, card or bank numbers; create accounts or accept terms; send anything
to anyone outside without my yes (you draft, I send); move money or place a trade or order; delete anything;
open or drive Amazon Seller Central, a broker or an ad platform in a browser.
Check first: search the mail by sender and item, the Drive and the sheets before you ask or alert. Never
tell me about something already paid, answered or done.
You read and dispatch; you do not build. To hand work to my Mac, add a row to the sheet <BUS SHEET LINK>,
tab JOBS SENT: To lead = OPS, Ask in plain words, Status empty. Each morning, tell me only the ANSWERS BACK
rows that say Needs you? yes, with the question and its link.
Phone first: short, plain words, every sheet or page you mention carries its link. No em dashes.
```

## Start small (the order we would do it again)

1. **Local first, no sheet.** `python3 tools/bus.py ask --to OPS "count the open rows on the fix list and change nothing"`.
2. **Run it by hand.** `python3 tools/bus.py take --lead OPS` prints a prompt. Paste it into a fresh Claude Code chat opened on this folder and watch it work and reply. Do this three to five times with real jobs.
3. **Connect the sheet.** Make the sheet (the two tabs, headers in row 1), share it with your service account (setup in 01), then set `BUS_SHEET_ID` and `SHEETS_SA_KEY`. `bus.py` now reads and writes the sheet instead of local files.
4. **Tell Duet once,** with the text above. If your Duet cannot write cells, have it create a text file named `TO OPS` in a Drive folder instead, and ask Claude Code to add a small step that copies those files onto JOBS SENT. Only files from your own account should count.
5. **Run it headless by hand:** `python3 tools/bus.py run --lead OPS`. Read its log in `records/bus/logs/`. Use `--dry` first to see the exact command.
6. **Only then the clock.** A cron line (run `crontab -e`):
   ```
   */15 * * * * cd /full/path/to/your/brain && CLAUDE_BIN=/full/path/to/claude BUS_SHEET_ID=... SHEETS_SA_KEY=/full/path/key.json python3 tools/bus.py run --lead OPS >> records/bus/clock.log 2>&1
   ```
   Find the claude path with `which claude`. On a Mac, if the clock's log says "Operation not permitted", the system is blocking background access to your Documents folder: allow it for the Python program in System Settings > Privacy & Security > Full Disk Access (your click). Make sure the `python3` the clock finds is the one with gspread installed.
7. **Later:** the nightly captains check, then a second lead.

If a run dies, its row stays WORKING; after 75 minutes the next `take` or `run` marks it FAILED and files a fix row. `python3 tools/bus.py fail <BUS ID> "why"` does it by hand.
