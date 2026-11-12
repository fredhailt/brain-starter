---
name: brand-call
description: Prepare for, and wrap up after, a call to a brand about opening a wholesale account. Before the call it finds who to ask for from public sources, builds a one-page call card (opener, what to learn, what they will ask for, answers to the usual objections); after the call it logs the result in amazon/tracker/brands.csv and drafts the follow-up email for the human to send. Use on "/brand-call", "prep a call to", "I'm calling", "I just talked to", "log this call", "follow up with", "what's due today", or any brand name with "call" or "account".
---

# Brand call

Two modes. Ask which if it is not obvious: **PREP** (before) or **LOG** (after). "What's due today?" reads NEXT DATE in `amazon/tracker/brands.csv` and lists the brands due, oldest first.

## Rules for this skill

- **Never the work ZoomInfo, the work CRM or any company data.** Public sources only.
- Brand-direct only. A brand that sells only through distributors is a polite close, not a lead.
- You never send an email, submit a form or sign anything. Draft it and stop; the human sends.
- Never put a price, a discount, costs or margins in an email draft.

## PREP

1. Read `amazon/tracker/brands.csv` for this brand. If it is there, start from its last note and next step.
2. Confirm the brand is worth a call, by the rule in `amazon/01-find-products.md`: 3 or more of its products PASS in `amazon/tracker/products.csv` and together make USD 300 or more a month on your share. If fewer are checked, run `/product-check` on its best sellers first; stop if they come back KILL or the total falls short.
3. Find the door from the brand's **official website** (contact, wholesale, dealer or retailer pages), never a marketplace page. If something is unclear, write "not found" rather than guess. If the brand sells only through distributors, say so and suggest moving on.
4. Do the three-minute check from `amazon/02-call-brands.md`: one word for their line; their Amazon picture (ads, anyone under their website price, out of stock, stars and reviews); their rough monthly Amazon sales (top five products' "bought in past month" x price). Name the source of each point.
5. Write the call card, one phone screen:
   - **Who to ask for:** sales, wholesale, dealer or e-commerce manager; the owner at a small brand (a name only if it is public on their site).
   - **Their time zone** and the best call window.
   - **Opener (2 sentences):** an e-commerce company that wants to carry their line.
   - **What you noticed:** one point from the three-minute check.
   - **The three promises:** protect their price (MAP), keep best sellers in stock, easy to work with (prepay, full cases, FBA, no drop ship).
   - **The ask:** "What's the best next step to get an account set up?", plus name, title, email, direct line, MAP policy, opening minimum, and whether they sell on Amazon themselves.
   - **Likely objections** for this brand, with the answers from `amazon/02-call-brands.md`.
6. Say it back in five lines and stop. The human makes the call.

## LOG

1. Ask what happened in plain words, or read the notes pasted in.
2. Pick exactly one LAST RESULT: PRICE LIST, APPLICATION, YES, MAYBE, NO or NO ANSWER (see `amazon/02-call-brands.md`).
3. Write or update the row at the top of `amazon/tracker/brands.csv`: STATUS, LAST RESULT, LAST TOUCH (today), NEXT STEP, NEXT DATE, and WHAT HAPPENED in plain English. NO ANSWER follows the nudge days in `amazon/02-call-brands.md` (day 3, 7, 14, then dormant).
4. Draft the follow-up email (short, friendly, what they asked for attached or promised, one clear next step) and **stop**. The human reads it, edits it and sends it.
5. A PRICE LIST result: tell the human to run `/first-order` on it today.
6. If they said no, record why. Three of the same "no" reasons in a row means change the pitch; say so.
