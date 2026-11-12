# 06. Small account playbook

What changes when the account is USD 5,000 to 10,000, and the rule card the `/trade-check` skill reads.

## Cash account or margin account

| | Cash account | Margin account |
|---|---|---|
| Borrowing | None. You trade with your own settled cash. | The broker lends against your holdings. FINRA's general minimum to open margin is $2,000 of equity. |
| What you can sell | Covered calls and cash-secured puts; many brokers also allow spreads | Adds naked options at higher approval levels |
| Main trap | **Freeriding**: buying a security and selling it before you have paid for it. Under the Fed's Regulation T this can freeze the account for 90 days (investor.gov). | Losses can exceed what you planned, and margin calls can force sales at the worst time |
| Good for a beginner? | **Yes.** The cash rule is a free seatbelt. | Later, once your rules are proven |

## Option approval levels

You apply for options trading and the broker assigns a level, as FINRA Rule 2360 requires. Levels differ by broker, but the usual order is:
1. Covered calls (sometimes cash-secured puts)
2. Buying calls and puts, cash-secured puts
3. Spreads (defined risk)
4. Naked selling (undefined risk)

Answer honestly. Level 1 or 2 is a fine start; add spreads when you are ready.

## The pattern day trader rule

The old rule: in a margin account under $25,000, four or more day trades (open and close the same position the same day) within five business days flagged you as a "pattern day trader" and restricted the account.

**It is being retired.** FINRA replaced it with intraday margin standards (Regulatory Notice 26-10), effective June 4, 2026, with brokers allowed to phase in until October 20, 2027. **Ask your broker which rule your account is under.** Trades held 30 to 45 days rarely trigger it, and cash accounts were never subject to it.

## Defined risk first

**Defined risk** means you know the worst case in dollars before you enter: put credit spreads, call credit spreads, iron condors. **Undefined risk** means the loss can grow far beyond the credit: naked puts, strangles, naked calls.

For the first year, use defined-risk spreads, cash-secured puts, and covered calls on shares you own. A cash-secured put is technically undefined until zero, but the cash covers it, so the worst case is known (and large, see file 02).

## Position sizing

| Guide | Number | Source |
|---|---|---|
| Max loss per defined-risk trade | 1 to 3 percent of the account | tastylive, "Dr. Jim Schultz Says Cap Your Buying Power at 50%" (2026) |
| Each trade's share of the portfolio | About 5 percent or less | tastylive, "Number of Occurrences Explained" (2016) |
| Total buying power in use | 20 to 25 percent low, 45 to 50 percent at most | Schultz segment above |

**The honest problem:** one cash-secured put in a small account breaks the 5 percent guide almost every time (a $15 strike is $1,500, which is 15 to 30 percent of the account). You have two honest choices:
- **Spreads** sized to 1 to 3 percent max loss: $50 to $300 per trade on these accounts.
- **The wheel**, accepting the concentration knowingly: one or two names, stocks you would own, strike x 100 at most 30 percent of the account (the rule card below), and the rest in cash.

What you never do is size by the margin number. Size by what you can actually lose.

## How many positions

- With spreads at 1 to 3 percent each and a 50 percent cap, the money allows many positions. Your attention does not. **Three to five open at once** is plenty for someone with a full-time job (our judgment, not a study).
- Spread them across unrelated names. Two trades on gold and silver, or on two chip makers, are really one bet. A small-account trader made exactly this point after a year of the 45-day method (file 04).

## What NOT to do

| Don't | Why |
|---|---|
| **Buy cheap far out-of-the-money calls as lotto tickets** | Low delta means a low chance of paying off, and time decay eats them daily. Fun once, a leak as a habit. |
| **Hold short options through earnings** | A report can gap the stock past your strike overnight, before you can act. Novavax fell about 30 percent in one day in August 2022 after cutting its forecast (file 02). |
| **Sell naked calls** | A stock has no ceiling, so the loss has none either. Brokers reserve it for the highest approval level for good reason. |
| **Average down on a falling stock** | Selling more puts on a name that keeps dropping doubles a losing bet. What you paid is not a reason; today's price and your rules are. |
| **Size up to win back a loss** | The urge to "make it back fast" is how small losses become account-ending ones. |

## Taxes, the basics

*Not tax advice. See a tax professional before your first year-end.*
- **Short-term gains.** Most option trades last under a year, so gains are short-term and taxed federally at your ordinary income rate.
- **Expired options you sold.** The premium is a short-term capital gain (IRS Publication 550).
- **Assigned puts.** The premium lowers your cost basis in the shares you bought (Publication 550).
- **Wash sales.** If you sell at a loss and buy the same or a "substantially identical" security, **including an option to buy it**, within 30 days before or after, the loss is deferred (investor.gov, citing Publication 550). Re-entering a name with a put right after selling it at a loss can trigger this.
- **California** has no lower rate for long-term gains; it taxes all capital gains as ordinary income (California Franchise Tax Board, "Capital gains and losses").
- **Index options** such as SPX can get different federal treatment (Section 1256, reported on IRS Form 6781). Ask a pro before trading them.

Your `trade-log.csv` plus the broker's 1099-B is what a tax pro will want.

## Brokers that fit

Described neutrally. No endorsement; compare current fees and features yourself.

| Broker | What it is known for | Practice mode |
|---|---|---|
| **tastytrade** | Built by the tastylive founders, options-first; IV rank and probability figures on the trade screen | Reviews we found say no retail paper mode; check |
| **Charles Schwab** | Large full-service broker; runs the thinkorswim platform | thinkorswim paperMoney (simulated trading with live data) |
| **Fidelity** | Large full-service broker; options by approval tier | Check what it offers today |
| **Interactive Brokers** | Wide market access, detailed margin rules | A separate paper trading account |

For a fully scriptable practice account, Alpaca's paper API has options enabled by default (file 07).

## The starter rule card

The `/trade-check` skill reads this table. Change any number you like, but change it here, in writing, before a trade, never during one.

| Check | Starter rule | Source |
|---|---|---|
| Account | Paper only until the gate in file 07 is passed | Our rule |
| Strategy | Cash-secured put, covered call, put or call credit spread, iron condor; jade lizard on paper only after 20 logged trades. Nothing naked except a fully cash-secured put. | Files 02, 03, 04 |
| IV rank | 30 or higher to sell premium | tastylive, "IV Rank Explained" (2026) |
| Days to expiration | 30 to 45, aim for about 45 (every strategy) | tastylive beginner course (2025); QuantWheel guide (30 to 45 for the wheel) |
| Short strike delta: cash-secured puts and covered calls (the wheel) | 0.20 to 0.30 | QuantWheel guide: 0.20 conservative, 0.30 standard (file 02) |
| Short strike delta: credit spreads, iron condors, jade lizard (a separate band) | 0.16 to 0.30 | 0.16 is about one standard deviation (tastylive, Butler, 2016); 0.30 is the same top as the wheel |
| Earnings | No earnings date between today and expiration. Unknown date counts as a fail. | Heitkoetter (file 02) |
| Liquidity | Bid/ask gap at most 10 percent of the option's mid price; open interest at least 100 at the strike | Our judgment, a beginner default, not a study |
| Defined-risk size | Max loss at most 3 percent of the account | tastylive, Schultz (2026) |
| Cash-secured put size (also the jade lizard's put) | Strike x 100 at most 30 percent of the account: a strike of $15 or less at $5,000, $30 or less at $10,000 | Our judgment for a 5 to 10K account, not a study |
| Total committed | At most 50 percent of the account in use | tastylive, Schultz (2026) |
| Open positions | At most 5 | Our judgment |
| Exit plan | Written before entry: take profit at 50 percent, decide at 21 days left | tastylive (file 04) |
| Never | Naked calls, 0DTE, holding through earnings, sizing up after a loss | This file |

## The first months: expect 4 to 6 months to reach the gate

Why that long: with at most five open positions and trades held about two to four weeks each, roughly five to eleven trades close in a month at full pace, so 30 closed trades takes about three to six months, and the first month is slower (our arithmetic from the rule card, not a study). Do not rush it by breaking the position cap.

| When | Do this | Done when |
|---|---|---|
| Month 1 | Read files 01 to 04. Open a paper account. Set the paper balance to your real planned size (or pretend it is). Copy the rule card into your own words. Start with one or two paper trades a week. | You can explain delta, IV rank and assignment out loud; first trades logged |
| Months 2 to 3 | Keep up to five open: put credit spreads and cash-secured puts, a new one each time a slot frees up. Every one goes through `/trade-check` and into `trade-log.csv`. Practice management: close at 50 percent, act at 21 days, roll one trade for a credit, let one get assigned and sell a covered call. Live through one earnings season without breaking the earnings rule. | About 15 closed trades; you have handled a loser by the rules |
| Months 4 to 6 | Keep the same pace. Grade every closed trade each month. Rewrite the rule card where it failed. Check the gate in file 07 each month. | Gate passed, or a written reason why not yet |
| After | If the gate is passed: real money, **one** defined-risk contract at a time, same log, same checks. | |
