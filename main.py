#!/usr/bin/env python3
"""Emit a single hugging-face emoji into /output/entry.txt.

The program is fully deterministic: it never touches the network,
never reads the clock and never rolls any dice.
"""

import os
import sys

EMOJI = "🤗"
LIMIT = 8
DEST = "/output/entry.txt"


class BadEntry(ValueError):
    """Raised when the fixed entry fails a sanity check."""


def check(candidate):
    """Run every sanity check on the fixed emoji, in order."""
    if candidate == "" or candidate.strip() == "":
        raise BadEntry("entry must not be blank")
    if any(ord(ch) < 32 for ch in candidate):
        raise BadEntry("entry must not contain control characters")
    if len(candidate) > LIMIT:
        raise BadEntry("entry is longer than the allowed cap")
    if len(candidate) != 1:
        raise BadEntry("entry must be a single character")
    if candidate.isalnum() or candidate.isspace():
        raise BadEntry("entry must be an emoji, not a letter, digit or space")
    if candidate.isascii():
        raise BadEntry("entry must be a non-ASCII character")
    return candidate


def run():
    try:
        good = check(EMOJI)
    except BadEntry as problem:
        print(f"bad entry: {problem}", file=sys.stderr)
        return 1
    folder = os.path.dirname(DEST)
    os.makedirs(folder, exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as handle:
        handle.write(good)
    return 0


if __name__ == "__main__":
    sys.exit(run())
