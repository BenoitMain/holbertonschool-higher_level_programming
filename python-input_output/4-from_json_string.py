#!/usr/bin/python3
"""
This script defines a function to deserialize a JSON-formatted string
into a native Python data structure.
"""


import json


def from_json_string(my_str):
    """Convert a JSON-encoded string to a Python object.

    This function takes a string containing JSON data and returns
    the corresponding Python object (e.g., list, dict). If the input
    string is not valid JSON, a JSONDecodeError will be raised.

    Args:
        my_str (str): A JSON-encoded string.

    Returns:
        Any: The Python object represented by the JSON string.

    """
    return json.loads(my_str)
