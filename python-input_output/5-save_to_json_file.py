#!/usr/bin/python3
"""
This script defines a function to save a Python object
to a text file using its JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file in JSON format.

    This function serializes the given Python object to JSON and writes
    it to the specified file. If the file already exists, its content
    is overwritten. If the object is not JSON-serializable, a TypeError
    will be raised.

    Args:
        my_obj (Any): The Python object to serialize (e.g., list, dict).
        filename (str): The path to the text file where JSON will be saved.

    Returns:
        None
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
