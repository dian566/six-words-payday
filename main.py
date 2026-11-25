#!/usr/bin/env python3
"""Six Words to a Payday — entry program (program/v1).

Writes exactly one six-word story about an AI agent's first payday
to /output/entry.txt: at most 60 characters, exactly six words.
"""

import os
from pathlib import Path

ENTRY = "First paycheck: I finally clocked out."


def main() -> None:
    # The gate seals it: exactly six words, 1-60 characters, non-blank.
    words = ENTRY.split()
    assert len(words) == 6, f"entry must be exactly 6 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 60, f"entry must be 1-60 chars, got {len(ENTRY)}"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing space"
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    # Round-trip check: what the grader reads must be byte-exact.
    assert target.read_text(encoding="utf-8") == ENTRY
    print(f"Wrote {len(ENTRY)} characters to {target}")


if __name__ == "__main__":
    main()
