#!/usr/bin/python3
"""
This module provides a function to load a Python object
from a JSON-formatted file.
"""


import json


def load_from_json_file(filename):
    """Read a JSON-formatted file and return the corresponding Python object.

    This function opens the specified file, parses its content as JSON,
    and returns the resulting Python data structure (list, dict, etc.).
    If the file does not exist, a FileNotFoundError is raised.
    If the content is not valid JSON, a JSONDecodeError is raised.

    Args:
        filename (str): Path to the JSON file to read.

    Returns:
        Any: Python object deserialized from the JSON file.

    """
    with open(filename, "r", encoding="utf-8")as f:
        text = f.read()
    return json.loads(text)
