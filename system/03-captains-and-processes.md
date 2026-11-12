# 03 - Captains and processes

**Captains are people. Processes are the work.**

- A **process** is the work, step by step. It is not finished until its named FINISHED RESULT exists.
- A **captain** is a seat that knows things and runs processes, like a virtual assistant with a rule book. A captain is never the work itself.

*Why:* we first built captains as big personalities with long rule books. They produced flags on sheets ("44 items need attention") instead of finished work. Naming the finished result of every process is what fixed it.

## A process

Each step says who does it: the **machine** (a plain script), the **AI** (a Claude run) or a **human** (you, or a helper).

It ends in a **finished result** you can point at. Examples:
- **Amazon restock:** a purchase order drafted, priced and checked, with its email drafted (To field blank) in a "ready for review" folder.
- **Options:** a trade ticket ready for you: symbol, strike, expiry, size, the most it can lose, the exit plan and why. The AI never places it.
- **Brand research:** a lead with its contact found and one line on why it fits.

It lists its **end states**, the ways it can finish. A brand call, for example, ends in exactly one of: PRICE LIST, APPLICATION, YES, MAYBE, NO, NO ANSWER.

**A run that stops at a flag waiting for you is not finished.** It drafts the thing you say yes to. "12 products look good" is a flag; "12 products, here is the order, approve or cut lines" is a result.

**Processes chain.** One process's result is the next one's input. A STATUS column that says READY is the hand-off: the sheet is the queue, and a clock only decides when to look. A run that finds nothing to do costs nothing.

Template: `templates/PROCESS-TEMPLATE.md`.

## Build the process first, then name the captain

1. Run the process by hand with Claude, one chat per run, three times.
2. Write it down in the template, with its finished result and end states.
3. Turn the boring steps into scripts (no model needed for a step that is always the same).
4. Only now give it a seat: a captain whose knowledge runs it.

*Why:* this is Musk's order (law 4). A seat with no proven process is a job title with no job.

## A captain

A captain lives in `captains/<name>/` with its own `AGENTS.md`. Build one with `/new-captain`; the template is `templates/captain-AGENTS.md`. It holds:

- **The lane:** one sentence of what it owns.
- **The voice:** how it talks. For example, "a buyer who has done this for twenty years: the number first, one recommendation, blunt".
- **NOT MINE:** a table of what belongs to another seat and the one line it says when asked.
- **Its processes,** each linked, each with its finished result.
- **RULINGS:** a dated table, newest first: date, what you said in your own words, what the captain does about it. Every ruling you give is written the same turn, before the reply.
- **HANDOFF.md** in its folder: where the last session stopped.

*Why the RULINGS table:* rulings given in a chat and never written down were our biggest source of "I already told you this". A row in the rule book outranks any memory.

A ruling is never changed or removed without your written okay. When something new you say seems to clash with an old ruling, the captain asks; it never assumes you changed your mind.

## Bev, the shadow grader

Before a captain makes a decision you will see (buy now or wait? is this brand a fit? take this trade or pass?), a second, cheaper model records its own call first. When the real answer is known (what you actually ordered, whether you took the trade), both are settled: match or no match. Bev changes nothing. It is a measurement.

**The ladder,** per kind of decision:
- **SHADOW:** the AI drafts, you finish.
- **ASSISTED** at 10 or more graded runs and 90 percent passed: the AI does it, you check before it leaves.
- **TRUSTED** at 30 or more graded runs and 99 percent passed: the AI does it alone, inside its rules.

Every run you finish together also ends with your PASS or FAIL in one sentence. A FAIL becomes a rule in that captain's book the same turn.

*Why:* "it seems good" is not a number. This is how a decision earns the right to move to a cheaper model, or to no human at all. Start simple: a small TSV with lane, item, Bev's call, the final answer and match. A free model on your own machine or a cheap hosted one both work.

## Foreman and Wrench

Two seats every setup ends up needing:
- **Foreman** ranks the work. For every row waiting on you it asks first: can an agent do this instead? At day's end it sweeps the day's chats for unfinished work and files it.
- **Wrench** fixes broken things. A failed scheduled run is work the same day; failing twice in a row is a fire.

Both start as a short once-a-day prompt, then a skill, then a captain if they earn it.

## Start with ONE captain

1. Pick the lane that eats the most of your week. For Amazon that is usually product research or restock; for options, the weekly trade review.
2. Write the process and run it by hand three times.
3. Run `/new-captain`, give it the name and the lane.
4. Add rulings as you go. Add a Bev lane once the captain repeats a decision.
5. Only then give it a clock (06) and a place on the bus (04).

*Why:* we stood up many captains in a short time and most sat idle. A captain with no shift is "available", not working.
