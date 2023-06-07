#!/usr/bin/python3
def uppercase(str):
    output = ""
    for c in str:
        if ord(c) in range(97, 123):
            c = chr(65 + (ord(c) - 97))
            output += c
        else:
            output += c
    print("{}".format(output), end="")
    print("")
