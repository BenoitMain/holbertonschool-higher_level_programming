#!/usr/bin/python3
"""
Executable script using the Python 3 interpreter.

This script defines a function that writes a string to a UTF-8 encoded
text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the number of characters
    written.

    This function opens (or creates) the specified file in write mode, writes
    the given text, and returns the count of characters successfully written.
    Existing content, if any, is overwritten.

    Args:
        filename (str): Path to the file to write. If not provided,
        defaults to an empty string.
        text (str): The string to write into the file.

    Returns:
        int: The number of characters written to the file.

    """
    with open(filename, "w", encoding="utf-8") as f:
        n = f.write(text)
    return n
