"""One-Liner Marathon entry.

Writes a single one-line comedy joke to /output/entry.txt.
Deterministic: no network, no randomness, no timestamps, no external files.
The joke is a constant in this file, written here by hand.
"""

import os

JOKE = "My therapist asked me to describe my childhood in one word; I said 'ongoing.'"


def main():
    # Gate self-check, mirroring the competition gate: 1-280 chars, one line.
    if not 1 <= len(JOKE) <= 280 or "\n" in JOKE or not JOKE.strip():
        raise SystemExit("entry fails the gate: must be one line of 1-280 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
