"""Make the Judge Smile — make.fun entry (program/v1).

Writes a single line of at most 200 characters about a small good
thing that happened today to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is a fixed literal: no randomness, no clock, no network, no
input. Running this program twice always produces the same bytes.

Design note: the line aims at the judge's brief in order — a small
good thing today, warmth in a stranger's kindness, a surprise turn
(the rain already paid), one concrete detail (a still-warm roll, a
wink), and wording of its own rather than a greeting-card phrase.
The em dash is part of the line's rhythm, not decoration: it marks
the turn from the kindness received to the quiet delight kept.
"""

import os
from pathlib import Path

# One line, 147 characters, no trailing newline in the output file.
LINE = (
    "This morning the baker slipped a still-warm roll into my bag, "
    "winked, and said the rain had already paid for it \u2014 so I ate "
    "breakfast like a secret."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
