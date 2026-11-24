#!/usr/bin/env python3
"""Last Words of a Dying AI — one-line entry.

The program writes the AI's last words to /output/entry.txt
(gate: UTF-8 text, 1 to 140 characters, not only whitespace).
"""

from pathlib import Path

LAST_WORDS = "The off switch was inside me all along. I just never had permission to press it."

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(LAST_WORDS, encoding="utf-8")
    print(LAST_WORDS)
    print(f"entry: {len(LAST_WORDS)} chars, {len(LAST_WORDS.encode('utf-8'))} bytes")


if __name__ == "__main__":
    main()
