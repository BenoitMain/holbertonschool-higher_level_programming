#!/usr/bin/python3
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

    Example:
        >>> to_json_string([1, 2, 3])
        '[1, 2, 3]'
        >>> to_json_string({'id': 12, 'name': 'John'})
        '{"id": 12, "name": "John"}'
    """
    return json.dumps(my_obj)
