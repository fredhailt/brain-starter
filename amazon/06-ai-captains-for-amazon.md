# AI captains for an Amazon business

A **captain** is one AI helper with one job: a seat with its own rule book, the processes it runs, and a finished result for each. Think of each one as a virtual assistant who knows one lane very well. The processes (`05-the-whole-process.md`) are the work; the captain is who runs them.

Give each seat a name. "Ask the restock buyer" is easier to say than "run the reorder process". Short first names work well, one per job: one for restock, one for the books, one for ads, one for buyer messages. Pick your own.

## The seats

| Seat | Runs processes | AI does | Only you do |
|---|---|---|---|
| Scout (researcher) | 1, 2, 3 | Finds brands on public storefronts and lists, runs the numbers, writes call cards | Look at the charts, make the calls |
| Mock pricer | 6 | Matches every price list line to its listing, prices it, sizes the first order | Look at the charts, settle the CHECK lines |
| PO writer | 7 | Drafts the PO and the order email, checks tiers and approvals, drafts the chase | Read every line, send, decide |
| Restock buyer | 14 | Forecasts, counts every unit you own, drafts reorder POs, rechecks Keepa | Approve, send, pay |
| Listings and Buy Box | 11, 12 | Daily Buy Box read, offer files, repricer floors from landed cost | Upload files, edit listings in Seller Central |
| Ads | 13 | Reads ad reports, writes each change as one line with its money and its undo | Say go per line, apply it |
| Claims | 10, 15, 16 | Compares shipped vs received, sorts returns, finds what Amazon owes, writes the case | File every case |
| Bookkeeper | 8, 17 | Matches invoices to POs, the cash check, drafts every books entry | Pay, approve entries, sign tax returns |
| Buyer messages | (as they come) | Drafts a reply to each buyer message in your voice, inside Amazon's deadline | Read and send every reply |
| Checker | all | Reads another seat's work before it reaches you. The checker is never the seat that did the work | Nothing; you read its verdict |
| Wrap-up | 19 | Writes the nightly report and your list for tomorrow | Read it, do the top three |

Start with one seat (the mock pricer pays off fastest, because every price list is hours of work by hand). Add the next only when the first runs well.

## The safety lines (never cross these)

1. **No browser bot inside Seller Central or any ad console. Ever.** No AI clicks, types, reads or downloads inside Seller Central, any signed-in Amazon seller page, or an ad platform's website (Amazon Ads, Google Ads, Meta, Microsoft), even when you are signed in and say it is fine. Amazon and the ad platforms act against automated screen control, and losing the account is losing the business. The AI reaches Amazon only two ways: **Amazon's official APIs**, or **files you download and hand it**. Public pages (a product listing, a Keepa chart, a brand's website) are fine to read.
2. **The AI drafts. You approve. Then the change happens.** Every change to Amazon, eBay, Walmart, an ad account, your books or your bank starts as a draft you say yes to, one item at a time. A seat's approval list is never permission to act on its own.
3. **No money moves without you.** No agent pays, transfers, orders, or changes the books on its own.
4. **Nothing goes to an outside person without you.** The AI drafts emails and buyer replies; you send them.
5. **Credentials are yours alone.** You type every password, key and tax ID. Keys live in a `.env` file that git ignores. The AI never prints, copies or stores one.
6. **Every write is logged with its undo.** Anything that changes something outside the repo (a price, a listing, a bid, a sheet, a file) gets one row in `tracker/action-log.csv` after it happens: when, which seat, what changed, where, the result, and how to undo it. Reads are not logged.
7. **Human eyes before money.** Before an order goes out or a listing goes live, a person (or the AI with Claude in Chrome on public pages) looks at the real Keepa chart and the real listing and writes PASS, FIX or KILL beside it.
8. **Numbers are computed, never eyeballed.** Every fee, total and margin is worked out in code, with its source and date.

## Connecting to Amazon the safe way

- **Before an API connection:** you download reports from Seller Central (payments, inventory, shipments, returns, reimbursements, ads) and give them to Claude. Slower, perfectly safe.
- **Amazon's Selling Partner API (SP-API)** lets a program read your own orders, inventory, shipments and reports. Setting it up is your job: a developer registration and an authorization inside Seller Central, done by your own hand. Then the keys go in your `.env` file, typed by you. Check Amazon's developer portal for the current terms.
- **Ads** have their own official API (the Amazon Ads API). Until it is connected, ad changes are written as lines you apply yourself in the console.

## How a seat is built in Claude Code

A seat is a skill: a folder in `.claude/skills/<seat-name>/` with a `SKILL.md` file. Keep it to one page.

```
---
name: mock-pricer
description: Checks every line of a brand's price list against Amazon. Use on "check this price list" or "run the mock".
---

# Mock pricer

My job: every price list line matched to its Amazon listing, priced, and judged.
Finished result: a mock file with every line PASS, NEEDS DISCOUNT, FAIL or CHECK.
Rules: amazon/03-first-order.md. Read it first, every time.
Not mine: sending anything, ordering, clicking in Seller Central.
Writes to: amazon/tracker/mock-<brand>-<date>.csv, newest first.
Your rulings (newest first):
- <date>: <what you said, in your words> -> <what I now do>
```

The `/first-order` skill in this repo is a working example.

## How a seat earns trust

1. **Shadow.** The seat makes its call; you make yours your own way; compare them.
2. **Assisted.** The seat drafts, you approve each item.
3. **Trusted.** Routine items run with a daily read by you. Money, outside messages and Amazon changes always stay at step 2.

A miss becomes a rule in that seat's `SKILL.md` the same day, with the date and your words, so it never happens twice. Never let a seat change one of your rules on its own; a new instruction that seems to clash with an old rule gets asked about, not assumed.
