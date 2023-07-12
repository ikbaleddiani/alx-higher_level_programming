#!/usr/bin/python3

"""define a function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """append_after"""

    txt =  ""
    with open(filename) as f:
        for line in f:
            txt = txt + line
            if search_string in line:
                txt = txt + new_string
    with open(filename, "w") as f:
        f.write(txt)
