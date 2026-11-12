# 05. Strategy cheatsheet

Eleven strategies on one table. "Fit" is for a USD 5,000 to 10,000 account run by a beginner: **yes**, **careful** (possible with tight size limits), or **no** (wait until the account and the experience are bigger). All formulas are per contract (100 shares). "Width" means the distance between the two strikes of a spread.

| Strategy | What it is | Market view | Max risk | Max gain | Capital needed | Fit |
|---|---|---|---|---|---|---|
| **Covered call** | Own 100 shares, sell a call above | Flat to slightly up | Share cost minus premium (stock to zero) | Call strike minus share cost, plus premium | 100 shares | **Careful**: shares up to $15 at $5,000, up to $30 at $10,000 (30 percent cap, file 06) |
| **Cash-secured put** | Sell a put, hold cash to buy the shares | Flat to up; happy to own | Strike minus premium (stock to zero) | The premium | Strike x 100 in cash | **Careful**: strikes up to $15 at $5,000, up to $30 at $10,000 (30 percent cap, file 06) |
| **Wheel** | Cash-secured puts until assigned, then covered calls until called away | Neutral to up, long term | Same as the put: the stock's full downside minus premiums | Premiums plus any gain up to the call strike | Strike x 100 in cash | **Careful**: one or two names at a time (file 02) |
| **Put credit spread** | Sell a put, buy a lower put | Neutral to up | Width minus credit | The credit | Width minus credit | **Yes**: the best first defined-risk trade |
| **Call credit spread** | Sell a call, buy a higher call | Neutral to down | Width minus credit | The credit | Width minus credit | **Yes** |
| **Iron condor** | A put credit spread plus a call credit spread | Range-bound | Wider side's width minus total credit | Total credit | Wider side's width minus total credit | **Yes**: go wide, not narrow (file 04) |
| **Strangle** | Sell an out-of-the-money put and call, both naked | Range-bound, high IV | Unlimited on the call side; large on the put side | Total credit | Margin, roughly 15 to 20 percent of the stock's value, and it grows when markets move (tastylive, Schultz, 2026) | **No**: needs a high approval level and room for big swings |
| **Jade lizard** | Sell a put plus a call credit spread; total credit above the call width | Neutral to up, high IV | Put strike minus total credit (downside only) | Total credit | Naked-put margin, or the full strike in cash; size it as put strike x 100 under the same 30 percent cap | **Careful**: one at most (file 03) |
| **Calendar** | Sell a near-dated option, buy the same strike further out | Flat near term; IV rising | About the net debit paid | Limited; depends on price and IV at the near expiration | The net debit | **Careful**: harder to manage, sensitive to IV |
| **Poor man's covered call** | Buy a deep in-the-money call far out (often a year or more), sell short-dated calls above it | Slowly up | About the net debit for the long call | Limited; roughly the gap between strikes minus the net debit | The net debit, far less than 100 shares | **Careful**: the long call can lose value fast if the stock drops |
| **Long call or long put** | Buy a call (bullish) or a put (bearish) | Big, fast move | The premium paid | Call: unlimited. Put: strike minus premium | The premium | **Careful**: time decay works against you; never a "lotto ticket" habit (file 06) |

## How to read "fit"

- **Yes** means defined risk, small capital, and losses you can size to 1 to 3 percent of the account (tastylive's guide for defined-risk trades, file 04).
- **Careful** means the trade fits only one or two at a time, or has a risk that is easy to underestimate.
- **No** means the downside or the margin need is too big for this account size today.

## The same ingredients, different dishes

Many of these are the same building blocks:
- A **strangle** plus two bought wings is an **iron condor**.
- A **strangle** plus one bought call above is a **jade lizard**.
- A **covered call** has the same payoff at expiration as a **cash-secured put** at the same strike (put-call parity).

Source: "Our Ultimate Guide To Strangles And Iron Condors" (tastylive, 2025) builds the condor and the lizard from a strangle exactly this way.

## Approval levels

Brokers unlock these in tiers, and the tiers differ by broker. Covered calls usually come first, then buying options and cash-secured puts, then spreads, and naked selling last. File 06 has more.
