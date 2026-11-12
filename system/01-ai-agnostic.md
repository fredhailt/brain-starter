# 01 - AI agnostic: the big three

The one idea: your system must outlive any one chat, any one AI and any one computer.

## The big three

Every record that matters lives in three places:

1. **Plain files on your own computer.** Markdown (`.md`) for writing, tab-separated (`.tsv`) for lists. Any AI and any person can read them with no special app.
2. **Backed up to GitHub,** in a private repo. Every change has a history, any mistake can be undone, and a new computer is one clone away.
3. **Mirrored to Google Sheets.** The view you read on your phone, sort, filter and share with a helper.

Some records start in a sheet and are saved down to a file (a list someone else types on, like the bus Duet writes to in 04). Either way, each record has ONE source and the other copy is a mirror. Two places that both get typed on will disagree within a week.

**Why, the way we learned it:**
- **Any AI can read it.** Claude Code today, ChatGPT or Codex tomorrow, an open model on your own machine next year. We have switched tools and models many times; plain files never cared.
- **It moves.** A new laptop, a cloud machine, a helper's computer: clone and go.
- **Nothing lives only in a chat.** A chat ends, gets compacted or archived, and its memory is not yours. A result that exists only in a chat message was never delivered.

## One rules file: AGENTS.md

- `AGENTS.md` is the file name Codex and most coding tools look for. Claude Code looks for `CLAUDE.md`. So `CLAUDE.md` is a one-line door that says `@AGENTS.md` (the `@` pulls the other file in).
- **Why:** we ran for months with our rules only in `CLAUDE.md`, and every other tool opened the repo with no rules at all. One file means no second copy to drift.
- Keep it short: each rule plus its one-line why. Long stories go in `records/decisions/`.
- Each captain gets its own `AGENTS.md` in its own folder (see 03). It adds rules; it never loosens the top file.

## A searchable knowledge base

- Everything you read and decide becomes a file: notes, video transcripts you learned from, decision records, handoffs.
- Make it searchable two ways. **Exact words:** Claude Code already searches files well; just ask it. **Meaning:** once you have a few hundred notes, add an open-source local search index that reads a plain folder of markdown and finds notes by meaning, not just by spelling. Several free ones exist; pick one that runs on your own machine.
- **Why:** "search the brain first" stopped more duplicate builds than any other habit. The answer to "do we have something for this?" is usually yes.

## Sheets are what a human reads; a page only shows a sheet

- When a record needs your eyes (your to-do, the fix list, a product tracker, a trade log), it lands on a Google Sheet.
- A web page or dashboard may read that sheet and show it nicely. It never holds the only copy.
- **Why:** pages break, get rebuilt and go stale quietly. A sheet keeps its history, opens on any phone, and the AI can read and write it.

Sheet rules that paid off:
- **The first three columns carry the meaning.** That is all a phone shows without scrolling.
- **Newest row at the top,** right under the header.
- **Every list has OPENED and DAYS OPEN,** so nothing old hides.
- **At most five working tabs plus one how-to tab** (START HERE). A new subject gets a new sheet. More tabs than that and nobody finds anything.
- **One sheet per subject.** A sheet 90 percent like another one is a duplicate: upgrade the old one.

## Set up the Sheets mirror (about 20 minutes, once)

A **service account** is a robot Google account your scripts use. It has its own email address. You share a sheet with it as Editor, exactly as you would with a person.

The steps marked YOU are yours alone, because they create or handle a credential (see law 5 in `02-the-laws.md`). The AI can talk you through each click; it never touches the key.

1. **YOU:** at console.cloud.google.com, create a project (any name).
2. **YOU:** APIs & Services > Library > Google Sheets API > Enable.
3. **YOU:** IAM & Admin > Service Accounts > Create. No roles needed. Open it > Keys > Add key > JSON. A key file downloads. It is a password: never paste it into a chat.
4. **YOU:** make a `credentials/` folder in this repo (ask Claude: `make the credentials folder`) and move the key file into it. Git ignores that folder, so it never reaches GitHub.
5. **YOU:** create the Google Sheet yourself. A service account has no Drive storage of its own, so it cannot create files; you make the sheet, the robot fills it. Share it with the robot's email (ends in `iam.gserviceaccount.com`) as Editor.
6. Install the package once: `python3 -m pip install --user gspread`
7. **YOU:** tell the tool where the key is, in your shell profile or a gitignored `.env` file: `export SHEETS_SA_KEY="/full/path/to/key.json"`
8. Try it without writing anything: `python3 tools/sheets_mirror.py push records/FIX-LIST.tsv --sheet <id> --tab "FIX LIST" --dry`. The sheet id is the long string between `/d/` and `/edit` in the sheet's address. Then run it again without `--dry`.

After that, just say "mirror the fix list and my to-do to the sheet". The tool writes its own action log row each time. Later, a scheduled job can do it (see 06).

## What never goes in any of the three

- **Passwords, keys, card or bank numbers.** Keys live in `credentials/` or `.env`, both ignored by git.
- **Raw bank or card statements.** Reading a file sends it to the AI provider, and gitignore protects nothing once it has been read. Redact on your own computer first; only the clean copy is ever read.
- **Real records in a public repo.** This starter is public. Your copy must be private before the first real trade, product or note goes in (the main README shows how).
