# 08. AI-run options research: the crew

How we structure options research with AI once the basics are working. This is a pattern, not a product. Build it slowly, paper only, one process at a time.

## The idea: seats, not one big chat

One chat that "does everything" drifts. It forgets rules, mixes jobs, and grades its own homework. Instead, we split the work into **seats** (we call them captains). Each seat is one job with its own rule book: a short markdown file that says what it owns, what it reads, what it writes, and what it must never do.

A seat is not a person and not a separate AI model. It is a role Claude plays with one rule book loaded. The rule book is what makes it reliable.

## The eight seats

| Seat | Owns | Says yes or no to | Never does |
|---|---|---|---|
| **Research analyst** | The business behind the ticker: revenue, cash flow, debt, a dated fair-value estimate | "Would I own 100 shares at this strike?" | Pick strikes or size trades |
| **Chart reader** | Trend, support and resistance, volume, whether the stock is in free fall | "Is the timing sane, or is this a falling knife?" | Override the risk officer |
| **Risk officer** | Size, cash on hand, total exposure, earnings and event dates, concentration, a kill switch | PASS or STOP on every ticket. The only seat that can block a trade alone. | Loosen a limit to let a ticket through |
| **Trader** | Strategy, strike, expiration, delta, credit, the written exit plan | Writes the ticket | Place the order |
| **Bookkeeper** | What you actually own and the cash in the account today; the trade log; tax lots and wash sales | "The cash and positions on this ticket match the account" | Guess a balance |
| **Watchman** | News and the market backdrop: big index moves, volatility spikes, macro headlines | Raises a flag the risk officer must read | Make the trade call |
| **Calendar** | Every date that moves money: earnings, Fed meetings, inflation and jobs reports, expirations, ex-dividend dates, holidays | Supplies dates; an unknown date is reported as unknown | Assume a date |
| **Historian** | Grades past calls against what really happened; keeps the scoreboard per seat | Says which seats have earned trust | Rewrite old grades |

## The first process: the weekly put ticket

One trade idea, one week, every seat signing in order. The output is a **ticket**: a single page (or one row on a sheet) with each seat's line on it.

| Step | Seat | Writes on the ticket |
|---|---|---|
| 1 | Calendar | This week's dates: earnings for each candidate, Fed and data releases, expiration dates |
| 2 | Watchman | The backdrop in two lines, plus any flag |
| 3 | Research analyst | Two or three names you would own, each with one sentence of why and a fair-value range |
| 4 | Chart reader | For each name: timing OK, wait, or falling knife |
| 5 | Trader | The proposed trade: strike, expiration, delta, credit, size, exit plan |
| 6 | Risk officer | PASS or STOP, one line per rule checked, citing the rule card |
| 7 | Bookkeeper | Cash available today, matches the account: yes or no |
| 8 | **You** | Read the ticket. Place the order yourself, or don't. |
| 9 | Historian, later | At close and again 30 to 60 days later: what happened, which seats were right |

Three rules make the ticket trustworthy:
- **Every seat signs, in order.** A missing signature means no trade.
- **NO TRADE is a valid ticket.** A week where the risk officer says STOP is the system working. Grade those too: was skipping right?
- **The ticket is graded later against reality.** Without the historian, the crew only ever hears its own opinion.

## Patterns that keep the crew honest

- **Fail closed.** If a seat cannot read a number it needs (a price, an earnings date, the cash), the answer is STOP, never a guess.
- **Sign only by written rules.** A seat checks the rule card. A rule that is not written down is a note, not a reason.
- **Never move a limit to fit a trade.** If the ticket is too big, the trader resizes it. The limit only changes in writing, on a calm day, never during a trade.
- **Every number carries its date.** "Cash $6,200 as of Monday 9:40 AM" beats "cash $6,200".
- **Record the call before the result.** Each seat writes its verdict before the outcome is known, so the historian can grade it fairly. Seats earn trust by their record, not by sounding confident.
- **A kill switch.** One file or setting that, when on, makes the risk officer STOP every new trade. You can flip it from your phone in a bad week.
- **Keep the record somewhere you can read.** A trade log or sheet, newest at the top. The chat is not the record.

## Why a human stays in the loop

- **Accountability.** The person who bears the loss presses the button.
- **AI errors are quiet.** A swapped strike, a stale quote, or a misread delta looks perfectly confident on a ticket. Your eyes are the last check.
- **Rules from brokers and regulators assume a human account owner** who understands what was sent.
- **Judgment about your life.** A job change, a big bill, a bad week of sleep: the crew does not know, you do.

The crew makes you faster and more consistent. It does not make you absent.

## What to build first

1. **One process, paper only:** the weekly put ticket.
2. **Three seats to start:** trader, risk officer, historian. The `/trade-check` skill in this repo is already a rough trader-plus-risk-officer. Your `trade-log.csv` is the historian's raw material.
3. **One rule book per seat,** each under a page, in a folder like `crew/<seat>/RULES.md`: the lane, what it reads, what it writes, its hard rules, what it must never touch.
4. **Run it by hand every week** for a month before automating anything.

## What to build later

| Later | Why wait |
|---|---|
| Chart reader, calendar, watchman, bookkeeper seats | Add one at a time, only when you feel the gap it fills |
| Live data through an API (paper first) | Typed-in numbers are fine until the process is stable |
| A scheduled run that drafts the ticket each Monday | Automate last, once the manual version is boring |
| A scoreboard per seat | Needs enough graded tickets to mean anything |
| Real money | Only after the gate in file 07, and still with you placing every order |

The order matters: question whether you need a piece, simplify it, run it by hand, and automate it last.
