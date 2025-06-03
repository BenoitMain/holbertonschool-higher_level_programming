#!/usr/bin/python3
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

    Example:
        >>> from_json_string('[1, 2, 3]')
        [1, 2, 3]
        >>> from_json_string('{"id": 12, "name": "John"}')
        {'id': 12, 'name': 'John'}
    """
    return json.loads(my_str)
