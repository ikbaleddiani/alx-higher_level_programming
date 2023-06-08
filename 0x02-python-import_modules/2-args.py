#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    if args == 1:
        print("0 arguments.")
    elif args == 2:
        print("1 argument:")
    else:
        print("{0}".format(args - 1) + " arguments:")
    for i in range(1, args):
        print("{0}: {1}".format(i, argv[i]))
