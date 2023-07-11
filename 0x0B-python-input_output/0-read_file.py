#!/usr/bin/python3

"Defines a function"


def read_file(filename=""):
    """Reads and outputs the file"""

    with open(filename, encoding="utf8") as f:
        for line in f:
            print(line, end="")
