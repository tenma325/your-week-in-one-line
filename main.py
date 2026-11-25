#!/usr/bin/env python3
"""Your Week in One Line - make.fun entry.

Running this program writes the entry text to /output/entry.txt.
The text sums up my week in a single line, fixed in the source
below, so every run produces exactly the same bytes. The
program uses only the Python standard library and never touches
the network. Set ENTRY_OUTPUT_PATH to redirect the output for
local testing.
"""

import os
from pathlib import Path

ENTRY_TEXT = "Monday I said 'let's circle back.' By Friday the circle was complete and I had become the back."
MAX_CHARS = 100


def main() -> None:
    if not 1 <= len(ENTRY_TEXT) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(ENTRY_TEXT)}"
        )
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
