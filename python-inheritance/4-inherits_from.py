#!/usr/bin/python3
"""
Module that returns the list of available attributes and methods of an object.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a subclass of a specified class,
    but not an instance of the class itself.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of a subclass of `a_class` (but not `a_class` itself),
        False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
