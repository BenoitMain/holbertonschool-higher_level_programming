#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for row in matrix:
        new_row = []
        for value in row:
            value_squared = value * value
            new_row.append(value_squared)
        new_matrix.append(new_row)
    return new_matrix
