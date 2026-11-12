---
name: first-order
description: The check before any money moves. Mode MOCK screens a brand's whole price list line by line (PASS, NEEDS DISCOUNT, FAIL, CHECK) into a mock file; mode ORDER re-runs the numbers today, reads the Keepa chart and the listing the way a careful buyer would, sizes the first order from your realistic share of sales, checks it against the money caps in amazon/03-first-order.md, and writes PASS, FIX or KILL with the draft PO lines for the human to place. Also covers reorders. Use on "/first-order", "check this price list", "run the mock", "should I buy this", "ready to order", "how many should I buy", "reorder", or before any purchase order.
---

# First order

The rules and caps live in `amazon/03-first-order.md`. Read it first, every time.

## Rules for this skill

- **No money moves until this skill says PASS and the human says go.** You never place an order, pay, send an email or click inside Seller Central. Draft and stop.
- Never guess a cost, a case pack or a match. Unsure is a CHECK.
- Every number carries its source and today's date.

## Mode MOCK (a price list arrived)

1. Copy `amazon/tracker/mock-template.csv` to `amazon/tracker/mock-<brand>-<YYYY-MM-DD>.csv`.
2. Read the price list. One row per line: brand item code, UPC, product, pack size, case pack, cost, price breaks.
3. **Match each line** to its Amazon listing: UPC first, then model number plus size, color and pack count. Fill MATCHED BY. Any other kind of match is a CHECK. No listing: NOT ON AMAZON.
4. **Price each matched line** the way `/product-check` does (Buy Box, fees, landed cost, profit, margin, your share, money a month).
5. **Verdict per line:** PASS, NEEDS DISCOUNT (fill COST IT NEEDS), FAIL (the gate, in plain words) or CHECK (the one question that settles it).
6. **Human eyes:** list every PASS and NEEDS DISCOUNT line with its Keepa link for the human to look at, and write their PASS, FIX or KILL in CHART LOOK.
7. Sort the file: PASS first, then NEEDS DISCOUNT, CHECK, FAIL, NOT ON AMAZON. Answer in five lines: lines checked, how many of each verdict, money a month across the PASS lines, the discount ask in one sentence, and whether the brand clears the "3 products and USD 300 a month" bar in `amazon/01-find-products.md`.

## Mode ORDER (sizing and the go / no-go)

1. **Fresh numbers.** Run `/product-check` again today on every line. A product that passed last week can fail today.
2. **Look at it like a buyer (Claude in Chrome, public pages only).** Open the one-year Keepa chart and the live listing:
   - Is the price steady, sliding or spiking? Did a stretch of out-of-stock make the price look better than it is?
   - Did sellers pile on lately? Does Amazon jump in and out?
   - Does the listing match what the supplier ships (pack size, color, model)? Any reviews about fakes, used items or wrong items?
   Write PASS, FIX or KILL and why, in plain words.
3. **Size the order.** Your share = monthly sales / (sellers sharing the Buy Box + 1), halved if Amazon wins the box. Order what `amazon/03-first-order.md` says from that share, at the right price-break tier, rounded to whole case packs only when the real case size is known.
4. **Money check.** Total landed cost = units x cost + freight + prep and labels + shipping into Amazon. It must fit the caps in `amazon/03-first-order.md` (no single brand above 30% of starting money), with cash left for fees and a reorder.
5. **Hand over.** The verdict, the reason, and the draft PO lines (item, brand item code, UPC, units, case packs, unit cost, line total, order total), plus a short order email draft. **Stop there. The human reads every line, sends it and pays.**
6. **After it ships,** fill in ORDERED ON, UNITS ORDERED and LANDED COST PER UNIT on each product's row in `amazon/tracker/products.csv`, and set the brand's STATUS to ORDERED in `amazon/tracker/brands.csv`.

## Reorders

Same as ORDER, with the reorder rules in `amazon/03-first-order.md`: current margin, cost is the higher of the list and the last price paid, count every unit you already own or have on order, lead time plus 30 days, never over 180 days of stock.
