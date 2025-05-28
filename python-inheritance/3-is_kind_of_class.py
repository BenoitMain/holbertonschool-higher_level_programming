#!/usr/bin/python3
"""
Module that returns whether an object is an instance of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a class or its subclass.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to check against.

    Returns:
        True if obj is an instance of a_class or its subclass, False otherwise.
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
