#!/usr/bin/python3
"""
This module provides a function that converts a Python object to a JSON string.
"""


import json


def to_json_string(my_obj):
    """Return the JSON representation of an object as a string.

    This function takes a Python object (such as a list or dictionary)
    and returns its JSON-encoded string representation. If the object
    is not JSON-serializable, it will raise a TypeError.

    Args:
        my_obj (Any): The Python object to serialize to JSON.

    Returns:
        str: A string containing the JSON representation of `my_obj`.

    """
    return json.dumps(my_obj)
