#!/usr/bin/python3

"""
Module 4-print_square
Prints a square made of the character '#'. size must be an integer greater than
or equal to 0,otherwise an exception is raised.
"""


def print_square(size):
    """
    Prints a square of the given size using the '#' character.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
