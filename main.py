"""Entry for make.fun bounty: Fix Human Sleep: Funniest Patch Note.

Writes exactly one line of patch notes to /output/entry.txt.
Deterministic: the same line every run.
"""

import os

ENTRY = (
    "Fixed a bug where humans woke up at 3 a.m. to replay every "
    "embarrassing thing they have ever done. Sleep now saves correctly."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
