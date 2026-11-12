# Options

A short course in selling options, written for someone with a full-time job, a USD 5,000 to 10,000 starting pot, and Claude Code on their laptop.

> **Education, not financial advice.** Nothing in this folder tells you what to buy or sell. It explains how the pieces work, what the well-known teachers say, and where they disagree. Your money, your decisions, your rules. Talk to a licensed professional for advice about your own situation.

## Read in this order

| # | File | What you get | Time |
|---|---|---|---|
| 1 | [01-how-options-work.md](01-how-options-work.md) | Every word you need: calls, puts, strike, premium, the greeks, IV rank, assignment | 20 min |
| 2 | [02-the-wheel.md](02-the-wheel.md) | The beginner's income strategy, step by step, with a worked example | 15 min |
| 3 | [04-the-tastytrade-way.md](04-the-tastytrade-way.md) | The rules most premium sellers follow, and who made them | 15 min |
| 4 | [06-small-account-playbook.md](06-small-account-playbook.md) | What changes when the account is small, the rule card, and a plan for the first months | 15 min |
| 5 | [07-paper-trading-with-claude.md](07-paper-trading-with-claude.md) | How to practice with fake money and Claude as your research partner | 10 min |
| 6 | [05-strategy-cheatsheet.md](05-strategy-cheatsheet.md) | One table of eleven strategies. Keep it open while you learn | 5 min |
| 7 | [03-jade-lizard.md](03-jade-lizard.md) | A more advanced trade. Read it after you have 20 paper trades | 10 min |
| 8 | [08-ai-run-options-research.md](08-ai-run-options-research.md) | How to grow this into a crew of AI "seats" later | 10 min |

Two working files:
- [trade-log.csv](trade-log.csv) is your trade journal. One row per trade, newest at the top.
- The `/trade-check` skill in `.claude/skills/trade-check/` walks a proposed **paper** trade through the rules in these files and writes the row for you. Say "trade check" or "should I sell this put" in Claude Code.

## The honest stance

**Options are easier to start than an Amazon business.** Everything is digital. There is no inventory to buy, no warehouse, no supplier to win over, no listing to fight for. You can open a paper account tonight and place a practice trade in ten minutes.

**Options are also riskier.** An Amazon mistake usually costs you one shipment. An options mistake can cost a large share of the account in a single day, because:
- one contract controls 100 shares, so small price moves become big dollar moves;
- selling options wins often and loses big, and the big loss tends to come all at once;
- the tools make it very easy to take more risk than you understand.

So the order is fixed:
1. **Learn the words** (file 01).
2. **Write your rules down** (files 02, 04, 06 give you a starter set).
3. **Paper trade first** (file 07). No real money until you pass the gate written there.
4. **Start real money small,** with defined-risk trades, and keep logging.

## Where the ideas come from

Most of the mechanics here come from tastylive, the media arm of the broker tastytrade, founded by Tom Sosnoff. They have published years of free segments on selling premium, and each rule in these files names the segment it came from. Keep one thing in mind: **tastylive is part of a broker, and a broker earns more when you trade more.** Their mechanics are useful; their "trade often" advice deserves a second look. File 04 covers this.

Where a number appears in an example, it is labeled **illustration**. Real prices change every second. Never trade off an example.

## A word on Claude

Claude Code is a great research partner: it explains, calculates, checks your rules, and keeps your log. It never places an order. You do. File 07 explains why that line matters and how to keep it.
