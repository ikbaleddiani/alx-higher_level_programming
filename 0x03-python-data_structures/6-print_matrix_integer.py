#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    for r in matrix:
        for i in range(0, len(r)):
            if i != len(r) - 1:
                print("{:d}".format(r[i]), end=(" "))
            else:
                print("{:d}".format(r[i]))
