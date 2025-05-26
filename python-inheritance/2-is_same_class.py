#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Check if an object is an instance of a given class.

    This function returns True if `obj` is an instance of `a_class` (including subclasses),
    and False otherwise.

    Args:
        obj (Any): The object to check.
        a_class (type): The class to compare against.

    Returns:
        bool: True if `obj` is an instance of `a_class`, False otherwise.
    """
    if not isinstance(obj, a_class):
        return False
    else:
        return True
