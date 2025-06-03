#!/usr/bin/python3

def class_to_json(obj):

    """Return the instance attributes of an object as
    a JSON-serializable dictionary.

    This function retrieves the `__dict__` attribute of a class instance,
    which contains all its instance attributes (keys and values).
    It is assumed that all attribute values are of simple data types
    (list, dict, str, int, bool) that can be directly serialized to JSON.

    Args:
        obj (Any): An instance of a class whose attributes
        are JSON-serializable.

    Returns:
        dict: A dictionary containing the instance’s attribute
        names and values, suitable for JSON serialization.

    """
    return obj.__dict__
