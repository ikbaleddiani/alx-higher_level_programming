#!/usr/bin/python3
for digit1 in range(0, 8):
    for digit2 in range(0, 10):
        if digit1 < digit2:
            print("{0}{1}".format(digit1, digit2), end=", ")
print("{0}{1}".format(digit1 + 1, digit2))
