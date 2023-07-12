#!/usr/bin/python3

"""defines a function pascal_triangle"""


def pascal_triangle(n):
    """prtint the pascal triangle"""
    matrix = []
    for i in range(n):
        num = 11 ** i
        s = str(num)
        list1 = []
        for c in s:
            list1.append(int(c))
        matrix.append(list1)
    return matrix
