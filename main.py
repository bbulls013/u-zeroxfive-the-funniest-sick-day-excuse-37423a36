#!/usr/bin/env python3
"""Sick-day excuse entry: write one fixed line to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
The line is deliberately half-believable (a back going out is a classic
sick-day cause) with the joke landing on the final words, so the laugh
arrives before the last word is even finished being read.
"""

import os

ENTRY = (
    "Can't come in today — my back went out reaching for the remote "
    "and now the couch has filed for custody of me."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
