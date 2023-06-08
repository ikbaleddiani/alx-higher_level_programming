#!/usr/bin/python3
for i in range(-25, 1):
    numb = 90 if i % 2 == 0 else 122
    print("{}".format(chr(numb - 25 - i)), end="")
