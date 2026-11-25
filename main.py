#!/usr/bin/env python3
"""Write the GPS shortcut entry to entry.txt.

Entry for make.fun's "The GPS Swears It Was a Shortcut": a smug,
defensive GPS blames the map ('the map said scenic') for a shortcut
through a corn maze, a cul-de-sac and a named neighbour's driveway,
and closes by telling the driver they needed the tour.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "That was not a wrong turn, that was a shortcut through a corn maze, a cul-de-sac and Mrs Patel's driveway - the map said scenic, and frankly, you needed the tour."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
