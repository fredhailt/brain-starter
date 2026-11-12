# 07. Paper trading with Claude

**Paper trading** means trading with simulated money on real market prices. Nothing you do can lose real dollars. It is the cheapest tuition you will ever pay.

## Pick a paper account

| Option | What it is | Good for |
|---|---|---|
| **Your broker's paper mode** | For example thinkorswim paperMoney at Schwab, or Interactive Brokers' paper account | Practicing the exact screens and order tickets you will use with real money |
| **Alpaca paper API** | A free paper account you control with code. Alpaca's docs say options trading is enabled by default in paper. | Letting Claude Code read prices and positions through a script |

Two settings matter more than which one you pick:
1. **Size it like your real account.** A default paper balance of $100,000 teaches bad habits. Size every trade as if the account were your real $5,000 or $10,000.
2. **Paper fills can be kinder than real ones.** A simulator may fill you at a price a real market would not give, especially on wide bid/ask spreads. Log the mid price **and** the price you would realistically get.

**Keys:** if you use the Alpaca API, generate **paper** keys only, put them in a `.env` file that is in `.gitignore`, and never paste them into a chat or a commit. Live keys should not exist on this machine during the paper phase.

## Claude Code as your research partner

Claude is good at explaining, calculating, checking rules and keeping records. It does not know today's prices unless you paste them or give it a tool that fetches them, and it can be confidently wrong. Make it show its math.

What to ask it:

| Job | Example prompt |
|---|---|
| Explain | "Explain this trade like I'm new: sell the 45 put, buy the 43 put, 42 days out, $0.55 credit. What is my max loss, break-even and max gain?" |
| Check the rules | "trade check: cash-secured put on XYZ, 23 strike, expiring in 38 days, 0.25 delta, $0.60 bid / $0.64 ask, open interest 850, IV rank 41, account $8,000 paper" |
| Stress test | "If this stock gaps down 20 percent tomorrow, what does each of my open positions lose? Use the positions in trade-log.csv." |
| Earnings | "Here is the earnings calendar I copied. Which of my candidates report before their expiration?" |
| Review | "Grade my last ten closed trades in trade-log.csv. Where did I break my own rules, and what did it cost?" |
| Learn | "Show me with a small Python script how the 21-day rule changes my results on the trades in my log." |
| Build | "Write a script that reads my Alpaca paper positions and prints days to expiration and percent of max profit for each." |

Habits that keep Claude honest:
- Paste the actual quotes (bid, ask, delta, open interest, IV rank, earnings date). Do not let it guess a number.
- Ask "where did that number come from?" for anything that matters.
- Keep your rules in files (`06-small-account-playbook.md`), not in your head, so Claude checks against the same rules every time.

## The weekly routine (about an hour a week)

| When | What | Time |
|---|---|---|
| **Sunday evening** | Update `trade-log.csv`. Check every open trade against the exit plan: 50 percent profit hit? 21 days left? Earnings coming? Write the actions for the week. | 20 min |
| **Monday or Tuesday** | Pick at most two or three candidates. Run each through `/trade-check`. Place the PASS ones on paper yourself. | 20 min |
| **Midweek, 5 minutes** | Glance at open trades. Act only on the written triggers, not on feelings. | 5 min |
| **Friday** | Close out anything the rules say to close. Grade every trade that closed this week: rules followed yes or no, what you learned. | 15 min |

A full-time job makes this better, not worse: 30 to 45 day trades do not need you watching the screen.

## How to fill trade-log.csv

One row per trade, **newest at the top** (right under the header). The `/trade-check` skill writes the opening half for you; you fill the closing half.

| Column | What goes in it |
|---|---|
| `id` | A short label, for example `2026-03-02-XYZ-CSP`. The example row says `EXAMPLE`. |
| `date_opened` / `date_closed` | Dates, YYYY-MM-DD |
| `mode` | `paper`; `live` after the gate; or `idea` for a proposal `/trade-check` marked SKIP (logged with `date_closed` filled and `pnl` 0, so it never counts as an open or closed trade, but can still be graded) |
| `ticker`, `strategy` | What and how |
| `expiration`, `dte_at_entry` | Expiration date and days left at entry |
| `short_strike`, `long_strike` | Strikes; leave long blank for a single option |
| `delta_at_entry`, `iv_rank_at_entry` | From the broker screen |
| `earnings_date` | The next report date, or `none before expiration` |
| `contracts`, `credit_or_debit` | Per-share price; positive for credit, negative for debit |
| `max_loss`, `capital_used`, `pct_of_account` | In dollars and percent, from the check |
| `check_verdict` | PASS, FIX or SKIP from `/trade-check` |
| `exit_plan` | Written before entry |
| `exit_price`, `exit_reason`, `pnl` | Filled when closed |
| `rules_followed` | yes or no, and which rule if no |
| `lesson` | One sentence |

## THE GATE: no real money until all of this is true

| # | Condition |
|---|---|
| 1 | At least **30 closed paper trades** (rows with `mode` paper; `idea` rows do not count) |
| 2 | Over at least **90 calendar days**, so you have seen more than one market mood and one earnings season |
| 3 | **Every** trade went through `/trade-check` before entry and has a full row in the log |
| 4 | Your rules are **written down** (your version of the rule card in file 06) |
| 5 | Rules followed on every trade, or each break written up with what it cost |
| 6 | You have managed at least one losing trade by the rules (closed, rolled for a credit, or taken assignment) |
| 7 | You can explain every loss in one sentence |

Expect 4 to 6 months to get here with the five-position cap (file 06 shows the arithmetic). These numbers are our judgment, not a study. Note what the gate does **not** require: a profit. Thirty trades is far too few to prove an edge; tastylive's own lesson on occurrences shows how wildly small samples swing (file 04). The gate tests **discipline**, which is the thing that protects real money.

After the gate: start live with one defined-risk contract at a time, keep the same log with `mode` set to `live`, and keep running every trade through the check.

## The line Claude never crosses

**Claude never places a live order. You do.**
- Claude researches, checks and drafts the ticket. You read it, decide, and click.
- Even on paper, enter the orders yourself at first. The point is to practice the real motion, including reading the confirmation screen before you send.
- If you later script paper orders on Alpaca, use paper keys and the paper endpoint only, and keep live keys off the machine.

Why: an AI can misread a strike, use a stale price, or flip a buy and a sell. A human reading the ticket is the last check, and the person who bears the loss should be the person who presses the button.
