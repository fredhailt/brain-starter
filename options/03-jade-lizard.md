# 03. The jade lizard

An intermediate trade. Read files 01 and 02 first, and wait until you have about 20 paper trades behind you before trying it.

## What it is

A jade lizard has three legs, all with the same expiration:

| Leg | Action | Why |
|---|---|---|
| 1 | **Sell a put** below the stock price | Collects most of the premium. This is the risky side. |
| 2 | **Sell a call** above the stock price | Collects more premium |
| 3 | **Buy a call** a little higher than leg 2 | Caps the loss on the call side |

Legs 2 and 3 together are a **short call spread** (also called a call credit spread). So a jade lizard is a short put plus a short call spread.

## The one rule that makes it a lizard

> **Total credit for all three legs must be greater than the width of the call spread.**

The **width** is the distance between the two call strikes. If the stock rallies far above both calls, the call spread loses its full width. If you collected more than that width in total, you still keep money. That is what "no upside risk" means.

The rule is stated plainly in a 2026 tastylive segment with Liz Dierking and Chris Vecchio: structure the trade for a net credit greater than the call spread width and the upside cannot lose ("The Jade Lizard Beat the Strangle in Every Backtest", tastylive, 2026).

**No upside risk is not no risk.** All of the risk moves to the downside, through the short put. If the stock falls hard, you lose like a short put, cushioned only by the total credit.

## When it fits

| Condition | Why |
|---|---|
| **High implied volatility** (high IV rank) | It is a premium-selling trade. In the same segment Dierking says she does not sell premium at all when IV is low. |
| **Neutral to bullish view** | You profit if the stock stays flat, rises a little, or falls a little. |
| **Normal skew** (puts pricier than calls) | Dierking's condition: the lizard works when puts carry higher implied volatility than calls, which is normal for stock indexes. On a stock where calls are bid up ("call skew"), the lizard makes you buy the most expensive call on the board. |
| **No earnings or big event before expiration** | The short put is exposed to a gap down. |

## A worked example

*Every number is an **illustration**. Not a real stock or quote.*

Stock XYZ at $50, IV rank high, about 45 days to expiration.

| Leg | Action | Premium |
|---|---|---|
| 1 | Sell the $45 put | +$1.40 |
| 2 | Sell the $55 call | +$0.75 |
| 3 | Buy the $56 call | -$0.35 |
| | **Total credit** | **$1.80** ($180 per lizard) |

- Call spread width: $56 minus $55 = **$1.00**
- Rule check: $1.80 is greater than $1.00. **Passes.**

What happens at expiration:

| XYZ at expiration | Result per lizard | Why |
|---|---|---|
| $60 (big rally) | **+$80** | Call spread loses $100; you keep $180 minus $100 |
| $55 to $45 | **+$180** | Everything expires worthless |
| $43.20 | $0 | Break-even: $45 minus $1.80 |
| $40 | **-$320** | Put is $5 in the money; $500 minus $180 |
| $35 | **-$820** | Put is $10 in the money |
| $0 (worst case) | **-$4,320** | The full downside of a short put |

**A version that fails the rule.** Same put for $1.40, but a wider call spread: sell the $55 call for $0.75 and buy the $57 call for $0.20. Total credit $1.95, width $2.00. Now a rally above $57 loses $5. Small, but the "no upside risk" promise is gone. Always check the rule with the real fill prices, not the prices you hoped for.

## Buying power

| Account type | What the broker holds (roughly) |
|---|---|
| **Margin account** | About the requirement for a naked put. Cboe's minimum for an uncovered stock option is built from the option's price plus 20 percent of the stock price, minus how far out of the money it is, with a floor of the price plus 10 percent of the strike (Cboe, "Overview of Margin Requirements for Options"). In the example: about $640. Brokers may require more, and the number grows when the stock falls or IV jumps. |
| **Cash account or IRA** | Usually the full put strike in cash ($4,500 here, less the credit), if the broker allows the trade at all. Some also hold the call spread width. Check your broker. |

## Why it is harder in a small account

1. **The real risk is the put, and the put is big.** The example ties up $640 of margin, but the true worst case is $4,320. In a $5,000 account that is most of the money, in one trade. The rule card in file 06 sizes a lizard like a cash-secured put (put strike x 100 at most 30 percent of the account), so this $45-put example fails the size check at both $5,000 and $10,000; it would need a put strike of $15 or less, or $30 or less.
2. **The rule leaves little room.** To keep total credit above the call width you usually need a narrow call spread and a rich put. On cheaper stocks, the call spread often pays only a few cents, so the lizard collapses into a plain short put with extra commissions.
3. **Three legs, three fees, three bid/ask gaps.** On small premiums, those costs are a large share of the profit.
4. **Margin approval.** In many accounts the naked put needs a higher option approval level than a beginner gets (file 06).

For a USD 5,000 to 10,000 account, treat the lizard as **"careful"**: one contract at most, on a liquid stock or fund priced low enough that the cash-secured version fits your size limit, and only after the wheel feels routine.

## The backtest claim, and what we can and cannot say

**The claim.** In a 2026 tastylive segment, Liz Dierking said that a 10-year backtest she requested, run on funds with $1-wide strikes (she named SPY, IWM, GLD and DIA), found that mechanically opening a jade lizard every day beat mechanically opening a strangle (a short put plus a short call, both naked) time and time again. Her reason: the lizard gives up some upside credit but cannot lose on the upside, and that shape won over many years. She added that it only works with normal skew and high IV.

Source: "The Jade Lizard Beat the Strangle in Every Backtest. Liz Dierking Explains Why", tastylive, 2026, https://www.youtube.com/watch?v=P0E--FyX8pw

**What we could not verify.** The segment shows no numbers: no years, no win rate, no average profit, no management rule, no costs. We did not find the study published. Treat it as an experienced trader's recollection, not data.

**Two cautions of our own.**
- Those funds rose over most of that decade. In a rising market a naked call loses most often, so any trade that caps the call side would look good. That may say as much about the decade as about the lizard.
- The study used index and commodity funds. A single stock can gap down on bad news far more than an index, and the lizard's open risk is exactly that downside.

The best line in the segment is a warning, from co-host Chris Vecchio: a high probability of profit and a good expected value are not the same thing. Higher odds bought by giving up credit are not an edge by themselves.

## Lizard rules to copy into your rule card

1. Total credit greater than call spread width, checked at the actual fill.
2. High IV rank, normal skew, neutral to bullish view.
3. No earnings or major event before expiration.
4. Size it by the short put's full risk, never by the margin number.
5. Same management as the wheel: take profit at 50 percent, decide at 21 days left.
