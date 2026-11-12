# 04. The tastytrade way

Most of today's retail premium sellers learned their rules, directly or secondhand, from Tom Sosnoff and the tastylive network. This file lists those rules, names the segment each one comes from, and says where they deserve a second look.

## Who they are

- **Tom Sosnoff** co-founded the thinkorswim trading platform, which TD Ameritrade bought in 2009, then started **tastylive** (a free financial video network, launched 2011) and the broker **tastytrade**.
- tastylive airs hours of live trading shows a day plus short research segments ("Market Measures", "Options Crash Course", "Mike and His Whiteboard").

## Read this first: the grain of salt

**tastylive is the media arm of a broker.** That does not make the rules wrong. It does mean:
- Their studies are their own backtests. Most are shown as charts on air, without a published sample, a test on fresh data, or an outside audit.
- Their disclaimers say results are not shown net of all commissions and fees.
- Advice to trade **more often** is advice a broker benefits from.

Our approach: trust the **mechanics** (when to enter, when to exit) more than the **frequency** advice, and test both on paper.

## The core idea: sell premium

On The Investor's Podcast (episode TIP395, 2021), Sosnoff explained his preference for selling: options are fairly priced most of the time, so he would rather take trades with a high probability of success and limited profit than chase rare big wins. He points to two tailwinds:
1. **Stocks drift up over time**, which favors put sellers.
2. **Implied volatility tends to run above the volatility that actually follows.** tastylive's own research says this has held most of the time on the S&P 500. Academic work calls this gap the variance risk premium (for example Carr and Wu, "Variance Risk Premiums", Review of Financial Studies, 2009). It is real on average and fails hardest in crashes.

## The rules, with their sources

| # | Rule | What it means | Source |
|---|---|---|---|
| 1 | **Sell when IV rank is high** | Sell premium when options are expensive versus their own past year | "IV Rank Explained: Why Options Sellers Wait for 30" (tastylive, 2026) uses 30. tastylive's definitions page treats above 50 as high. Pick one and write it down. |
| 2 | **Enter about 45 days out** | Far enough for decent premium, close enough for decay to speed up | "How To Trade Options in 2 Hours 12 Minutes and 4 Seconds" (tastylive, 2025) |
| 3 | **Manage winners at 50 percent** | Buy back once you have kept half the credit, then redeploy | Same beginner course: manage at 50 percent or 21 days left, whichever comes first, and be consistent |
| 4 | **The 21 DTE rule** | At about 21 days left, close or roll, win or lose | "We Studied 15 Years of 21 DTEs Results" (tastylive, 2023), details below |
| 5 | **Small size** | Defined risk: 1 to 3 percent of the account per trade. Undefined risk: 3 to 7 percent of the account in buying power per trade, higher for small accounts. Total buying power in use: about 20 to 25 percent at the low end, 45 to 50 percent at most. | "Dr. Jim Schultz Says Cap Your Buying Power at 50%" (tastylive, 2026) |
| 6 | **Trade small, trade often** | Many small, similar trades let the odds play out; keep each one around 5 percent of the portfolio or less | "Number of Occurrences Explained" (tastylive, Mike Butler, 2016) |
| 7 | **Liquid underlyings only** | High open interest, volume across many strikes, narrow bid/ask | 2025 beginner course: liquidity comes before everything else |
| 8 | **Defined vs undefined risk** | Defined: max loss known at entry (spreads, condors). Undefined: loss can grow far past the credit (naked puts, strangles). | Same course; Schultz segment above |
| 9 | **Strangles vs iron condors** | Same trade, except the condor buys "wings" | "Our Ultimate Guide To Strangles And Iron Condors" (tastylive, 2025), below |

### Rule 4 in detail: why 21 days

The 2023 study sold 20-delta strangles at 45 days on SPY, IWM and QQQ and compared every fixed holding period. Its findings, as presented on air:
- Average profit per trade rose until about 24 days held (21 days left), then fell.
- Tail losses (the average of the worst 5 percent of trades) grew sharply in the last two to three weeks.
- Exits much earlier than about 20 days held had low average profit too.

So 21 days is not magic. It is roughly where a rising profit curve meets a rising risk curve, **for those three index funds, at that delta, from a 45-day start.** The figures were read off charts during a live show; no table was published. Treat 21 days as a sensible default, not a law of nature.

### Rule 5 in dollars

| Account | 1 to 3 percent of account (defined-risk max loss per trade) |
|---|---|
| $5,000 | $50 to $150 |
| $10,000 | $100 to $300 |

*Illustration:* a $1-wide put spread sold for $0.30 risks $70. A $5-wide spread sold for $1.50 risks $350, which is too big for either account.

### Rule 9 in detail: strangles vs iron condors

A **strangle** sells an out-of-the-money put and call. An **iron condor** is the same strangle plus a cheaper put bought below and a cheaper call bought above, which caps the loss on both sides.

| | Strangle | Iron condor |
|---|---|---|
| Credit | Larger | Smaller (you pay for the wings) |
| Max loss | Undefined | Defined |
| Buying power | Higher | Lower |
| Sensitivity to volatility | Much higher | Lower |
| Account needed | Margin, high approval level | Usually spread approval |

The same tastylive segment's research tip: if you trade iron condors, **go wide**. Narrow condors look attractive (the segment's example: make $8 while risking only $2) but rarely reach that profit. For a USD 5,000 to 10,000 account, the iron condor is the version that fits; the strangle does not.

## The 0DTE lesson: most close at 50 percent, the math says otherwise

0DTE means options that expire **the same day**. In a 2026 segment ("Most Zero DTE Traders Close at 50%. Liz and Jenny Show Why the Math Doesn't Work"), tastylive's Liz Dierking and Jenny Andrews walked through a same-day S&P put spread, $10 wide, sold at the expected move for $1.50. That risks $850 to make $150.

*Illustration of their point, using those figures:*

| Management | Profit per win | Wins needed to repay one full loss |
|---|---|---|
| Close at 50 percent | $75 | 12 (11 wins make only $825) |
| Let it expire | $150 | 6 |

When the credit is tiny compared with the risk, taking half of it may not pay for the losers. They cited a colleague's newer study that suggested not managing this exact setup at all, while noting that older studies favored managing and more data is still coming in.

**The lesson is bigger than 0DTE:** a management rule belongs to the trade it was tested on. The 50 percent rule was built on 45-day trades. Before borrowing any rule, do the arithmetic: how many wins does one full loss erase? (And 0DTE is not a beginner trade. Skip it.)

## The counterweight: a small account's view

A small-account trader who followed the 45-day method for a year ("I Traded the Tastytrade 45 DTE Strategy for a Year", Small Account Options Trading, 2026) named the problems the studies do not show:
- With a few hundred to a few thousand dollars, **every trade feels big**, so the method stops feeling mechanical.
- A small account **cannot diversify**. Two positions in related names (gold and silver, say) are really one bet.
- The edge only shows up over many occurrences. A small account may not survive the bad stretch before the many occurrences arrive.

## One claim we could not verify

A widely viewed video from another channel credits Sosnoff with a single favorite trade: a 12-delta put on S&P futures, 45 days out, closed at 50 percent. The quote is secondhand, and we could not find Sosnoff saying it himself. The video's "12 percent in 45 days" was measured against the margin posted, not the full market exposure the put carries, which is many times larger. **Always ask what a return is divided by.**

## What we keep

- 45 days in, 50 percent or 21 days out, consistently.
- IV rank as an entry filter, with one written threshold.
- Defined risk and small size first.
- Liquidity checked before every trade.
- Frequency advice treated with care, and every claim tested on paper.
