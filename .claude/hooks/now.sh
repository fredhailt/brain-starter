#!/bin/bash
# now.sh - tells the AI the real local date and time on every message you send.
#
# Why: the model knows today's date but never the time, so any time it writes
# without this is a guess. Every dated record (an action log row, a fix row, a
# handoff, a decision record) takes its time from this clock, never from memory.
#
# Wired in .claude/settings.json under UserPromptSubmit. Whatever this prints is
# added to the AI's context for that turn. No extra programs needed (no jq).
#
# Test it:  bash .claude/hooks/now.sh

set -eu

DAY=$(date "+%A")
PLAIN=$(date "+%Y-%m-%d %-I:%M %p %Z")    # 2026-03-14 6:19 PM EST   (a line a human reads)
SORT=$(date "+%Y-%m-%d %H:%M")             # 2026-03-14 18:19         (records, file names)

cat <<EOF
REAL CLOCK (read from this computer, not a guess): ${DAY} ${PLAIN}
Use these stamps exactly, never a remembered time:
  records and file names: ${SORT}
  a line a human reads:   ${PLAIN}
A message to an outside person never carries this stamp or any tracking text; the
time it was sent goes in records/ACTION-LOG.tsv instead.
EOF
