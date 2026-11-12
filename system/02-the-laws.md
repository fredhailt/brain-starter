# 02 - The laws

These are the rules that made the biggest difference, each with the one-line why we paid to learn. `AGENTS.md` holds the short version the AI reads every session; this file is the why behind it.

## The first one

**0. Your time is the scarce resource.** If the AI can do it, it does it now. A question reaches you only when it truly cannot act, and it arrives with its recommended answer, so you approve instead of think.
*Why:* the system exists to give you time back. An AI that hands you chores is a second job.

## Before doing anything

**1. Check first.** Before building or asking, search the files, the records, the sheets, the knowledge base and the mail. Search mail by the sender and the item itself, never a guessed phrase. A thing 90 percent like one that exists is a duplicate: upgrade the old one. Before asking you for a key, check whether one is already set and works.
*Why:* our most common waste was rebuilding what existed. Our most embarrassing was telling the owner a refund was still due when the "refund sent" email had been in the inbox for a day; the search used the wrong words.

**2. Verify every number in code.** Math runs in Python, never in the model's head. Every figure has its source and date. Every total names its window ("last 30 days"). A per-unit cost can never be higher than the price. An estimate is never cash in hand.
*Why:* a model does arithmetic by pattern. Confident wrong numbers are the most expensive kind.

**3. Scope-gate a big build.** Before anything over an hour, write down: the goal, the smallest version that proves it, what you will not build, and how you will know it worked. Agree, then build.
*Why:* big builds without a gate grow sideways and never finish.

**4. Musk's order:** question the requirement, delete, simplify, speed up, automate last.
*Why:* we automated a few broken processes and got broken results, faster.

## The never list (no judgment here)

**5. Credentials, accounts, signatures and first authorizations are the human's alone.** The AI never types or stores a password, key, card, bank or ID number; never creates an account, accepts terms, approves an app's access or signs anything.
*Why:* a key pasted into a chat is a key stored somewhere you do not control, and you are the one legally on the hook.

**6. Money moves only on your word, for that one item.** No trade, order, payment or transfer by the AI. It prepares the ticket; you press the button. A yes to a plan is not a yes to every order inside it.
*Why:* options and inventory are exactly where a misread instruction costs real money in seconds.

**7. Nothing goes to an outside person without your yes.** The AI drafts, you send. A drafted email leaves the To field blank. A message to an outside person carries no internal stamps or tracking text.
*Why:* a sent message has no undo and your name is on it. We once had internal timestamp lines leak into the bottom of real emails.

**8. Nothing is deleted.** Archive, rename or freeze instead. An `_ARCHIVE` folder is the trash, and only you empty it. Copy before any overwrite or bulk change.
*Why:* an agent once archived hundreds of chats in four minutes, live ones included. Deleting is the one mistake you cannot walk back.

**9. No browser bots on ad platforms, Amazon Seller Central or a broker.** Use official APIs only, read-only first. A report the API will not give you is your own download.
*Why:* those platforms detect automation that imitates human clicks and restrict accounts on sight. We had ad accounts restricted this way (both were later reinstated). Your seller account is the business.

## Every write leaves a trail

**10. Every write to the outside world is logged with its undo.** A sheet edited, a file moved, an API write, a draft placed in a real inbox: one row in `records/ACTION-LOG.tsv` after it lands, with the real result, the target and how to undo it. Reads are not logged. The log holds the AI's actions only, never yours.
*Why:* it is how you check from your phone what the machine did, and whether it broke something.

**11. Newest row at the top of every growing list.** The writer inserts under the header; it never appends. Anyone looking for "the latest" goes by the date, never by position.
*Why:* a phone shows the top. A log you must scroll to the bottom of is a log nobody reads.

**12. Commit and push after each logical unit.** Pull first, add your own files by name, never `git add -A`.
*Why:* two chats working in one folder sweep each other's half-done files into the wrong commit. Small pushed commits are your undo button.

## What "done" means

**13. Built is not done.** Done means it is on your surface (the sheet or page you actually read), proven (the AI read it back or ran it), and recapped with `/recap`: the goal, what is done with proof, the honest percent, who it waits on, the next task. Only real files with paths count as progress.
*Why:* for a long time "it's done" meant about 25 percent done.

**14. Every chat ends finished.** Either done with proof, or every leftover filed on the fix list with its number. Never "want me to...?" and never "the next chat will".
*Why:* a promise in a chat that ends is a promise nobody keeps.

**15. A prompt you type twice becomes a skill.**
*Why:* the second time proves it repeats. A skill does it the same way every time and improves in one place.

## Working with the AI

**16. A fresh session per job, and a handoff before the context gets long.** Past about a third of the context window, run `/handoff` and start a fresh chat that reads it.
*Why:* somewhere past 30 to 40 percent context the AI gets quietly worse. A clean start with a good handoff beats a long tired chat.

**17. A correction is a scalpel.** Fix exactly the detail you named and leave the rest standing.
*Why:* a full rewrite after a one-line correction once cost an afternoon and broke the parts that were right.

**18. Fix a mistake where it lives, and log the miss.** Change the rule file, skill or tool that failed, not only today's output. Then add one row to `records/MISS-LOG.tsv` naming where it was fixed. Log misses the process catches too, not only the ones you catch.
*Why:* a correction made only in chat is forgotten by the next chat. Nothing should be corrected twice. A log of only what you noticed measures you, not the work.

**19. Mobile first.** Every surface works on a phone: the first three columns carry the meaning, short words, links, newest on top. A button you must press is named with its colour: green APPROVE, red DENY.
*Why:* you will check this system from your phone far more than from a desk.

## Smaller ones worth keeping

- **Name the sheet and the tab, with its link,** whenever a result is reported. A result only in chat is not delivered.
- **Look at what you built** (open the page or the sheet) before handing it over.
- **Obvious fixes under 15 minutes are done now,** not filed. A reminder ("plug in the laptop") is said once and filed nowhere.
- **Scheduled jobs run read-only or draft-only** until you approve more (see 06).
- **No more than four helper agents at once** without your okay. They burn usage fast.
- **No em dashes.** A house style: hyphens, or restructure the sentence. It keeps the writing plain.
