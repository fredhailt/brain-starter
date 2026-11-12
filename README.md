# Brain starter

A working folder you run with Claude Code. It holds three things:

1. **The brain:** the best parts of an AI operating system we have been building and running every day for months. How the rules work, how the AI keeps its own to-do list, how every record is kept so any AI can pick it up, and how Duet hands work out from your phone.
2. **Options trading:** how options work from zero, the wheel, the jade lizard, the tastytrade rules, a playbook for a small account, and how to paper trade with Claude before a dollar is at risk.
3. **Amazon wholesale:** the whole process from setup to the first order to restocking, plus other businesses an AI is genuinely good at helping run.

It is not a course. Open it in Claude Code and use it. Everything in here can be changed by asking.

## Get it onto your Mac (10 minutes)

**1. Clone it.** Open the Claude Code desktop app on your projects folder (Code tab, Select folder). Type:

```
clone github.com/fredhailt/brain-starter into this folder, then tell me what's in it
```

**2. Open the new folder.** Select folder again and pick the new `brain-starter` folder. This matters: the rule book (`AGENTS.md`) only applies when the app is opened on this folder.

**3. Make it yours.** Your trades, product checks and notes should save to your own private repo, not to this public one. Type:

```
make this folder a private repo on my personal GitHub account, push it there, and keep the repo I cloned from as "upstream"
```

(If Claude asks you to sign in to GitHub, that sign-in is yours to do. It will tell you exactly what to click.)

**4. Start.** Type:

```
read the README and AGENTS.md, then ask me which lane I want first: options or Amazon
```

Later, when this starter gets updates, type `pull the latest changes from upstream and tell me what changed`.

## The first hour

| Step | What you do | Done when |
|---|---|---|
| 1 | Read `system/01-ai-agnostic.md` and `system/02-the-laws.md`. | You know why everything lives in files, GitHub and Sheets. |
| 2 | Read `options/01-how-options-work.md`. | You can explain a put to someone. |
| 3 | Ask Claude: `help me pick a paper trading account and open it` (free; it shows the numbers a trade check needs). Then: `run /trade-check on a cash-secured put on a stock I would happily own` | Your first paper ticket is in `options/trade-log.csv`. A SKIP is a fine first result: it means the rules worked. |
| 4 | Ask Claude: `run /product-check on one product I see in my house` | Your first row is in `amazon/tracker/products.csv`. |
| 5 | Ask Claude: `/recap` | You see what got done and what's next. |

## Options or Amazon first?

Honest take from running both:

- **Options is easier to start.** It is all digital. No inventory, no warehouse, no brands to win over, no shipping. You can learn it with fake money for months at zero cost. **It is also riskier:** a bad habit can lose real money fast, which is why the paper gate exists.
- **Amazon wholesale is slower and steadier.** It takes phone calls, applications and a first order before you see a dollar, and the money is tied up in boxes. But a good brand reorders for years. Your phone skills are the edge here.

A sensible order: paper trade options from week one (an hour a week), and work the Amazon calls in parallel. Real money goes into options only after the paper gate in `options/07-paper-trading-with-claude.md`, and into Amazon only after `/first-order` says PASS.

## What's in here

| Folder or file | What it is |
|---|---|
| `AGENTS.md` | The rule book every AI reads first. `CLAUDE.md` just points to it. |
| `system/` | The brain: AI-agnostic records, the laws, captains and processes, Duet as dispatcher, the records, daily habits. |
| `options/` | Options from zero to an AI-assisted paper trading routine. |
| `amazon/` | Amazon wholesale, beginning to end, and the trackers. |
| `ideas/` | Other businesses an AI is good at helping run, ranked for a $5K to $10K start. |
| `records/` | Your fix list, to-do, action log, miss log, handoffs, decisions. |
| `templates/` | Blank captain, process and decision files. |
| `tools/` | `log.py` (adds rows to your records), `sheets_mirror.py` (copies a record to Google Sheets) and `bus.py` (the job bus Duet uses to hand work to Claude Code). |
| `.claude/skills/` | Slash commands: `/trade-check`, `/product-check`, `/brand-call`, `/first-order`, `/recap`, `/handoff`, `/new-captain`. |
| `.claude/agents/` | Helper agents: builder, verifier, scout. |
| `.claude/hooks/` | A clock that tells Claude the real time on every message, so every dated record is right. |

## Duet

If you have Duet: read `system/04-duet-the-dispatcher.md`. Short version: talk to Duet from your phone, let it keep your to-do list and hand jobs to Claude Code on your Mac through one shared Google Sheet, and give it the same rules as `AGENTS.md`. We have only used it for about a week, so treat that file as what's working so far, not the final word.

## Three things to know

- **Nothing in here sends, pays, trades, deletes or posts on its own.** The AI drafts, you decide. Keep it that way until a process has proven itself many times.
- **Nothing here is financial, tax or legal advice.** It is what we learned and how we run things. Check the official pages, and talk to a tax pro before your first real trade or first sale.
- **This was built by Claude Code** working for someone who does not write code. You can change any rule by asking: `change rule 3 in AGENTS.md to say ...`.
