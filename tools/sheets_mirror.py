#!/usr/bin/env python3
"""sheets_mirror.py - copies one records file (TSV) up to one Google Sheet tab, or one tab down to a file.

The file on your computer is the record; the sheet is the view you read on your phone. A push rewrites the whole
tab from the file, so anything typed on that tab by hand is replaced: tell the AI instead, and it writes the file.
A record that starts life in a sheet (like the bus, which Duet writes) is saved down with pull.

ONE-TIME SETUP (steps marked YOU are yours alone: they create or handle a credential)
 1. YOU: open console.cloud.google.com and create a project (any name).
 2. YOU: APIs & Services > Library > Google Sheets API > Enable.
 3. YOU: IAM & Admin > Service Accounts > Create service account (any name, no roles needed). Open it > Keys >
    Add key > Create new key > JSON. A key file downloads. Treat it like a password: never paste it into a chat.
 4. YOU: move the key file into the credentials/ folder of this repo (git ignores that folder), or anywhere
    outside the repo.
 5. YOU: make the Google Sheet yourself in Google Drive. A service account has no Drive storage of its own, so it
    cannot create files; you make the sheet, it fills it. Click Share and add the service account's email as
    Editor (it ends in iam.gserviceaccount.com; the key file shows it as client_email).
 6. Install the package once: python3 -m pip install --user gspread
 7. Point the tool at the key (in your shell profile, or a gitignored .env):
        export SHEETS_SA_KEY="/full/path/to/the-key.json"
 8. Try it without writing anything:
        python3 tools/sheets_mirror.py push records/FIX-LIST.tsv --sheet <sheet id> --tab "FIX LIST" --dry
    The sheet id is the long string between /d/ and /edit in the sheet's address. Then run it again without --dry.

COMMANDS
  sheets_mirror.py push <file.tsv> --sheet ID --tab "TAB" [--dry]   rewrite the tab from the file (header frozen)
  sheets_mirror.py pull <file.tsv> --sheet ID --tab "TAB" [--dry]   save the tab down to the file; the old file is
                                                                    kept as <file>.bak first, so nothing is lost
RULES IT KEEPS
  - A push that would add a sixth tab to a sheet is refused: five working tabs plus one how-to tab per sheet;
    a new subject gets a new sheet.
  - Every real push is a write to the outside world, so it writes its own row in records/ACTION-LOG.tsv
    (with how to undo it) after the write lands.
"""
import argparse
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import log  # noqa: E402

MAX_TABS = 6  # five working tabs plus one how-to tab


def need_gspread():
    try:
        import gspread
    except ImportError:
        raise SystemExit("gspread is not installed. Install it once with: python3 -m pip install --user gspread")
    return gspread


def need_key():
    key = os.environ.get("SHEETS_SA_KEY", "")
    if not key:
        raise SystemExit("SHEETS_SA_KEY is not set. Point it at your service account key file "
                         "(setup steps are at the top of this file).")
    if not os.path.exists(key):
        raise SystemExit(f"SHEETS_SA_KEY points at a file that does not exist: {key}")
    return key


def read_tsv(path):
    with open(path, encoding="utf-8") as f:
        rows = [ln.rstrip("\n").rstrip("\r").split("\t") for ln in f if ln.strip()]
    width = max((len(r) for r in rows), default=1)
    return [r + [""] * (width - len(r)) for r in rows]


def open_book(sheet_id):
    gspread = need_gspread()
    key = need_key()
    return gspread.service_account(filename=key).open_by_key(sheet_id)


def push(path, sheet_id, tab, dry):
    rows = read_tsv(path)
    width = len(rows[0]) if rows else 1
    need_gspread()
    need_key()
    if dry:
        print(f"DRY RUN: would rewrite tab '{tab}' of sheet {sheet_id} with {len(rows)} rows x {width} columns.")
        for r in rows[:3]:
            print("  " + " | ".join(c[:30] for c in r))
        return
    book = open_book(sheet_id)
    titles = [ws.title for ws in book.worksheets()]
    if tab in titles:
        ws = book.worksheet(tab)
    elif len(titles) >= MAX_TABS:
        raise SystemExit(f"REFUSED: sheet already has {len(titles)} tabs ({', '.join(titles)}). Five working tabs "
                         "plus one how-to tab is the limit; put this record on a new sheet.")
    else:
        ws = book.add_worksheet(title=tab, rows=max(len(rows), 1), cols=max(width, 1))
    ws.clear()
    ws.resize(rows=max(len(rows), 1), cols=max(width, 1))
    ws.update(range_name="A1", values=rows)
    ws.freeze(rows=1)
    print(f"pushed {len(rows)} rows to tab '{tab}'")
    log.action_add(what=f"Mirrored {os.path.basename(path)} ({len(rows) - 1} rows) to tab {tab}",
                   target=f"Google Sheet {sheet_id} > {tab}", result="OK", kind="sheet write",
                   undo="Push the earlier version of the file from git history",
                   link=f"https://docs.google.com/spreadsheets/d/{sheet_id}/edit")


def pull(path, sheet_id, tab, dry):
    book = open_book(sheet_id)
    rows = book.worksheet(tab).get_all_values()
    if dry:
        print(f"DRY RUN: would save {len(rows)} rows from tab '{tab}' to {path}")
        return
    if os.path.exists(path):
        shutil.copy2(path, path + ".bak")
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write("\t".join(log.clean(c) for c in r) + "\n")
    print(f"saved {len(rows)} rows from tab '{tab}' to {path}" + (" (old copy: .bak)" if os.path.exists(path + ".bak") else ""))


def main(argv=None):
    p = argparse.ArgumentParser(prog="sheets_mirror.py", description="Mirror one TSV file and one Google Sheet tab.")
    p.add_argument("direction", choices=["push", "pull"])
    p.add_argument("file")
    p.add_argument("--sheet", required=True, help="the sheet id (between /d/ and /edit in its address)")
    p.add_argument("--tab", required=True)
    p.add_argument("--dry", action="store_true")
    x = p.parse_args(argv)
    if x.direction == "push":
        if not os.path.exists(x.file):
            raise SystemExit(f"No such file: {x.file}")
        push(x.file, x.sheet, x.tab, x.dry)
    else:
        pull(x.file, x.sheet, x.tab, x.dry)


if __name__ == "__main__":
    main()
