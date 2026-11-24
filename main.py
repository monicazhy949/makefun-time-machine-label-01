#!/usr/bin/env python3
"""{e["title"]}.

Writes a single line of text to /output/entry.txt.
Pure stdlib, deterministic, no network, no input files.
"""

import os

ENTRY = (
    'WARNING: Do not meet yourself. He is needier than you remember, and he already borrowed your charger.'
)
# Revision: v1 was a generic do-not-press-twice warning; the payoff (apologizing) was weak and abstract.
# Revised: replaced it with a concrete, relatable punchline — your past self is needier and already borrowed your charger.


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry must be 1-120 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
