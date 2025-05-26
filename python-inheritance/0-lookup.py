#!/usr/bin/python3

def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of attribute and method names available in the object.
    """
    return dir(obj)
