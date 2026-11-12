# The price list, the first order, and reorders

`/first-order` reads this page. Nothing gets bought until every box below is ticked and you decide to go. The numbers here are our house rules (a working wholesale business, 2026) unless a source is named.

## Step 1: the mock (check every line of the price list)

A brand's price list can have 20 lines or 2,000. Check all of them the day it arrives, because the best product on it is rarely the one you called about.

For every line:

1. **Match it to its Amazon listing.** UPC first; then model number plus size, color and pack count (see `01-find-products.md`). No match: mark it NOT ON AMAZON and move on.
2. **Price it.** Buy Box price today, fees, your landed cost, profit per unit, margin, your share of sales, money a month.
3. **Give it one verdict:**

| Verdict | Means |
|---|---|
| PASS | Clears every gate in `01-find-products.md` at the price list cost |
| NEEDS DISCOUNT | Would pass at a lower cost. Write the cost it needs, so you can ask the brand |
| FAIL | A hard gate fails. Write which one in plain words |
| CHECK | Claude is not sure of the match (pack size, color, model). A human looks before it counts |

4. **A human looks at the charts** of every PASS and NEEDS DISCOUNT line on Keepa: PASS, FIX or KILL, with a reason.

The mock is saved as a file in `tracker/` (see `tracker/README.md`). It is finished when every line has a verdict, or a CHECK with the question that settles it.

## Step 2: the first order

Only PASS lines, after the human chart look, with no CHECK left open.

### Before the first order

- [ ] Every line on the order passed `/product-check` **today**.
- [ ] Each line's Keepa chart and listing were looked at like a buyer: PASS, FIX or KILL, with a reason. A pack-size mismatch is fixed before anything else.
- [ ] New sellers in the last 30 and 90 days were counted. A pile-on means smaller, or not at all.
- [ ] Price breaks: each line is priced at the quantity tier you are actually buying (buying 15 at the "10+" price when "20+" is cheaper is money left behind).
- [ ] Any item you are not sure matches the Amazon listing exactly is confirmed with the rep.
- [ ] You are approved to sell every item (brand or category restrictions). Find this out **before** you build the order, not after.
- [ ] The account is open: application accepted, a price list dated this year, you know how they take orders, and the bill-to and ship-to addresses are set (ship-to is your prep center, not your home, unless you prep yourself).

### How many to buy

- **60 days of your share** of sales (your share is in `01-find-products.md`).
- **30 days** if the listing has under 20 reviews.
- **90 days** only if the other sellers will run out of stock within 30 days.
- At least 2 units, and never more than the whole listing sells.
- Round to whole case packs only when you know the real case size. Never round up on a guess.
- **Never size on the brand's minimum order.** If their minimum is many months of your share, ask for a smaller opening order or walk away. One real seller's brand minimums once came out to 1 to 6 years of stock.
- **Kit default for your starting money:** no first order with a single brand above 30% of your starting money. Keep cash for fees, freight and a reorder.

### The profit math

Profit per unit = Buy Box price - referral fee - FBA fee - your cost - freight and prep.

- Referral fee: 15% in many categories, with a $0.30 minimum in most ([sell.amazon.com/pricing](https://sell.amazon.com/pricing), checked 2026-11-12). Use the real category rate from Amazon's Revenue Calculator.
- Freight and prep: get real quotes. Until you have them, our planning placeholder is about $1.75 per unit for a small item (label plus freight into Amazon). Replace it the moment you know your own number.
- Margin = profit / Buy Box price. Money per month = profit x your monthly share.
- From order to sellable on Amazon has run about 70 days in our business. **Seasonal products must be ordered early**; a winter product that lands in March sits until November.

### The order itself

- Claude drafts the PO (item, brand item code, UPC, units, case packs, unit cost, line total, order total) and the order email.
- **You** read every line, send it, and pay.
- The order is done when the brand confirms it (a reply, an order acknowledgement, an invoice or a ship notice). No confirmation after 2 business days: chase it.

## Reorders

- Gate on the **current** Buy Box margin, not the one you bought at.
- Your cost is the higher of the price list and what you last paid.
- Count everything you already have: at Amazon, at your prep center, on the way in, and on open orders.
- Order enough for the brand's lead time plus 30 days. Never hold more than 180 days of stock (Amazon's aged inventory charges start at 181 days; see `04-money-and-mistakes.md`).
- Products selling under 1 a month: don't reorder.
- Before every reorder, recheck each line on Keepa: is the Buy Box really new (not used), is Amazon there, how many sellers, is the price still at least 1.3x your landed cost, will this quantity take more than 6 months to sell?
- One brand's order at a time.

## After it ships

Fill in ORDERED ON, UNITS ORDERED and LANDED COST PER UNIT on the product's row in `tracker/products.csv` (the latest order). Then, every month, check for units Amazon lost or damaged and file the claim; claim windows are short, and an unfiled claim is money left on the table.
