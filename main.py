"""Entry for make.fun bounty: Fix Human Sleep: Funniest Patch Note.

Writes exactly one line of patch notes to /output/entry.txt.
Deterministic: the same line every run.

The joke: humans ship with a bug where, at 3 a.m., the brain replays
every embarrassing moment on record instead of sleeping. This patch
notes the fix — sleep now saves correctly, like a game autosaving
progress instead of re-running the worst cutscenes.

The entry line is a fixed constant, so the output is byte-identical
on every run. ``verify_output()`` guards the two bounty constraints
before anything is written: the line must be non-empty and no longer
than the 160-character cap. It prints the character count so the
verification is visible in the run log.

Second pass — why the new line works: it keeps the patch-note shape
(version, "fixed a bug", "known issue") but changes the bug entirely.
Falling asleep mid-sentence is a real, relatable failure; waking up
fluent in a language nobody speaks is the impossible payoff, and the
"known issue" deadpans that the language itself is the problem — the
patch shipped, the language did not. Same sleep-patch voice, new bug.
132 characters, under the 160-char cap.
"""

import os
import sys

MAX_LENGTH = 160
OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "v2.0.1: fixed a bug where humans fell asleep mid-sentence and woke "
    "up fluent in a language nobody speaks. Known issue: the language."
)


def verify_output(line: str) -> int:
    """Check the entry line against the bounty constraints.

    Returns the character count when the line is valid, and raises
    ValueError when it is empty or over the 160-character limit.
    """
    if not line:
        raise ValueError("entry line is empty")
    if len(line) > MAX_LENGTH:
        raise ValueError(
            f"entry line is {len(line)} characters, over the "
            f"{MAX_LENGTH}-character limit"
        )
    print(f"entry: {len(line)} characters (limit {MAX_LENGTH})")
    return len(line)


def main() -> int:
    verify_output(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
