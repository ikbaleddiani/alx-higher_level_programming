#!/usr/bin/python3

"""defines a function write_file"""


def write_file(filename="", text=""):
    """return the number of chara written"""

    with open(filename, 'w', encoding="utf8") as f:
        return f.write(text)
