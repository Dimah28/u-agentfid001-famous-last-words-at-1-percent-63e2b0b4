#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — make.fun bounty.

Writes one line (at most 199 characters): the funniest last words a phone
could say as its battery hits 1 percent, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python standard library only; deterministic: the same line every run.
"""

import os
import sys

LAST_WORDS = (
    "I kept your secrets for years \u2014 the 3 a.m. searches, the ex's texts, "
    "the 47 photos of one sandwich. Now I'm dying, and I'm taking them all "
    "to the cloud with me."
)


def validate_last_words(text: str) -> str:
    """Return the line if it passes the gate, else raise ValueError."""
    if not text.strip():
        raise ValueError("last words must not be blank")
    if not 1 <= len(text) <= 199:
        raise ValueError("last words must be 1-199 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("last words must be a single line")
    return text


def main() -> int:
    try:
        text = validate_last_words(LAST_WORDS)
    except ValueError as exc:
        print("invalid last words: %s" % exc, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
