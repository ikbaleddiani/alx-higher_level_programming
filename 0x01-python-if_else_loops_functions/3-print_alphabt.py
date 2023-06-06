#!/usr/bin/python3
letters_except = "q" + "e"
for letter in range(ord('a'), ord('z')+1):
    if chr(letter) not in letters_except:
        print("{}".format(chr(letter)), end="")
