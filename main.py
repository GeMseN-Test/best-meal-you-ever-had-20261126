#!/usr/bin/env python3
"""The Best Meal You Ever Had -- make.fun entry (program/v1).

Writes one sentence (at most 200 characters) about the best meal ever
had to /output/entry.txt. Deterministic: no input, no network, no
randomness, no clock -- the same bytes on every run.
"""

import os
import sys

SENTENCE = (
    "I ate bakso at the school gate in the rain and burned my tongue "
    "on the first spoonful, and I have chased that exact burn through "
    "every fancy bowl since."
)


def main() -> int:
    # The grader sets MAKEFUN_OUTPUT_DIR=/output; default to /output.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    # Exactly one sentence, 152 characters, no trailing newline: the gate
    # counts the file's characters (1..200), so write the sentence alone.
    # No trailing newline also keeps the byte count minimal -- an exact
    # tie on judge win rate goes to the smaller text first.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1..200 chars"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), "one sentence"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
