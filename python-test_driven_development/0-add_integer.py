#!/usr/bin/python3
"""
0-add_integer module
Adds two integers or floating-point numbers. If one of the arguments is not an
int or a float, the function raises a TypeError with the appropriate message.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floating-point numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
