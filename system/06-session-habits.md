# 06 - Session habits

How to drive Claude Code day to day. None of this is clever. All of it is what separated the days that moved from the days that churned.

## One job per chat

Start a fresh chat for each job. When the job is done, `/recap` and close it. When it is not done and the chat is getting long, `/handoff` and start fresh.

*Why:* a chat carrying three jobs does all three a little worse, and a long chat gets quietly dumber. Watch the context meter: around a third full is the time to hand off.

## Plan first, then build

Anything with more than two steps: ask for numbered steps with a check at the end of each, read them, then build one step at a time. Claude Code's plan mode does exactly this.

*Why:* a wrong plan costs a minute to fix. A wrong build costs an hour, then another hour to undo.

## The three helpers (`.claude/agents/`)

| Helper | Use it for | Model |
|---|---|---|
| scout | Fast, cheap lookups: where is X, does Y exist. Before planning. | small |
| builder | Exactly one scoped task from the plan. Shows proof when done. | strong |
| verifier | A cold check of finished work against the plan. Never fixes anything. | strong |

Just ask: "use the scout to find...", "have a builder do step 3", "have the verifier check it".

**The checker is never the builder.** The model that did the work always thinks it worked. A verifier with fresh context, given the ask and where the result is (never the builder's conclusion), is what catches the rest.

**A planner plans, a worker builds, a fresh model checks.** That one line is most of our quality.

Independent steps can run as parallel builders, but no more than four at once without thinking about the cost. Two builders must never touch the same file.

## Pick the model and effort per job

- **New or high-stakes work** (designing a process, money, anything going to an outside person): the strongest model, high effort.
- **A proven process** (it has passed its graded runs, see Bev in 03): step down to a cheaper model or lower effort, and check the grades still hold.
- **The steps that are always the same:** a plain script, no model at all.

Say the model and effort in one line at the start of any sizeable task, so the choice is visible and yours.

## Remote Control and the phone

- Turn on **Remote Control** for a chat and you can follow and answer it from the Claude phone app. The app can also let your phone start new sessions on your computer. (Setting names move between app versions; ask Claude to find the current one.)
- An app update or a restart can turn Remote Control off on open chats. If a chat is missing from your phone, that is usually why.
- On the phone, talk instead of typing. Claude writes the sheets; you never need to type into one.

## Scheduled routines

A routine is a job that runs on a clock with nobody watching. Rules:
- **Read-only or draft-only** until you approve more. A scheduled run inherits every connector you have connected, write access included, so scope it down hard.
- Each routine has a **landing place** (the sheet and tab it writes), a **reader** (who looks at it), and a **kill condition** (when to turn it off).
- A script-started run uses the locks `bus.py` uses: no connectors (`--strict-mcp-config`), an exact allow list of commands, and edits confined to the folder. Prove a new allow list by trying a command it must refuse.
- A failed run is work the same day. Failing twice in a row is a fire.
- A clock that wakes, finds nothing to do and exits should cost nothing. Start a model only when there is real work.

## The real clock

`.claude/hooks/now.sh` runs on every message (wired in `.claude/settings.json`) and tells the AI the real date and time. Every dated record takes its time from it.

*Why:* the model knows the date but never the time. Before this hook, times in our logs were guesses, and a log with guessed times is worse than no log.

Test it: `bash .claude/hooks/now.sh`. You can also wire it to `SessionStart` so a new chat knows the time before your first message.

## Look at it before you hand it over

Anything with a screen (a page, a sheet, a chart) gets opened and looked at before it is called done: Claude in Chrome, or a screenshot you share. On a phone-sized window too.

*Why:* "the code is there" and "it looks right" are different claims. Most of our embarrassing hand-offs passed every test and looked wrong.

## End every task the same way

`/recap`: the goal in your words, what is done with proof, the honest percent, who it waits on, the one next task. Anything left over is a fix row with a number.
