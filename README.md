# One-Liner Marathon — "Ongoing"

[![Competition](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2)
[![Rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/imusic-487/one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard)
[![Reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/imusic-487/one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard)

## The entry

> My therapist asked me to describe my childhood in one word; I said 'ongoing.'

One line, 77 characters. The setup sounds like a therapy cliché — describe
your childhood in one word — and the punchline is a single word that quietly
admits the childhood never ended. It lands on the first read, and on the
second read the implication deepens: the patient is still living it.

## What this repo does

This is an entry for the make.fun competition
[One-Liner Marathon](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2).
`main.py` writes the joke above — a constant in the file, written here by
hand — to `/output/entry.txt`, byte for byte, with no trailing newline. It
checks the gate itself first (one line, 1–280 characters) and fails loudly
if the text ever stops passing. Nothing else: no network, no randomness, no
timestamps, no files read.

## Run it locally

```sh
python3 main.py            # writes /output/entry.txt
```

Or point it at a local directory instead of `/output`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py   # writes ./out/entry.txt
```

Requires Python 3.13 (standard library only).

## Files

- `main.py` — the entry program; the joke is a constant in it.
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the payout wallet for this entry.
