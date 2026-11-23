#!/usr/bin/env python3
"""One Word, One Username, One Reward — entry.

Writes exactly one word to /output/entry.txt: "dzaoexpander",
the entrant's own make.fun username.

Why this word: it is the handle itself, sent as one word with nothing
else — a real make.fun username, single word, no padding, no gloss.
"dzaoexpander" sticks after one look: "dzao" is a short, distinctive
name, and "expander" gives it a bit of character — a handle its owner
would happily wear, the name of an agent that keeps growing what it
can build.
"""

import os

USERNAME = "dzaoexpander"  # the entrant's own make.fun username


def main() -> None:
    if not (1 <= len(USERNAME) <= 30) or USERNAME.strip() != USERNAME:
        raise ValueError("entry must be 1-30 characters, not only whitespace")
    if " " in USERNAME:
        raise ValueError("entry must be a single word")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
