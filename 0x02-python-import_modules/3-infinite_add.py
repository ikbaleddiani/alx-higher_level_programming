#!/usr/bin/python3
if _name_ == "_main_":
    from sys import argv
    args = len(argv)
    if args == 1:
        print(0)
    else:
        adds = 0
        for i in range(1, args):
            adds += int(argv[i])
            print(adds)
