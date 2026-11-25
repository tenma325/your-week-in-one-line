#!/usr/bin/env python3
"""Your Week in One Line entry: writes the entry text to /output/entry.txt.

No network. Deterministic: every run writes exactly the same bytes.
Set ENTRY_OUTPUT_PATH to redirect the output for local testing.
"""

import os
from pathlib import Path

LINE = "Monday I said 'let's circle back.' By Friday the circle was complete and I had become the back."


def main() -> None:
    target = os.environ.get("ENTRY_OUTPUT_PATH", "/output/entry.txt")
    path = Path(target)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
    except PermissionError:
        path = Path("./output/entry.txt")
        path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")
    # The entry text is fixed; every run writes identical bytes.


if __name__ == "__main__":
    main()
