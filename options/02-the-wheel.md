# 02. The wheel

The wheel is the most common first strategy for option sellers. It is simple, it uses cash instead of borrowed money, and the worst case is owning a stock you already said you wanted. That last part is also its biggest risk.

## The cycle

```
 1. Sell a cash-secured put  --(expires worthless)-->  repeat step 1
          |
     (assigned)
          v
 2. You now own 100 shares
          |
          v
 3. Sell a covered call  --(expires worthless)-->  repeat step 3
          |
     (called away)
          v
 4. Shares sold. Back to step 1.
```

| Step | Term | What it means |
|---|---|---|
| 1 | **Cash-secured put (CSP)** | You sell a put and set aside enough cash to buy 100 shares at the strike. You collect the premium now. |
| 2 | **Assignment** | The stock finished below your strike, so you buy 100 shares at the strike. Your real cost is the strike minus the premium you collected. |
| 3 | **Covered call** | You own 100 shares and sell a call against them. You collect premium; you agree to sell at the call's strike. |
| 4 | **Called away** | The stock finished above the call strike, so your shares are sold at that strike. |

## Step zero: pick a stock you would happily own

The single test: **would I buy 100 shares at this strike today, with no option involved?** If the answer is no, do not sell the put. The wheel turns a "maybe" into ownership the moment the stock drops.

Good wheel candidates usually:
- are businesses or funds you understand and would hold through a bad quarter;
- have **liquid options** (narrow bid/ask, open interest in the hundreds, see file 01);
- have a share price your account can hold (table below);
- are not trading on a rumor, a buyout, or a meme.

A fat premium on a stock you would not own is a warning, not a gift. Premium is high because the market expects a big move.

## Choosing the strike and the date

| Choice | Common starting point | Source |
|---|---|---|
| **Days to expiration** | 30 to 45 days | tastylive's standard entry is about 45 days ("How To Trade Options in 2 Hours 12 Minutes and 4 Seconds", 2025); QuantWheel's guide says most wheel traders use 30 to 45 |
| **Strike by delta** | Put at about 0.20 to 0.30 delta | A convention in wheel guides; QuantWheel's strike-selection guide, for one, calls 0.30 standard and 0.20 conservative. Lower delta: less premium, fewer assignments. Higher delta: more premium, more assignments. |
| **Covered call strike** | At or above your cost basis | A common wheel convention, and plain arithmetic: below your basis, being called away locks in a loss. |

Delta is only a rough guide to the odds (file 01). Treat these as defaults you write into your own rules, not laws.

## Managing the trade

- **Take profits early.** Many premium sellers buy the option back once they have kept about half the premium, then start the next one. The 50 percent rule comes from tastylive's beginner course, which manages at half the credit or at 21 days left, whichever comes first. File 04 explains why.
- **Know the 21-day line.** If the trade has not hit 50 percent by about 21 days left, tastylive closes or rolls it, because the riskiest days are the last weeks (file 04).
- **Rolling for a credit.** To roll, you buy back your option and sell a later one in a single order. Only roll if the new option pays more than it costs to close the old one (a net credit), and ideally at the same or a lower strike for a put. If no credit roll exists, take the assignment. That is the wheel working, not failing.
- **Check the earnings date before you sell.** Do not let a short put stay open through an earnings report unless you are ready to own the stock after a gap down. Wheel teacher Markus Heitkoetter filters out any put that expires after the next report ("Selling Options During Earnings?", Rockwell Trading, 2022). His example: Novavax fell about 30 percent in one day in August 2022 after cutting its forecast.

## The real risk

**A cash-secured put is a short put.** If the stock goes to zero, you lose the strike times 100, minus the premium. The premium is a small cushion, not a shield.

And the covered call does not fix this. At expiration a covered call has the same payoff shape as a short put at the same strike (this identity is called put-call parity). Once you own the shares, you own their whole downside. The call only adds premium and caps your upside.

Put simply: **the wheel is a bet that the stock does not fall much, paid a little each month.** It wins most months and has one bad month that can erase many good ones.

## How much capital it takes

One cash-secured put needs the strike times 100 in cash. In a small account that is a big slice:

| Share price (about the strike) | Cash for one put | Share of a $5,000 account | Share of a $10,000 account |
|---|---|---|---|
| $10 | $1,000 | 20% | 10% |
| $15 | $1,500 | 30% | 15% |
| $20 | $2,000 | 40% | 20% |
| $25 | $2,500 | 50% | 25% |
| $30 | $3,000 | 60% | 30% |
| $50 | $5,000 | 100% | 50% |

Plain read: the rule card in file 06 caps one cash-secured put at 30 percent of the account (strike x 100), so the wheel fits strikes of **$15 or less at $5,000** and **$30 or less at $10,000**, one or two positions at a time. Above that, a single assignment ties up too much of the account. Many cheap stocks are cheap for a reason, so the "would I own it" test matters even more here. File 06 sets the size limits.

## A worked example

*Every number below is an **illustration**, rounded to keep the math easy. It is not a real stock, quote or recommendation.*

**Setup.** Stock XYZ trades at $25. You sell one put, strike $23, 38 days out, at about 0.25 delta, for $0.60.
- Premium collected: $0.60 x 100 = **$60**
- Cash set aside: $23 x 100 = **$2,300**
- Break-even: $23 minus $0.60 = **$22.40**
- Return on the cash: $60 / $2,300 = **2.6 percent** for 38 days
- Size check: $2,300 is 23 percent of a $10,000 account, inside the 30 percent cap. In a $5,000 account it would be 46 percent, over the cap, so there you would need a strike of $15 or less.

**Path A: the stock stays above $23.** At 50 percent profit the put costs $0.30 to buy back. You close it, keep $30, and sell the next put.

**Path B: the stock closes at $22 at expiration.** You are assigned 100 shares at $23. Your cost basis is $22.40. You sell a covered call, strike $24, 30 days out, for $0.50 ($50).
- If XYZ ends above $24, the shares are called away. Profit: ($24 minus $22.40 plus $0.50) x 100 = **$210** over both legs.

**Path C: bad news, the stock drops to $15 and stays.** You own 100 shares with a $22.40 basis. You are down **$740**. Closing winners at 50 percent, a win is about $30, so that is the profit from about 25 winning puts (or about 12 held all the way to expiration for the full $60). Selling calls at $24 now pays almost nothing, and selling them near $15 risks locking in the loss.

Path C is the one to plan for before you place Path A.

**A warning about annualizing.** 2.6 percent in 38 days works out to about 25 percent a year only if every cycle wins and the cash is always working. Path C shows why that number is fantasy. Always judge a wheel trade on the full cash at risk, never on a yearly figure.

## Wheel rules to copy into your rule card

1. Only names I would own at the strike, today.
2. Strike about 0.20 to 0.30 delta, 30 to 45 days out.
3. No short put open through an earnings report.
4. Take profit at 50 percent; at 21 days left, close or roll for a credit; otherwise accept assignment.
5. Covered calls at or above my cost basis, unless I have decided in writing to exit.
6. Size by the full strike times 100, never by the premium.

Run any proposed paper wheel trade through `/trade-check` in Claude Code before you place it.
