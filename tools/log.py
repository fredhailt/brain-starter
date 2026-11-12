#!/usr/bin/env python3
"""log.py - the one writer for the records/ files. Standard library only; any python3 runs it.

Every growing list keeps its newest row at the top (row 2, right under the header), so the
first thing you see on a phone is the latest. Dates come from this machine's clock, never
from a model's memory.

RECORDS (tab-separated, in records/ next to this tools/ folder; set BRAIN_RECORDS to use another folder)
  FIX-LIST.tsv     the AI's work list: broken things, promised work not done
  ACTION-LOG.tsv   every write the AI made to the outside world, with how to undo it
  MY-TO-DO.tsv     the human's list: only what truly needs the human
  MY-ACTIONS.tsv   the human's own done things, said in chat, written by the AI
  MISS-LOG.tsv     every correction, so nothing is corrected twice

COMMANDS
  fix add "<what is wrong>" [--area A] [--where W] [--who AI|HUMAN]
  fix done <num> "<evidence>"          closes the row with its proof and a CLOSED ON date
  fix list [--all]                      open rows (or every row) with DAYS OPEN
  action add --what W --target T --result R --undo U [--kind K] [--who AI] [--link L]
  miss add "<what went wrong>" --fix "<where it was fixed>" [--shape S] [--caught C] [--model M]
  todo add "<what to do>" [--how H] [--where W] [--why Y] [--when N] [--answer A] [--fix-num N]
  todo done <num> "<note>"
  todo list [--all]
  did add "<what the human did>" [--result R] [--where W] [--note N]

Examples
  python3 tools/log.py fix add "Restock sheet still shows last week" --area restock
  python3 tools/log.py fix done 3 "Rebuilt; cell A1 now reads today's date"
  python3 tools/log.py action add --what "Rewrote tab FIX LIST" --target "Sheet MY BRAIN > FIX LIST" \
      --result OK --undo "Run the mirror again from the previous TSV in git"
  python3 tools/log.py miss add "Called it done before opening the page" --fix ".claude/skills/recap/SKILL.md step 1"
"""
import argparse
import datetime as dt
import os
import sys
import tempfile

try:
    import fcntl  # macOS and Linux; on Windows the lock is skipped
except ImportError:  # pragma: no cover
    fcntl = None

HERE = os.path.dirname(os.path.abspath(__file__))
RECORDS = os.environ.get("BRAIN_RECORDS") or os.path.join(os.path.dirname(HERE), "records")

HEADERS = {
    "FIX-LIST.tsv": ["#", "STATUS", "WHAT IS WRONG", "AREA", "WHERE TO SEE IT", "WHO DOES IT",
                     "OPENED", "DAYS OPEN", "CLOSED ON", "EVIDENCE"],
    "ACTION-LOG.tsv": ["WHEN", "WHAT", "RESULT", "KIND", "WHO", "TARGET", "LINK", "UNDO"],
    "MY-TO-DO.tsv": ["#", "STATUS", "WHAT TO DO", "WHERE (link)", "HOW", "WHY", "WHEN",
                     "RECOMMENDED ANSWER", "ADDED", "DAYS OPEN", "FIX #"],
    "MY-ACTIONS.tsv": ["WHEN", "WHAT I DID", "RESULT", "WHERE", "NOTE"],
    "MISS-LOG.tsv": ["WHEN", "WHAT WENT WRONG", "SHAPE", "FIXED IN", "CAUGHT BY", "MODEL"],
}
SHAPES = ["no-check", "no-look", "over-scope", "jargon", "wrong"]
NOT_A_FIX = {"", "not yet", "todo", "later", "tbd", "none", "n/a"}
HUMAN_WORDS = {"me", "human", "owner", "i", "you", "myself"}


def now():
    return dt.datetime.now()


def stamp():
    return now().strftime("%Y-%m-%d %H:%M")


def today():
    return now().strftime("%Y-%m-%d")


def clean(value):
    """One cell: no tabs or line breaks, so the file stays one row per line."""
    return " ".join(str(value or "").replace("\t", " ").splitlines()).strip()


def path_of(name):
    return os.path.join(RECORDS, name)


class Locked:
    """Holds a lock on <folder>/.lock (records/ by default) so two chats writing at once never drop a row."""

    def __init__(self, folder=None):
        self.folder = folder or RECORDS

    def __enter__(self):
        os.makedirs(self.folder, exist_ok=True)
        self.f = open(os.path.join(self.folder, ".lock"), "w")
        if fcntl:
            fcntl.flock(self.f, fcntl.LOCK_EX)
        return self

    def __exit__(self, *exc):
        if fcntl:
            fcntl.flock(self.f, fcntl.LOCK_UN)
        self.f.close()


def read(name):
    p = path_of(name)
    if not os.path.exists(p):
        return [HEADERS[name]]
    with open(p, encoding="utf-8") as f:
        lines = [ln.rstrip("\n").rstrip("\r") for ln in f]
    rows = [ln.split("\t") for ln in lines if ln.strip()]
    if not rows:
        return [HEADERS[name]]
    width = len(rows[0])
    return [r + [""] * (width - len(r)) for r in rows]


def write(name, rows):
    """Write the whole file to a temp file, then swap it in, so a crash never leaves half a file."""
    p = path_of(name)
    fd, tmp = tempfile.mkstemp(dir=RECORDS, prefix=".tmp-")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        for r in rows:
            f.write("\t".join(clean(c) for c in r) + "\n")
    os.replace(tmp, p)


def insert_top(name, values):
    rows = read(name)
    rows.insert(1, values)
    write(name, rows)


def next_num(rows):
    nums = [int(r[0]) for r in rows[1:] if r and r[0].isdigit()]
    return max(nums, default=0) + 1


def days_between(start, end):
    try:
        a = dt.date.fromisoformat(start[:10])
        b = dt.date.fromisoformat(end[:10])
        return str((b - a).days)
    except ValueError:
        return ""


def refresh_days(rows, opened_col, days_col, closed_col=None):
    """DAYS OPEN is counted again on every write: to today while open, frozen at the close date once closed."""
    for r in rows[1:]:
        end = r[closed_col] if closed_col is not None and r[closed_col] else today()
        r[days_col] = days_between(r[opened_col], end)


def find_row(rows, num):
    for i, r in enumerate(rows[1:], start=1):
        if r[0] == str(num):
            return i
    return None


# ---------- FIX LIST ----------
def fix_add(what, area="", where="", who="AI"):
    with Locked():
        rows = read("FIX-LIST.tsv")
        num = next_num(rows)
        status = "WAITING ON YOU" if who.strip().lower() in HUMAN_WORDS else "OPEN"
        rows.insert(1, [str(num), status, what, area, where, who.upper(), today(), "0", "", ""])
        refresh_days(rows, 6, 7, 8)
        write("FIX-LIST.tsv", rows)
    return num


def fix_done(num, evidence):
    if not clean(evidence):
        raise SystemExit("REFUSED: a fix closes only with its evidence (what proves it is fixed).")
    with Locked():
        rows = read("FIX-LIST.tsv")
        i = find_row(rows, num)
        if i is None:
            raise SystemExit(f"No fix row #{num}.")
        rows[i][1] = "CLOSED"
        rows[i][8] = today()
        rows[i][9] = evidence
        refresh_days(rows, 6, 7, 8)
        write("FIX-LIST.tsv", rows)


def show(rows, keep):
    out = [rows[0]] + [r for r in rows[1:] if keep(r)]
    widths = [min(max(len(r[c]) for r in out), 48) for c in range(len(rows[0]))]
    for r in out:
        print("  ".join(r[c][:48].ljust(widths[c]) for c in range(len(r))).rstrip())
    print(f"({len(out) - 1} rows)")


def fix_list(show_all=False):
    with Locked():
        rows = read("FIX-LIST.tsv")
        refresh_days(rows, 6, 7, 8)
        write("FIX-LIST.tsv", rows)
    show(rows, lambda r: show_all or r[1] != "CLOSED")


# ---------- ACTION LOG ----------
def action_add(what, target, result, undo, kind="", who="AI", link=""):
    if clean(who).lower() in HUMAN_WORDS:
        raise SystemExit("REFUSED: the action log holds the AI's actions only. "
                         "Your own go in MY-ACTIONS: python3 tools/log.py did add \"...\"")
    for label, value in (("--what", what), ("--target", target), ("--result", result), ("--undo", undo)):
        if not clean(value):
            raise SystemExit(f"REFUSED: {label} is required (an outside write is logged with its result and its undo).")
    with Locked():
        insert_top("ACTION-LOG.tsv", [stamp(), what, result, kind, who, target, link, undo])


# ---------- MISS LOG ----------
def miss_add(what, fix, shape="", caught="human", model=""):
    if clean(fix).lower() in NOT_A_FIX:
        raise SystemExit("REFUSED: name where the mistake was fixed (the rules file, skill or tool you changed). "
                         "Fix it where it lives first, then log it.")
    if shape and shape not in SHAPES:
        raise SystemExit(f"--shape must be one of: {', '.join(SHAPES)}")
    with Locked():
        insert_top("MISS-LOG.tsv", [stamp(), what, shape, fix, caught, model or os.environ.get("CLAUDE_MODEL", "")])


# ---------- MY TO-DO ----------
def todo_add(what, how="", where="", why="", when="", answer="", fix_num=""):
    with Locked():
        rows = read("MY-TO-DO.tsv")
        num = next_num(rows)
        rows.insert(1, [str(num), "OPEN", what, where, how, why, when, answer, today(), "0", str(fix_num or "")])
        for r in rows[1:]:
            if r[1] == "OPEN":  # a done row keeps the count it had when it closed
                r[9] = days_between(r[8], today())
        write("MY-TO-DO.tsv", rows)
    return num


def todo_done(num, note):
    with Locked():
        rows = read("MY-TO-DO.tsv")
        i = find_row(rows, num)
        if i is None:
            raise SystemExit(f"No to-do row #{num}.")
        rows[i][9] = days_between(rows[i][8], today())
        rows[i][1] = "DONE " + today() + (": " + note if clean(note) else "")
        write("MY-TO-DO.tsv", rows)


def todo_list(show_all=False):
    with Locked():
        rows = read("MY-TO-DO.tsv")
        for r in rows[1:]:
            if r[1] == "OPEN":
                r[9] = days_between(r[8], today())
        write("MY-TO-DO.tsv", rows)
    show(rows, lambda r: show_all or r[1] == "OPEN")


# ---------- MY ACTIONS ----------
def did_add(what, result="", where="", note=""):
    with Locked():
        insert_top("MY-ACTIONS.tsv", [stamp(), what, result, where, note])


def main(argv=None):
    p = argparse.ArgumentParser(prog="log.py", description="Write the records/ files, newest row on top.")
    sub = p.add_subparsers(dest="record", required=True)

    fx = sub.add_parser("fix").add_subparsers(dest="cmd", required=True)
    a = fx.add_parser("add"); a.add_argument("what"); a.add_argument("--area", default="")
    a.add_argument("--where", default=""); a.add_argument("--who", default="AI")
    d = fx.add_parser("done"); d.add_argument("num"); d.add_argument("evidence")
    l = fx.add_parser("list"); l.add_argument("--all", action="store_true")

    ac = sub.add_parser("action").add_subparsers(dest="cmd", required=True)
    a = ac.add_parser("add")
    for flag in ("--what", "--target", "--result", "--undo"):
        a.add_argument(flag, required=True)
    a.add_argument("--kind", default=""); a.add_argument("--who", default="AI"); a.add_argument("--link", default="")

    ms = sub.add_parser("miss").add_subparsers(dest="cmd", required=True)
    a = ms.add_parser("add"); a.add_argument("what"); a.add_argument("--fix", required=True)
    a.add_argument("--shape", default=""); a.add_argument("--caught", default="human"); a.add_argument("--model", default="")

    td = sub.add_parser("todo").add_subparsers(dest="cmd", required=True)
    a = td.add_parser("add"); a.add_argument("what")
    for flag in ("--how", "--where", "--why", "--when", "--answer", "--fix-num"):
        a.add_argument(flag, default="")
    d = td.add_parser("done"); d.add_argument("num"); d.add_argument("note", nargs="?", default="")
    l = td.add_parser("list"); l.add_argument("--all", action="store_true")

    dd = sub.add_parser("did").add_subparsers(dest="cmd", required=True)
    a = dd.add_parser("add"); a.add_argument("what"); a.add_argument("--result", default="")
    a.add_argument("--where", default=""); a.add_argument("--note", default="")

    x = p.parse_args(argv)
    if x.record == "fix":
        if x.cmd == "add":
            n = fix_add(x.what, x.area, x.where, x.who)
            print(f"fix #{n} added ({path_of('FIX-LIST.tsv')})")
        elif x.cmd == "done":
            fix_done(x.num, x.evidence)
            print(f"fix #{x.num} CLOSED")
        else:
            fix_list(x.all)
    elif x.record == "action":
        action_add(x.what, x.target, x.result, x.undo, x.kind, x.who, x.link)
        print("action logged")
    elif x.record == "miss":
        miss_add(x.what, x.fix, x.shape, x.caught, x.model)
        print("miss logged")
    elif x.record == "todo":
        if x.cmd == "add":
            n = todo_add(x.what, x.how, x.where, x.why, x.when, x.answer, x.fix_num)
            print(f"to-do #{n} added")
        elif x.cmd == "done":
            todo_done(x.num, x.note)
            print(f"to-do #{x.num} DONE")
        else:
            todo_list(x.all)
    elif x.record == "did":
        did_add(x.what, x.result, x.where, x.note)
        print("your action recorded")


if __name__ == "__main__":
    main()
