#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx in range(len(row)):
            value = row[idx]
            if idx == len(row) - 1:
                print("{:d}".format(value), end="")
            else:
                print("{:d}".format(value), end=" ")
        print()
