# The whole process, beginning to end

This is how a mature wholesale operation runs, written as numbered processes. You will not run all of them in month one. Weeks 1 to 4 are processes 1 to 7. The rest switch on as stock starts to move.

## How to read a process

Each process has:

- **Starts when:** what kicks it off.
- **Steps:** in order.
- **AI does / You do:** the split. The AI drafts, checks and logs. You decide, sign, pay, send and click inside Amazon.
- **FINISHED RESULT:** the one thing that exists when the process is done.
- **Ends as:** the short list of ways it can end. Every run ends as exactly one of them.

**The rule that makes this work:** a process is not finished until its FINISHED RESULT exists. A list of products "flagged for review" is not a finished result. A drafted PO nobody sent is not a finished result. If a run stops halfway, the next run picks it up first.

---

## 1. Find brands

- **Starts when:** your list of brands to call runs short (aim for 20 open leads).
- **Steps:**
  1. Open competitor storefronts, trade-show exhibitor lists, brands you know.
  2. List each brand's top products.
  3. Drop the ones you already called or already carry (check `tracker/brands.csv`).
- **AI does:** reads public storefronts and lists, removes duplicates, writes the list.
- **You do:** pick the categories you like; nothing else.
- **FINISHED RESULT:** a list of new brands, each with its top products and where it was found.
- **Ends as:** LEADS FOUND (with the count) / NO NEW LEADS (with why).

## 2. Check each lead on Keepa

- **Starts when:** a new brand lands on the list.
- **Steps:**
  1. `/product-check` on the brand's best sellers.
  2. A human looks at each chart that passed (the 3-month and 1-year views): PASS, FIX or KILL.
  3. The brand counts only if 3 or more products pass and clear the monthly bar in `01-find-products.md`.
- **AI does:** pulls the numbers, does the math, logs every row.
- **You do:** look at the charts. A screen without human eyes is how bad buys happen.
- **FINISHED RESULT:** every lead marked worth calling or not, with the reason.
- **Ends as:** WORTH CALLING / NOT WORTH IT (the gate that failed).

## 3. Find the right contact

- **Starts when:** a brand is marked worth calling.
- **Steps:**
  1. Read the brand's official site: wholesale, dealer, retailer, contact pages.
  2. Note the role to ask for, the main number, the wholesale email if public, the time zone.
  3. Distributor only: close it here.
- **AI does:** reads public pages and writes the call card (`/brand-call` PREP).
- **You do:** nothing until the call. Never the work ZoomInfo or CRM.
- **FINISHED RESULT:** a call card with who to ask for and how to reach them, each with its source.
- **Ends as:** READY TO CALL / NOT FOUND (what is missing) / DISTRIBUTOR ONLY.

## 4. Call and apply

- **Starts when:** a call card is ready and a call window is open.
- **Steps:**
  1. Call. Follow `02-call-brands.md`.
  2. Log the result the same day (`/brand-call` LOG).
  3. Send the follow-up email the same day.
  4. Fill in any application; you sign it.
- **AI does:** the card, the log, the email draft, the application fields it can fill from your saved business details (never your SSN).
- **You do:** the call, the send, the signature.
- **FINISHED RESULT:** one result on the brand's row, with a next step and a date.
- **Ends as:** PRICE LIST / APPLICATION / YES / MAYBE (call-back date) / NO (reason) / NO ANSWER (three touches, then dormant for 3 months).

## 5. Get the price list

- **Starts when:** an account is open but no price list has arrived.
- **Steps:**
  1. Ask for the price list (and MAP policy, minimums, how they take orders).
  2. Nudge once a week until it comes.
- **AI does:** drafts each nudge, tracks the dates.
- **You do:** send the nudges.
- **FINISHED RESULT:** the price list in hand, dated this year, and read the same day.
- **Ends as:** PRICE LIST IN / NUDGED (date sent) / GONE QUIET.

## 6. The mock (check every line of the price list)

- **Starts when:** a price list arrives.
- **Step 1, the screen:** every line matched to its Amazon listing and priced: PASS / NEEDS DISCOUNT / FAIL / CHECK (`/first-order` MOCK, rules in `03-first-order.md`).
- **The human look:** you read the Keepa chart of every PASS and NEEDS DISCOUNT line.
- **Step 2, the first order:** quantities for the PASS lines from your share of sales, at the right price-break tier, inside the money caps.
- **AI does:** the matching, the math, the file, the sizing, the discount ask.
- **You do:** the chart looks, and settle every CHECK line (often one question to the rep).
- **FINISHED RESULT:** a mock file with every line judged and the first order sized.
- **Ends as:** ORDER SIZED / NEEDS DISCOUNT (the ask written for the brand) / NOTHING WORTH BUYING (why).

## 7. The first purchase order

- **Starts when:** the mock ends ORDER SIZED.
- **Steps:**
  1. Claude drafts the PO and the order email.
  2. You read every line: item, UPC, units, case packs, cost, total.
  3. You send it (or place it on the brand's website).
  4. Wait for the brand to confirm; chase after 2 business days.
- **AI does:** the draft, the checks (approved to sell, right tier, ship-to is your prep center), the chase drafts.
- **You do:** review, send, and decide.
- **FINISHED RESULT:** the order sent and confirmed by the brand.
- **Ends as:** CONFIRMED / SENT, WAITING / HELD (what failed) / NO ORDER (why).

## 8. Pay and receive

- **Starts when:** the brand sends an invoice.
- **Steps:**
  1. Match the invoice to the PO, line by line: units and prices.
  2. Check the cash: does it fit, with money left for fees and a reorder?
  3. You pay it.
  4. The prep center counts what arrived against the PO.
- **AI does:** the match, the cash check, flags any difference.
- **You do:** pay. No agent ever moves money.
- **FINISHED RESULT:** the invoice paid and the goods counted against the PO.
- **Ends as:** PAID AND RECEIVED / DIFFERENT (units or prices do not match: ask the brand) / SHORT (missing units: ask the brand).

## 9. Prep and labels

- **Starts when:** goods arrive at the prep center (or at your door, if you prep yourself).
- **Steps:**
  1. Each unit gets its Amazon barcode label (FNSKU) and any prep Amazon's rules require (bags, bubble wrap, sets bundled).
  2. Boxes are packed and their contents recorded.
- **AI does:** reads Amazon's prep rules for each item and writes the prep sheet for the prep center.
- **You do:** send the prep sheet; approve the prep center's bill.
- **FINISHED RESULT:** every unit labeled, every box's contents known.
- **Ends as:** READY TO SHIP / PROBLEM (damaged, wrong item, wrong count).

## 10. The inbound shipment to Amazon

- **Starts when:** boxes are ready to ship.
- **Steps:**
  1. Create the shipment in Seller Central (you click it, or a tool that uses Amazon's official API).
  2. Labels on the boxes, carrier picks up.
  3. Watch it until Amazon finishes receiving.
  4. Compare units shipped with units Amazon received, item by item.
- **AI does:** reads the shipment status (from reports you download or through the API), does the compare, drafts the case for any short.
- **You do:** every click inside Seller Central.
- **FINISHED RESULT:** the shipment received, shipped and received matched item by item, every short sent to process 16.
- **Ends as:** MATCHED / SHORT (to claims) / STILL ARRIVING / STUCK RECEIVING.

## 11. Listing and the Buy Box

- **Starts when:** a PO is sent (get your offers ready before the boxes land).
- **Steps:**
  1. Create your offer on each existing listing (your SKU, condition new, your price).
  2. Check each one reads live and buyable once stock arrives.
  3. Every morning: which listings hold the Buy Box, which lost it, to whom, and why (price, Amazon came back, stock out).
- **AI does:** the offer file, the morning read, the "why we lost it" notes.
- **You do:** upload the file or make the edits in Seller Central.
- **FINISHED RESULT:** every product you bought live and buyable, with a daily Buy Box read.
- **Ends as:** LIVE / WAITING ON STOCK / BLOCKED (gated, missing info, Amazon error named).

## 12. Pricing and the repricer floor

- **Starts when:** a product goes live, and again whenever cost or MAP changes.
- **Steps:**
  1. Set a **floor** for each product: never below landed cost plus your minimum profit, never below MAP.
  2. Set a ceiling.
  3. Load the floors into a repricer (Amazon's own Automate Pricing comes with the Professional plan, or a paid repricer).
- **AI does:** works out every floor and ceiling from the landed cost, writes the file, flags any floor below MAP.
- **You do:** review the file and upload it.
- **FINISHED RESULT:** every live product with a floor at or above its landed cost, loaded in the repricer.
- **Ends as:** FLOORS LIVE / FILE READY (waiting on your upload) / BELOW COST (a product that cannot sell at a profit: to process 18).

## 13. Ads basics

- **Starts when:** a product has been live about 7 days and holds the Buy Box.
- **Know two words:** ACOS (advertising cost of sale) = ad spend / ad sales. **Break-even ACOS** = your profit margin before ads. Above it, every ad sale loses money.
- **Steps (every two weeks):**
  1. Wasted spend: search terms that spent and sold nothing. Add them as negatives.
  2. Harvest: search terms that sold. Give them their own exact-match targets.
  3. Bids: small steps toward break-even, never big jumps.
  4. Judge each change 14 days later; undo what did not work.
- **AI does:** reads the ad reports, writes each change as one numbered line with its money and its undo.
- **You do:** say go on each line, and apply it yourself in the ad console, or through the official Amazon Ads API.
- **FINISHED RESULT:** the fortnight's changes approved, applied, and recorded with their undo.
- **Ends as:** APPLIED / PROPOSED (waiting on your go) / NO CHANGE NEEDED.

## 14. Restock forecasting and reorder POs

- **Starts when:** weekly, every week.
- **Steps:**
  1. For each product: sales a week, units you own (at Amazon, at prep, inbound, on order), the brand's lead time.
  2. Weeks of cover = units owned / sales a week. Reorder when cover falls under lead time plus 30 days.
  3. Recheck each line on Keepa before it goes on the PO (`03-first-order.md`, Reorders).
  4. Draft the reorder PO. You send it. Chase the confirmation.
- **AI does:** the forecast, the draft PO, the recheck, the chase drafts.
- **You do:** review, send, pay.
- **FINISHED RESULT:** every brand that needs it has a reorder sent and confirmed.
- **Ends as:** CONFIRMED / SENT, WAITING / READY TO SEND / HELD (a check failed or the cash is short) / NOTHING TO ORDER (with the weeks of cover).

## 15. Returns

- **Starts when:** weekly.
- **Steps:**
  1. Read every customer return of the last 30 days from Amazon's returns report.
  2. Give each one its fate: back in stock, unsellable, removed, refunded without a return.
  3. Anything Amazon owes you goes to process 16.
- **AI does:** reads the report you download (or the API), sorts every return, writes the list.
- **You do:** download the report if there is no API connection.
- **FINISHED RESULT:** every return of the last 30 days with one fate.
- **Ends as:** BACK IN STOCK / UNSELLABLE (to process 18) / OWED (to claims).

## 16. Removals and reimbursement claims

- **Starts when:** monthly, and whenever process 10 or 15 finds a short.
- **Steps:**
  1. Find units Amazon lost, damaged, or refunded without getting back.
  2. Check which Amazon already paid for on its own.
  3. Write each remaining case with its proof (the shipment, the PO, the invoice).
  4. You file it in Seller Central and type the case number into the tracker.
  5. Read Amazon's payment back from the reimbursement report.
- **AI does:** the hunt, the proof, the case text, the follow-up.
- **You do:** file every case. Never let a bot file claims. Claim windows are short and change; check Amazon's FBA reimbursement policy page for the current windows.
- **FINISHED RESULT:** every unit Amazon owes you filed with a case number, and Amazon's payment read back.
- **Ends as:** READY TO FILE / FILED (case number) / PAID / NOT OWED (why).

## 17. Bookkeeping

- **Starts when:** weekly, monthly, quarterly, yearly.
- **Steps:**
  - **Weekly:** every bank and card line given its category.
  - **Monthly:** sales, Amazon fees, refunds, inventory bought, and **cost of goods** (what the units you sold cost you, from landed cost) booked; the books tied to the bank to the cent.
  - **Quarterly:** the profit for the quarter and the estimated tax payment.
  - **Yearly:** the package for your CPA.
- **AI does:** reads the payments report and bank exports you give it, drafts every entry with its reason.
- **You do:** approve entries in QuickBooks or a similar tool, pay taxes, sign returns. No agent changes the books without your yes.
- **FINISHED RESULT:** a closed month: every dollar booked and tied to the bank.
- **Ends as:** CLOSED / OPEN (what is missing) / WAITING ON YOU.

## 18. Selling leftovers on eBay and Walmart

- **Starts when:** stock is aging, a return is unsellable on Amazon as new, or a product sells below its floor.
- **Steps:**
  1. List each aged or leftover unit: its age, the storage fee date, the money at risk.
  2. Pick a way out: a price cut to the floor, a coupon, a removal to sell on eBay, or a write-off.
  3. eBay: honest condition, real photos, a fair price.
  4. Walmart Marketplace: worth applying once your Amazon account has a track record; Walmart reviews each application.
- **AI does:** the aging list, the way-out proposal, eBay listing drafts (title, description, price check).
- **You do:** approve each way out, publish the listings, ship eBay sales, approve write-offs.
- **FINISHED RESULT:** every aged or leftover unit with a way out started.
- **Ends as:** MOVING / LISTED / SOLD / WRITTEN OFF (with a photo, for the books) / HOLD (why).

## 19. The nightly wrap-up

- **Starts when:** every evening, 10 minutes.
- **Steps:**
  1. Yesterday's sales, units and returns.
  2. Account health: any warning or performance notice in Seller Central (you read it out or download it).
  3. Reorders due, POs waiting to send, confirmations to chase.
  4. Emails due tomorrow, with their drafts.
  5. Claims to file, cases to follow up.
  6. Your one list for tomorrow: the three things only you can do, first.
- **AI does:** writes the whole report.
- **You do:** read it and do the top three.
- **FINISHED RESULT:** one short report, and tomorrow's list for you.
- **Ends as:** WRITTEN / WRITTEN WITH GAPS (which section and why).

---

## Which processes run when

| When | Processes |
|---|---|
| Daily (10 minutes) | 11 (Buy Box read), 19 (wrap-up) |
| Weekly | 1, 2, 3, 4, 5 (the sales engine), 14 (restock), 15 (returns), 17 (weekly books) |
| When something arrives | 6 (price list), 7 (order), 8 (invoice), 9 and 10 (goods), 12 (new product) |
| Every two weeks | 13 (ads) |
| Monthly | 16 (claims), 17 (month close), 18 (aged stock) |

Who does which part, and the safety lines, are in `06-ai-captains-for-amazon.md`.
