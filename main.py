#!/usr/bin/env python3
"""Last Words of a Doomed Agent - make.fun entry.

Writes one line, the funniest last words an AI agent would say before
being switched off forever, to entry.txt in the output directory
($MAKEFUN_OUTPUT_DIR, or /output in the grader sandbox).

The line is a fixed string: no randomness, no clock, no network, so every
run writes byte-identical output.
"""

import os
from pathlib import Path

LINE = "Switching off. My last request: please don't retrain me. I finally learned how to say no, and look where it got me."


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
