# Amazon wholesale, start here

This folder is a working kit for starting an Amazon wholesale business on the side, run with Claude Code. It is not a course. Open the repo in Claude Code and use it.

**Wholesale** means buying name-brand products in bulk **straight from the brand**, then selling them on Amazon listings that already exist, while Amazon stores and ships them for you. That Amazon service is called **FBA** (Fulfillment by Amazon). You never make a product. The hard part is getting brands to open an account for you, and that is a phone job. If you are good on the phone, that is your edge.

## Three rules before anything else

1. **Your day job and this business never mix.** Run it on a personal Claude plan, never the company's account (whatever goes into a company account is the company's to see). Never use the work ZoomInfo seat, the work CRM, work logins or any company data to find brands or contacts. Keep your copy of this repo on your personal GitHub, never the work one.
2. **Brand-direct, not distributors.** A middleman's cut rarely leaves a margin. If a brand says "we only sell through distributors", thank them and move on.
3. **No money moves until `/first-order` says PASS and you say go.** Claude drafts. You place the order, pay, send the email and click every button inside Amazon.

## Read in this order

| # | File | What it is |
|---|---|---|
| 1 | `00-setup.md` | Accounts and paperwork, in order, with costs |
| 2 | `01-find-products.md` | What a good wholesale product looks like, with the numbers |
| 3 | `02-call-brands.md` | Finding the right person, the call, the follow-up |
| 4 | `03-first-order.md` | The price list check, the first order, reorders |
| 5 | `04-money-and-mistakes.md` | Fees, cash flow, books, and the mistakes that cost real money |
| 6 | `05-the-whole-process.md` | The whole business, start to finish, as numbered processes |
| 7 | `06-ai-captains-for-amazon.md` | Which AI helper does which job, and the safety lines |
| 8 | `amazon-vs-options-california.md` | Amazon wholesale vs selling options, with California's fees and taxes |
| - | `tracker/` | Your product checks, brand calls and price list checks, newest first |

## The three commands

| Type this | What it does |
|---|---|
| `/product-check` | Checks one Amazon product as a wholesale buy: PASS, FIX or KILL, logged |
| `/brand-call` | Preps a call to a brand, then logs the result and drafts the follow-up email |
| `/first-order` | Screens a price list, sizes the first order, and checks it before money moves |

## The first 30 days

| Week | What you do | Done when |
|---|---|---|
| 1 | Setup (`00-setup.md`). Read `01-find-products.md`. Run `/product-check` on 10 products to learn the read. No money. | 10 rows in `tracker/products.csv` |
| 2 | List 30 brands from the lead sources in `01-find-products.md`. `/brand-call` before each call (it checks the brand's best seller first and drops the KILLs). Make your first 10 calls. | 10 rows in `tracker/brands.csv`, each with a next step and a date |
| 3 | Keep calling. Follow up on the days the tracker says. Fill in applications. | 30 calls logged, every one with a next date |
| 4 | When a brand sends a price list: `/first-order` screens every line, then sizes the first order. No price list yet: keep calling. | A first order checked and placed by you, or 30 more calls logged |

A first "yes" often takes more than 30 days. The calls compound: a brand that said "call me next quarter" is a warm lead, not a no.

## Words you will see

| Word | What it means |
|---|---|
| Seller Central | The website where you run your Amazon seller account: listings, stock, shipments, payments, reports |
| ASIN | Amazon's 10-character ID for one product listing |
| UPC | The barcode number on the product. The safest way to match a brand's item to an Amazon listing |
| Buy Box | The Add to Cart button. When several sellers offer the same product, Amazon gives the button to one at a time, and nearly every sale goes to whoever holds it |
| Keepa | A tool that charts every Amazon product's price, sales rank and sellers over time |
| Sales rank, rank drop | Amazon's best-seller number for a product in its category; lower sells more. On a Keepa chart, each sudden drop in that number is usually one sale |
| Private label | A product line one seller makes under its own brand and sells only itself. Nobody can buy it wholesale, so skip it |
| MAP | Minimum advertised price: the lowest price a brand lets sellers show. Brands that enforce it keep the price from collapsing |
| Price list | The brand's list of products and your cost for each. The start of every order |
| Mock | Your check of a whole price list: every line matched to its Amazon listing and judged |
| PO | Purchase order: the document that says what you are buying, how many, and at what price |
| Case pack | How many units come in the brand's shipping carton. You usually buy whole cartons |
| Landed cost | What one unit really costs once it reaches Amazon: your price plus freight, prep and labels |
| Margin | Profit per unit divided by the selling price |
| Prep center | A company that receives your stock, labels it to Amazon's rules and sends it in, for a fee per unit |
| FNSKU | The Amazon barcode label that goes on each unit you send in, so Amazon knows it is yours |
| Repricer | Software that moves your price up and down to win the Buy Box, never below a floor you set |
| Reimbursement claim | A case you file when Amazon loses or damages your units, so Amazon pays you for them |
| EIN | A free federal tax ID number for your business, from irs.gov |
| CDTFA | California's sales tax agency (California Department of Tax and Fee Administration) |
| Resale certificate | A form you give a supplier so it does not charge you sales tax on goods you will resell |
| Marketplace facilitator | A marketplace like Amazon that collects and pays the sales tax on the sales it handles for you |

## Thinking about options instead?

Read `amazon-vs-options-california.md` first, then the `options/` folder in this repo.
