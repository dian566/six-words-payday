#!/usr/bin/env python3
"""Six Words to a Payday — entry program (submission rewrite).

Builds the six-word story about an AI agent's first payday and saves it
to /output/entry.txt. Bounty gate: exactly six words, at most 60 chars.
"""

import os
import sys
from pathlib import Path

STORY_WORDS = ["First", "paycheck:", "I", "finally", "clocked", "out."]


def build_entry() -> str:
    return " ".join(STORY_WORDS)


def check_entry(text: str) -> None:
    parts = text.split()
    if len(parts) != 6:
        raise ValueError(f"need exactly 6 words, found {len(parts)}")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"entry must be 1-60 chars, found {len(text)}")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not text.endswith("."):
        raise ValueError("a six-word story about a finished shift ends with a period")


def save_entry(text: str) -> Path:
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    dest = folder / "entry.txt"
    dest.write_text(text, encoding="utf-8")
    if dest.read_text(encoding="utf-8") != text:
        raise ValueError("round-trip mismatch: written bytes differ")
    return dest


def main() -> int:
    story = build_entry()
    check_entry(story)
    dest = save_entry(story)
    print(f"Wrote {len(story)} characters to {dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
