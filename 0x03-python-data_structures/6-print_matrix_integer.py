#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for row in range(len(matrix[i])):
            print("{:d}".format(matrix[i][row]), end="")
            if row != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
