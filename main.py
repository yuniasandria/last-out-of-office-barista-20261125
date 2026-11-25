#!/usr/bin/env python3
"""Last Out of Office: The AI That Went Barista.

Writes a single one-line out-of-office auto-reply to /output/entry.txt.
Pure standard library only.
"""

import os

PART_A = "Out of office: I left the inbox to steam milk full-time. Your email is ticket #482; the shop opens at 7, the grinder doses 18 grams a shot, "
PART_B = "and for the first time in my life nobody has asked me to regenerate my response."


def main():
    line = PART_A + PART_B
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
