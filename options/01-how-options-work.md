# 01. How options work

Every word you need, defined once, in plain English. Example numbers are **illustrations**, not real prices.

## The contract

An **option** is a contract that gives its buyer the right, but not the duty, to buy or sell a stock at a set price before a set date.

| Word | Meaning |
|---|---|
| **Call** | The right to **buy** 100 shares at the strike. Calls gain value when the stock rises. |
| **Put** | The right to **sell** 100 shares at the strike. Puts gain value when the stock falls. |
| **Strike** | The fixed price in the contract. |
| **Expiration** | The last day the contract exists. After it, the option is gone. |
| **Premium** | The price of the option, quoted per share. |
| **Contract** | One option controls **100 shares**. A premium of $1.20 costs $120 for one contract. |
| **Underlying** | The stock or fund the option is on. |
| **DTE** | Days to expiration. "45 DTE" means 45 days left. |

## In, at, or out of the money

- A call is **in the money (ITM)** when the stock is above the strike. A put is ITM when the stock is below the strike.
- **At the money (ATM)** means the stock is right at the strike.
- **Out of the money (OTM)** is the rest. An OTM option is all time value.

## Intrinsic and extrinsic value

Premium = **intrinsic value** + **extrinsic value**.
- **Intrinsic** is what the option would be worth if it expired right now. For a call: stock price minus strike, if positive.
- **Extrinsic** (also "time value") is everything else: the price of time and uncertainty. It melts to zero by expiration.

*Illustration:* stock at $53, a $50 call costs $4.00. Intrinsic is $3.00 ($53 minus $50). Extrinsic is $1.00. If the stock is still $53 at expiration, the call is worth $3.00 and the $1.00 of time value is gone.

## Buying versus selling

| | Buyer | Seller (also called "writer") |
|---|---|---|
| Pays or collects | Pays the premium | Collects the premium |
| Best case | Large gain if the stock moves far and fast | Keeps the premium |
| Worst case | Loses the premium | Can lose many times the premium |
| Time | Works against you | Works for you |
| Wins | Less often, bigger | More often, smaller |

Most of this folder is about **selling**, because time decay pays the seller. The price for that is that the seller's losses can be large. Tom Sosnoff describes it as trading unlimited profit for a higher chance of being right (The Investor's Podcast, episode TIP395, 2021).

## Buying power

**Buying power** is the amount of money the broker sets aside (or lets you use) for a position. It is not your cash balance and not your maximum loss:
- **Cash-secured put:** the full strike x 100, held in cash.
- **Defined-risk spread:** the spread's max loss, which stays fixed for the life of the trade.
- **Naked option in a margin account:** a broker formula, often around 15 to 20 percent of the stock's value, that grows when the stock moves against you or volatility jumps (tastylive, "Dr. Jim Schultz Says Cap Your Buying Power at 50%", 2026).

Size by what you can actually lose, not by the buying power number. Files 04 and 06 use the term.

## The greeks, in plain words

The greeks are measures your broker shows next to each option.

| Greek | Plain meaning | Rule of thumb |
|---|---|---|
| **Delta** | How much the option moves for a $1 move in the stock. | Also a **rough** guide to the chance the option finishes in the money. A 0.30 delta put is roughly a 30 percent chance of finishing ITM. It is an estimate from a pricing model, not a promise. |
| **Theta** | How much value the option loses per day from time passing. | Sellers have positive theta (they earn it). Decay speeds up as expiration nears. |
| **Vega** | How much the option moves when implied volatility moves 1 point. | Sellers lose when volatility jumps. |
| **Gamma** | How fast delta changes. | High near expiration and near the strike. This is why the last weeks of a trade get jumpy. |

Two notes on delta:
- The chance a stock **touches** your strike at some point before expiration is higher than the chance it **finishes** past it. tastylive teaches roughly double the delta as a quick estimate ("Why Most Traders Get Probability Wrong in Options", tastylive, 2026).
- A high chance of winning is not the same as a good trade. *Illustration:* a trade that wins $50 eighty-five times and loses $400 fifteen times ends down $1,750. Win rate is not profit.

## Implied volatility and IV rank

**Implied volatility (IV)** is the market's guess of how much the stock will move, worked backward from option prices. High IV means expensive options. Sellers like expensive options.

IV alone does not tell you if options are cheap or rich **for that stock**. A sleepy utility at 25 IV may be expensive; a biotech at 60 IV may be cheap. So traders compare IV to its own past year.

| Measure | Definition (from tastylive's glossary) |
|---|---|
| **IV rank** | Where today's IV sits between the past year's lowest and highest IV, on a 0 to 100 scale. Formula: (today minus year low) divided by (year high minus year low), times 100. |
| **IV percentile** | The share of trading days in the past year when IV was lower than today. |

These are different numbers. One huge spike in the past year can hold IV rank down for months while IV percentile looks normal. tastylive's definitions page treats IV rank above 50 as high; its presenters often use 30 as the line for selling premium ("IV Rank Explained: Why Options Sellers Wait for 30", tastylive, 2026). Pick one number, write it in your rules, and use it every time.

Very high IV rank often has a reason: an earnings report, a court ruling, a drug trial. Expensive options before a known event are expensive for a reason.

## Assignment

When an option buyer **exercises**, a seller somewhere is **assigned**: the seller of a put must buy 100 shares at the strike, the seller of a call must sell 100 shares at the strike.

- **At expiration**, options that finish at least $0.01 in the money are normally exercised automatically (the Options Clearing Corporation's "exercise by exception" process; brokers can set their own policies).
- **Early assignment** can happen any day on American-style options. It is most likely when the option is deep in the money, close to expiration, or (for calls) the day before the stock pays a dividend larger than the call's remaining time value ("Options Assignment Explained", tastylive, 2016).
- Assignment is chosen at random among sellers.
- If you are assigned on one leg of a spread and your long option is in the money, exercising the long option usually closes the trade at its stated max loss. Selling the long option for less than its intrinsic value has cost traders more than their max loss (same tastylive segment).

## American and European style

| Style | Can be exercised | Examples | Settles in |
|---|---|---|---|
| **American** | Any day up to expiration | Single stocks, ETFs such as SPY | Shares |
| **European** | Only at expiration | Index options such as SPX and XSP | Cash |

Source: Cboe's product pages. European style removes early-assignment risk, which is one reason index traders use it.

## Liquidity: can you get in and out?

"Liquidity is king" is a line from tastylive's long beginner course ("How To Trade Options in 2 Hours 12 Minutes and 4 Seconds", 2025). Check three things before every trade:

| Check | What it is | What you want |
|---|---|---|
| **Bid/ask spread** | The gap between the price buyers pay and sellers get | Narrow. *Illustration:* a $0.05 gap on a $1.00 option is small; a $0.40 gap is a toll you pay twice. |
| **Open interest** | How many contracts at that strike are open right now | In the hundreds or more |
| **Volume** | Contracts traded today | Steady trading across many strikes |

A wide spread is a hidden cost. You pay it entering and again exiting, and it is biggest exactly when you most want out.

## Next

Go to [02-the-wheel.md](02-the-wheel.md).
