# PROCESS: <name>

<!-- Copy to captains/<captain>/processes/<name>.md (or anywhere it belongs). Fill every <...>.
     Write it AFTER running the process by hand at least once, so the steps are real. -->

**Captain:** <the seat whose knowledge runs it, or "none yet">
**Starts when:** <the trigger: a clock (when), a STATUS of READY on a sheet, the human's word>
**Finished result:** <the one thing that exists when it is done. Examples: "a purchase order drafted, priced and checked, its email drafted with the To field blank, in the ready-for-review folder"; "a trade ticket ready for the human: symbol, strike, expiry, size, max loss, exit plan, why">
**End states:** <every way it can end, e.g. DRAFTED | NOTHING TO DO | NEEDS YOU: <question> | FAILED: <why>>

## WHY IT EXISTS

<One or two lines, in the words of whoever asked for it, with the date.>

## THE STEPS

| # | Step | Who (machine / AI / human) | Reads | Writes | Done when |
|---|---|---|---|---|---|
| 1 | <verb + object> | machine | <file, sheet tab, API> | <file, sheet tab> | <a checkable fact> |
| 2 | <...> | AI | <...> | <...> | <...> |
| 3 | Human approves or cuts lines | human | <the draft> | <their answer, said in chat> | <answer recorded> |
| 4 | Verifier checks the result cold | AI (verifier) | <the result> | PASS or FAIL with proof | <PASS> |

Rules for the steps:
- One step, one owner. A step that is always the same is a script, not a model.
- The human appears only where only the human can act (a yes, a click, a signature).
- Every write outside the repo is one row on `records/ACTION-LOG.tsv` with its undo.

## HOW IT IS CHECKED

- **The proof a run worked:** <what to open or run, and what "good" looks like>
- **The lying test:** <an independent cross-check that would catch a false "done": a recount, a second source, opening the page>
- **Bev lane:** <the repeat decision inside this process that gets a shadow call, or "none yet">

## CLOCK AND LIMITS

- **Runs:** <by hand | daily at time | when a row turns READY>
- **Allowed to write:** <exactly what; everything else is read-only>
- **Kill condition:** <when to stop running it>

## HISTORY

| Date | Change | Why |
|---|---|---|
| <YYYY-MM-DD> | First written after <n> runs by hand | <...> |
