# Trackers

Plain CSV files that open in any spreadsheet app (or ask Claude to put them in a Google Sheet for your phone). Every row is dated, and the newest row sits at the top, right under the header.

**Once you fill these in, they are private business data.** Your brand list and costs are what a competitor would love to see. Keep your copy of this repo private, and never push a filled-in tracker to a public repo.

## The files

| File | What it holds | Written by |
|---|---|---|
| `products.csv` | Every product check: PASS, FIX or KILL and why, plus the latest order once you buy | `/product-check`, `/first-order` |
| `brands.csv` | Every brand you reach out to and where it stands | `/brand-call` |
| `mock-template.csv` | The header for a price list check. Each price list gets its own copy: `mock-<brand>-<YYYY-MM-DD>.csv` | `/first-order` |
| `action-log.csv` | Every change made outside this repo (a price, a listing, a bid, a sheet), with its result and how to undo it. Reads are not logged | Every AI seat, right after the change (see `../06-ai-captains-for-amazon.md`) |

## brands.csv

**STATUS** is one of: TO CALL, CALLED, APPLIED, ACCOUNT OPEN, PRICE LIST IN, ORDERED, DORMANT, NO.

**LAST RESULT** is the result of the latest call, one of: PRICE LIST, APPLICATION, YES, MAYBE, NO, NO ANSWER (see `../02-call-brands.md`).

Ask Claude "what's due today?" and it reads NEXT DATE.

## A mock file

One row per line of the brand's price list.

- **VERDICT:** PASS, NEEDS DISCOUNT, FAIL, CHECK or NOT ON AMAZON (see `../03-first-order.md`).
- **MATCHED BY:** UPC, or MODEL + SIZE/COLOR/PACK. A line matched any other way is a CHECK.
- **COST IT NEEDS:** for NEEDS DISCOUNT lines, the cost that would make it pass.
- **CHART LOOK:** the human's PASS, FIX or KILL after reading the Keepa chart.
- **FIRST ORDER UNITS:** filled in by step 2, PASS lines only.

The mock is finished when every line has a verdict, or a CHECK with the one question that settles it.
