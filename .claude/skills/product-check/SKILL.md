---
name: product-check
description: Check one Amazon product as a wholesale buy. Takes an ASIN, an Amazon link, a UPC, or a brand plus product name; pulls the price history, sales, sellers and fees with a source and date for each; does the profit math at the wholesale cost (or shows the highest cost that still works); gives PASS, FIX or KILL against the gates in amazon/01-find-products.md; and logs the row at the top of amazon/tracker/products.csv. Use on "/product-check", "check this product", "is this a good one", "run the numbers on", or any Amazon product link.
---

# Product check

The gates and their numbers live in one place: `amazon/01-find-products.md`. Read it first, every time.

## Rules for this skill

- Work and this business never mix: no company data, no work CRM or ZoomInfo, no work logins.
- Read public pages only. Never open, click or type inside Seller Central or any signed-in Amazon seller page with a browser tool. If a number lives only in Seller Central, ask the human to read it out or paste it.
- Never guess a number, never round a fee in your favor.

## Steps

1. **Pin down the product.** The ASIN (Amazon's 10-character product ID), title, brand, category, UPC and pack size. If you were only given a brand, list its five best sellers by sales and ask which to check.
2. **Pull the facts, each with where it came from and today's date.** Open the public Amazon listing and its Keepa chart with Claude in Chrome and read them like a buyer would:
   - the Buy Box price now, whether it is for new, and its 90-day range and average;
   - sales a month (the listing's "bought in past month" line, Keepa's monthly sold, or how often the sales rank drops);
   - how many FBA sellers there are now and over the last 90 days, and whether Amazon itself sells it and how often it wins the Buy Box;
   - the referral and FBA fees from Amazon's free Revenue Calculator;
   - restrictions: is the brand or category gated for this account (ask the human), is it hazmat, is it in an enhanced safety category that needs insurance from the first sale (see `amazon/00-setup.md`, step 10), any known IP complaints on the brand.
3. **Do the math.** Profit per unit = price - referral fee - FBA fee - inbound shipping per unit - prep per unit - buy cost. Margin = profit / price. Your share of monthly sales, and the money a month it makes: see "Your share of sales" in `amazon/01-find-products.md`. If the wholesale cost is unknown, never guess it: show the highest buy cost that still clears the margin floor.
4. **Verdict.** PASS when every gate clears. FIX when one gate misses but something specific would clear it (a lower cost, a bigger pack, waiting for the price to settle): name it. KILL when a hard gate fails. Give the reason in one plain sentence.
5. **Log it.** Insert the row right under the header of `amazon/tracker/products.csv` (newest first), with the sources column filled. Then answer in five lines or fewer: verdict, profit per unit, margin, money a month on your share, the one thing that decided it.

A product that sells a lot is still a KILL when Amazon is in stock today or keeps coming back, or when the price is sinking. Margin over 40%: check the pack size before you believe it.
