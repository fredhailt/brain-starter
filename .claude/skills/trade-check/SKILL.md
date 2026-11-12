---
name: trade-check
description: "Walks a proposed PAPER options trade through the written rules in options/02-the-wheel.md, options/04-the-tastytrade-way.md and the rule card in options/06-small-account-playbook.md (liquidity, IV rank, days to expiration, delta, size against the account, earnings date, defined risk), returns PASS, FIX or SKIP with a reason per rule, writes the ticket, and adds the row to options/trade-log.csv newest at the top. Never places an order and never gives personal financial advice. Use when the user says 'trade check', 'check this trade', 'wheel ticket', 'should I sell this put', 'check my put', 'is this trade OK', 'run the rules on this', or pastes an option quote and asks whether it fits the rules."
---

# trade-check

A rules check for a proposed **paper** options trade. It applies the user's own written rules. It is education, not financial advice, and it never places an order.

## Hard lines (read first, never bend)

1. **Never place, send, stage or modify an order** with any broker, API or browser, paper or live. No order endpoints, no "submit" clicks. The user places every order by hand.
2. **Never give personal financial advice.** Do not say "you should buy" or "this is a good investment". Say what the rules say: PASS, FIX or SKIP, and why.
3. **Never guess a market number.** Every price, delta, IV rank, open interest and earnings date comes from the user (pasted from the broker) or a data tool the user has set up. If one is missing, ask for it. An unknown earnings date or IV rank is a SKIP, not an assumption (fail closed).
4. **Do the arithmetic in code**, with `/usr/bin/python3`, and show the inputs. Never mental math on money.
5. **Money is written as USD 1,000 style** in everything this skill writes, never with a currency symbol in front of a digit.
6. No em dashes or en dashes in anything written.

## Step 1. Gather the proposal

Get today's date with the `date` command. Then collect every field below in ONE message to the user, listing only what is missing:

| Field | Example |
|---|---|
| Mode | paper (live only after the gate in options/07) |
| Account size | USD 8,000 |
| Ticker and strategy | XYZ, cash-secured put |
| Expiration date | 2026-02-13 |
| Strikes | short 23, long blank for a single option |
| Contracts | 1 |
| Bid and ask of every leg | 0.58 / 0.62 for a single put; one pair per leg for a spread |
| Delta of the short strike | 0.25 |
| IV rank, and where it came from | 41, broker screen |
| Open interest at the short strike | 850 |
| Next earnings date | 2026-02-26, or "none before expiration" with the source |
| For a cash-secured put | one sentence: why the user would own 100 shares at this strike |
| For a covered call | cost basis per share |
| For any short call (covered call, call spread, iron condor, jade lizard) | the next ex-dividend date, or "none before expiration" with the source |

## Step 2. Read the rules

Read these files from disk every time (the user may have changed them):
- `options/06-small-account-playbook.md`, section "The starter rule card". **Its numbers override every default below.**
- `options/02-the-wheel.md` (wheel rules) and `options/04-the-tastytrade-way.md` (management rules), for the reasons to cite.
- `options/trade-log.csv`, to count open positions (rows with mode `paper` or `live` and an empty `date_closed`) and the capital they use.

Defaults, used only if the rule card is missing: IV rank at least 30; 30 to 45 days, aim 45, for every strategy; short delta 0.20 to 0.30 for cash-secured puts and covered calls (the wheel band), and a separate band of 0.16 to 0.30 for the short strikes of credit spreads, iron condors and the jade lizard; no earnings before expiration; bid/ask gap at most 10 percent of mid and open interest at least 100; defined-risk max loss at most 3 percent of the account; strike x 100 at most 30 percent of the account for a cash-secured put and for a jade lizard's put; total committed at most 50 percent; at most 5 open positions; take profit at 50 percent, decide at 21 days left; never naked calls or 0DTE.

## Step 3. Compute

With `/usr/bin/python3`, compute and show:
- days to expiration (calendar days from today)
- mid price, and the bid/ask gap as a percent of mid
- the **natural price**, which is the realistic fill: for a credit, the bids of every leg you sell minus the asks of every leg you buy; for a debit, the asks of legs you buy minus the bids of legs you sell. Use the natural price, not the mid, for every number below (show the mid beside it for reference)
- **total credit in USD** = natural credit per share x 100 x contracts
- **max loss**, using the natural credit: credit spread or iron condor = (width minus credit) x 100 x contracts; cash-secured put = (strike minus credit) x 100 x contracts; covered call = (cost basis minus credit) x 100 x contracts; jade lizard = (put strike minus total credit) x 100 x contracts
- **capital used**: credit spread or iron condor = max loss; cash-secured put = strike x 100 x contracts; jade lizard = put strike x 100 x contracts (sized like the cash-secured put it contains, options/03); covered call = cost basis x 100 x contracts
- capital used as a percent of the account, and total committed including open positions
- break-even price, using the natural credit
- for a jade lizard: total natural credit against the call spread width

## Step 4. Check every rule

One line per check, each PASS, FIX or SKIP, with the number and the rule's source file.

| Check | PASS when | Otherwise |
|---|---|---|
| Mode and gate | Mode is paper. For mode live, ALL seven gate conditions in options/07 must hold (list below) | Any condition unmet or unconfirmed: SKIP, naming which |
| Strategy allowed | On the rule card's list; nothing naked except a fully cash-secured put | SKIP |
| Never list | Not a naked call, not 0DTE, not sized up after a loss | SKIP |
| IV rank | At or above the rule card's number | Below: SKIP (wait, or pick another name). Unknown: SKIP |
| Days to expiration | Inside the rule card's window | FIX: name an expiration inside the window |
| Short delta | Inside the rule card's band for that strategy: the wheel band for a cash-secured put or covered call, the spread band for credit spreads, iron condors and the jade lizard | FIX: name a strike inside the band |
| Earnings | No report between today and expiration | Report before or on expiration, or date unknown: SKIP (an earlier expiration may fix it; say so) |
| Liquidity | Gap and open interest inside the rule card's limits | FIX: try a nearer expiration or a more traded strike; SKIP if the whole chain is thin |
| Size | Defined risk: max loss inside the rule card's cap. Cash-secured put and jade lizard: capital used (put strike x 100 x contracts) inside the cash-secured put cap | FIX: fewer contracts, a narrower spread or a lower strike; SKIP if one contract is already over the cap |
| Total committed | At or under the cap after this trade | SKIP: wait for a position to close |
| Open positions | Under the cap after this trade | SKIP |
| Wheel owner test | Cash-secured put has the user's own-it sentence | FIX: ask for it |
| Covered call basis | Call strike at or above cost basis, or the user wrote that they intend to exit | FIX |
| Ex-dividend | For ANY short call (covered call, call spread, iron condor, jade lizard): no ex-dividend date before expiration, or the short call is far enough out of the money that its time value stays above the dividend | FIX: note the early assignment risk (options/01) and suggest an expiration before the ex-date; date unknown for a short call: SKIP |
| Jade lizard rule | Total natural credit greater than the call spread width | FIX |
| Exit plan | Written: take profit at 50 percent, decide at 21 days left, or the user's own plan | FIX: propose the rule card's plan |

**The seven gate conditions for a live trade** (options/07, THE GATE). Check each from `options/trade-log.csv` where the log can show it, and ask the user to confirm the rest in writing in this chat:
1. At least 30 closed paper trades: rows with mode `paper` and `date_closed` filled (`idea` rows do not count).
2. Over at least 90 calendar days: the oldest paper row's `date_opened` is 90 or more days before today.
3. Every paper row has a `check_verdict` and its opening columns filled.
4. The rules are written down: the user confirms their own version of the rule card in options/06 is current.
5. Rules followed on every trade: each closed paper row has `rules_followed` yes, or no with the break and its cost written in `lesson`.
6. At least one losing trade managed by the rules: a closed paper row with negative `pnl`, or a roll or an assignment in `exit_reason`, and `rules_followed` yes.
7. Every loss explained in one sentence: every row with negative `pnl` has a `lesson`, and the user confirms they can explain each one.

**Verdict:** any SKIP gives **SKIP**. Otherwise any FIX gives **FIX**. Otherwise **PASS**.

## Step 5. Write the ticket

Show this in the chat:

```
TRADE CHECK - <ticker> <strategy> - <today>
Mode: paper | Account: USD <size>
Trade: <sell/buy> <contracts> x <strikes> exp <date> (<DTE> days) for <natural credit> per share (mid <mid>), USD <total credit> in total
Max loss: USD <n> | Capital used: USD <n> (<pct> of account) | Break-even: <price>
Checks:
  PASS  IV rank 41 (rule: 30 or more, options/06)
  FIX   Delta 0.34 (rule: 0.20 to 0.30 for a cash-secured put) -> try the 22 strike
  ...
VERDICT: PASS | FIX | SKIP
Exit plan: <plan>
You place the order yourself, or not at all. This applies your written rules; it is education, not financial advice.
```

## Step 6. Add the row to options/trade-log.csv

- **PASS:** add a row with mode `paper`, `date_closed` empty, `check_verdict` PASS. Tell the user: if they decide not to place it, change `mode` to `idea` and fill `date_closed`.
- **SKIP:** add a row with mode `idea`, `date_closed` = today, `exit_reason` = "not placed: SKIP" plus the failing rule, `pnl` 0. Skipped ideas are graded later too.
- **FIX:** do not add a row. Offer the fixed version and run the check again on it.

Insert the row **directly under the header** (newest at the top), leaving every other row, including the EXAMPLE row, untouched. Use `/usr/bin/python3` with the `csv` module: read the whole file into memory first, then write it back with the new row at index 1. Never open the file for writing before reading it. Fill every column you know; leave closing columns (`exit_price`, `exit_reason`, `pnl`, `rules_followed`, `lesson`) empty for a PASS. Money columns hold plain numbers without currency symbols.

Then read the top three lines of the file back to confirm the row landed, and tell the user the file path.

## Step 7. When the user closes a trade

If the user says they closed, rolled, or were assigned on a logged trade, update that row's closing columns (`date_closed`, `exit_price`, `exit_reason`, `pnl` computed in code, `rules_followed`, `lesson`). A roll closes the old row and adds a new row at the top for the new position.
