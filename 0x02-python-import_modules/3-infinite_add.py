#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    if args == 1:
        print(0)
        exit(0)
    adds = 0
    for i in range(1, args):
        adds += int(argv[i])
    print(adds)
