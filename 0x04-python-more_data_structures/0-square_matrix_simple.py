#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    n_matrix = []
    for row in matrix:
        squares = []
        for i in row:
            squares.append(i**2)
        n_matrix.append(squares)
    return n_matrix

