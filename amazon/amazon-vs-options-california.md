# Amazon or options? The California version

Checked 2026-11-12. Fees and tax rules change, so every number here has its source at the bottom; check the live page before you pay anything. This is a comparison, not financial or tax advice. Have a CPA look at your own situation before you file.

## The short version

- Both can start small in California, and neither needs an LLC on day one.
- **Amazon wholesale** costs about $70 to $75 a month in fixed tools before you sell anything (Amazon's $39.99 plan plus Keepa's €29), takes 5 to 15 hours a week at the start, and pays your phone skills. The hard part of wholesale is getting brands to say yes, and that is a sales job.
- **Selling puts (the wheel)** costs nothing a month at a commission-free broker, takes a few hours a week once the rules are set, and pays patience. With $5,000 the rule card in `options/06` allows **one or two** positions, each with strike x 100 at most 30 percent of the account: a strike of **$15 or less** ($1,500).
- In the model below, one put on a $15-or-lower strike pays **about $25 to $65 for 45 days** inside the rules, not $200 to $300 every two weeks. Bigger credits only come from more risk (a strike closer to the price) or more capital than a $5,000 account has.
- You can practice both without risking a dollar. For options, real money comes only after the paper gate in `options/07` (30 closed paper trades over at least 90 days, rules followed); for Amazon, only after a product passes `/first-order`.
- The Claude plan you use costs the same either way.

## Side by side

| | Amazon wholesale, as a sole owner | Selling puts (the wheel) |
|---|---|---|
| Monthly cost before any sale | Professional plan $39.99, plus Keepa (about €29) | Often $0 commission; small regulatory and per-contract fees vary by broker |
| California filings | None required under your own name. Seller's permit optional (see below) | None |
| If you form an LLC | $70 to file, then **$800 a year from the first year**, plus $20 every 2 years | Not needed |
| Insurance | Required once you pass $10,000 of sales in a month, and from the first sale in Amazon's enhanced safety categories | None |
| Tax on profit | Federal income tax + **15.3% self-employment tax** + California 1% to 12.3% (13.3% over $1 million) | Federal income tax (gains held a year or less are taxed like pay) + California 1% to 12.3% (13.3% over $1 million). **No self-employment tax** |
| Hours a week | 5 to 15 to start: research, calls, shipping in | 1 to 3 once the rules are set |
| What $5,000 does | Buys one or two small first orders. The money comes back, with profit or not, as the units sell | Up to $1,500 (30 percent) sits as collateral for one put with a strike of $15 or less; the rest stays in cash. It is only spent if you get assigned |
| Main risk | The product slows, the price drops, fees eat the margin, account problems | The stock drops hard and you own 100 shares at a loss, with up to $1,500 (30 percent of the account) tied up in one name |
| Does your phone skill help? | **Yes, it is the edge.** Most beginners quit at the calling step | No |
| Grows with | More brands and reinvested profit | More capital |

## California details

### If you sell on Amazon

- **Sole owner first.** Selling under your own name needs no state entity and no state entity fee. Many cities still want a business license or tax certificate even for a home business, so check your city's website.
- **Seller's permit.** If every sale goes through Amazon, California does not require you to register (CDTFA Publication 109). You can still buy inventory without paying sales tax by giving the supplier a resale certificate that explains why you hold no permit, plus the marketplace's permit number. If a supplier insists on a permit number anyway, the permit costs nothing to register; CDTFA can ask for a security deposit sized to the taxable sales you expect.
- **EIN.** Get a free federal tax ID from irs.gov and put it on supplier forms instead of your Social Security number. Never pay a website for one.
- **LLC.** $70 to file, then the $800 annual tax every year starting with the first (the first-year break only covered LLCs formed in tax years 2021 to 2023), plus a $20 statement every two years. An extra LLC fee starts at $250,000 of total California income ($900 at that first tier), and that income counts sales, not profit. Plenty of sellers start as a sole owner with insurance and form the LLC once the profit is real; ask the CPA when.
- **Insurance.** Commercial liability insurance of at least $1 million per occurrence within 30 days after you pass $10,000 of gross sales in a month. Since 2026-11-02, products in Amazon's enhanced safety categories (children's products, cosmetics, ingestibles, lithium batteries and others) need it from the first sale.
- **Taxes.** Self-employment tax is 15.3% (12.4% Social Security plus 2.9% Medicare) on 92.35% of net profit. The Social Security part stops at $184,500 for 2026, and your paycheck counts toward that first. Then federal and California income tax on top. Set money aside every month and pay quarterly estimates.

### If you sell puts

- **No filings, no entity, no license.**
- **Taxes.** California taxes every capital gain as ordinary income, 1% to 12.3% (13.3% on income over $1 million), with no lower long-term rate. Federally, gains on positions held a year or less are taxed at your normal rate. Option premium from your own investing is not subject to self-employment tax. Losses offset gains, plus up to $3,000 a year against other income, and wash-sale rules apply.
- **Approval.** The broker has to approve you for options. Cash-secured puts and covered calls sit at the lowest levels. Alpaca's paper (practice) account has options turned on by default.

## What one put on $5,000 really pays

A cash-secured put means you agree to buy 100 shares at the strike price if the stock is below it at expiration, and you get paid a credit up front for that promise. The broker holds strike x 100 in cash the whole time. $5,000 could cover a strike up to $50, but the rule card in `options/06` caps one put at 30 percent of the account, so the strike is **$15 or less**.

The table models a $16 stock and a put that expires in 45 days (the rules allow 30 to 45). **Delta** is the market's rough odds that you end up buying the shares; the rules allow 0.20 to 0.30 for a cash-secured put.

| How jumpy the stock is (implied volatility) | Strike | Delta | Credit for 45 days | On the cash held | Share of $5,000 | Passes the delta rule? |
|---|---|---|---|---|---|---|
| Steady (30%) | $15, 6% below | 0.24 | $25 | 1.7% | 30% | Yes |
| Normal growth stock (45%) | $14.50, 9% below | 0.23 | $37 | 2.6% | 29% | Yes |
| Jumpy (70%) | $14, 12.5% below | 0.25 | $65 | 4.6% | 28% | Yes |
| Jumpy (70%) | $15, 6% below | 0.34 | $104 | 6.9% | 30% | No: too close to the price |
| Normal growth stock (45%) | $13, 19% below | 0.08 | $9 | 0.7% | 26% | No: pays almost nothing |

How to read it: further below the price is safer and pays less. Inside the rules, one contract on a $5,000 account earns tens of dollars per 45 days, not hundreds. The $104 row shows where bigger credits come from: a strike close to the price on a jumpy stock, with about one chance in three of being handed 100 shares of a stock that moves a lot. Rows marked Yes meet the delta, days and size rules only; IV rank, the earnings date and liquidity still have to pass on a live chain through `/trade-check`.

These are model prices (Black-Scholes, flat volatility, 4% interest, 45 calendar days, a $16 stock), recomputed in Python on 2026-11-12. Real option chains usually pay somewhat more for puts further below the price, so check a live chain before trusting any row.

### The risk, in one example

You sell a $14.50 put on a $16 stock and collect $37. Bad news hits and the stock opens at $12, down 25 percent. You must buy 100 shares at $14.50 ($1,450) that are now worth $1,200. That is -$250, plus the $37 you kept: **-$213**, about six full credits gone, and 29 percent of your $5,000 now sits in one stock. The wheel's next step is selling calls above your cost while you wait for it to come back, which can take months. Small steady credits, with a rare big hit, is the whole trade.

## Which one fits you

- **The case for options first:** everything is digital, there is no inventory, no shipping, no monthly tools, no California business paperwork, and it fits around a full-time job.
- **The case for Amazon first:** wholesale rewards exactly what you are best at. Getting a brand on the phone and getting approved is the step most people never finish. Each brand you open keeps paying with reorders, and the business can grow past what $5,000 of collateral can.
- **Time:** Amazon is front-loaded (setup, calls, first shipments). Options is steady but needs rules you follow when you are nervous.

## Decide without spending a dollar (the paper phase)

1. **Options on paper.** Open a free paper (practice) account. Make two or three paper trades a week with Claude walking you through each one through `/trade-check`, and write down every trade and why. The `options/` folder in this repo is the kit for this.
2. **Amazon on paper.** Run 20 product checks and make 30 brand calls with the method in this folder. No money until a product passes `/first-order`.
3. **Real money only after the gates.** Options: only after the paper gate in `options/07` (30 closed paper trades over at least 90 days, rules followed). Amazon: only after a product passes `/first-order`. Then read your notes and put money where you were careful, consistent, and enjoyed the work.

## Sources (checked 2026-11-12)

- Amazon selling plans and referral fees: [sell.amazon.com/pricing](https://sell.amazon.com/pricing)
- Amazon insurance, both triggers: [Novadata on the 2026-11-02 change](https://novadata.io/resources/news/amazon-liability-insurance-enhanced-safety-categories-november-2026), [Jungle Scout summary](https://www.junglescout.com/blog/amazon-seller-insurance/) (check the live requirement in Seller Central)
- Marketplace sellers and permits: [CDTFA Publication 109](https://cdtfa.ca.gov/formspubs/pub109/online-marketplaces-and-fulfillment-centers.htm), [CDTFA Marketplace Facilitator guide](https://cdtfa.ca.gov/industry/MPFAct.htm), [CDTFA Regulation 1668 (resale certificates)](https://cdtfa.ca.gov/lawguides/vol1/sutr/1668.html)
- Seller's permit cost and deposits: [CDTFA Publication 107](https://cdtfa.ca.gov/formspubs/pub107/)
- LLC tax and fee: [FTB LLC page](https://www.ftb.ca.gov/file/business/types/limited-liability-company/index.html), [FTB 3522 instructions for 2026](https://www.ftb.ca.gov/forms/2026/2026-3522.pdf), [FTB Form 568 booklet](https://www.ftb.ca.gov/forms/2025/2025-568-booklet.pdf)
- LLC filing and statement fees: [California Secretary of State business FAQs](https://www.sos.ca.gov/business-programs/business-entities/faqs) (check bizfileonline.sos.ca.gov for the current fee)
- California taxes capital gains as ordinary income: [FTB capital gains](https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html)
- Self-employment tax and the 2026 wage base: [IRS Topic 751](https://www.irs.gov/taxtopics/tc751), [SSA contribution and benefit base](https://www.ssa.gov/oact/COLA/cbb.html), [2026 Schedule SE instructions](https://www.irs.gov/instructions/i1040sse)
- Capital loss limit: [IRS Topic 409](https://www.irs.gov/taxtopics/tc409)
- Alpaca paper accounts and options: [Alpaca options docs](https://docs.alpaca.markets/us/docs/options-trading)
- Keepa price: [RevenueGeeks summary](https://revenuegeeks.com/software/keepa/pricing) (check keepa.com)
