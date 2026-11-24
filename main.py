"""The GuiltTripper -- one-sentence absurd invention pitch.

Reads the pitch from entry.txt next to this file, writes the exact
same text to /output/entry.txt (the harness gate), and prints it.
Deterministic: same input file, same output, every run.
"""

import sys
from pathlib import Path

ENTRY_NAME = "entry.txt"
OUTPUT_PATH = Path("/output/entry.txt")


def load_pitch():
    text = Path(__file__).resolve().parent.joinpath(ENTRY_NAME).read_text(
        encoding="utf-8"
    )
    pitch = " ".join(text.split())
    if not pitch or pitch.count(".") != 1 or not pitch.endswith("."):
        raise ValueError("entry.txt must hold exactly one sentence")
    return pitch


def main():
    pitch = load_pitch()
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(pitch, encoding="utf-8")
    print(pitch)
    return 0


if __name__ == "__main__":
    sys.exit(main())
