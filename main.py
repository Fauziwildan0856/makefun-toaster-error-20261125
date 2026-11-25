#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Writes one line, at most 120 characters: the error message a kitchen
toaster shows its owner. Python 3, standard library only.
"""

import os

# The entry: a deadpan appliance error. The bread has unionised — a
# fresh surprise from a direction the obvious burnt-toast puns never
# go, in one consistent deadpan voice, and it lands on a single read.
ENTRY = "ERROR 07: The bread has unionised. Toasting suspended until demands are met."

MIN_LENGTH = 1
MAX_LENGTH = 120


def validate(text):
    """Check the entry against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    Gate: UTF-8 text of 1 to 120 characters, not only white space,
    a single line.
    """
    problems = []
    if not MIN_LENGTH <= len(text) <= MAX_LENGTH:
        problems.append(
            "length %d is outside the %d-%d character gate"
            % (len(text), MIN_LENGTH, MAX_LENGTH)
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if text.strip() == "":
        problems.append("entry must not be only white space")
    # A real appliance display shows printable text only: reject any
    # control character (tab, bell, escape, ...) that could hide in
    # the line, and prove the text encodes as UTF-8 before writing.
    if any(ord(char) < 32 or ord(char) == 127 for char in text):
        problems.append("entry must not contain control characters")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry must be UTF-8 text")
    return problems


def main():
    problems = validate(ENTRY)
    if problems:
        for problem in problems:
            print("invalid entry: %s" % problem)
        raise SystemExit(1)

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # No trailing newline: the entry is exactly the one line.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    print("wrote %d characters to %s" % (len(ENTRY), path))


if __name__ == "__main__":
    main()
