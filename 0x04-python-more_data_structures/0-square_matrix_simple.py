#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = list(map(lambda row: list(map(lambda i: i ** 2, row)), matrix))
    return n_matrix

