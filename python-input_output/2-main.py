#!/usr/bin/python3
def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return the number of characters added.

    This function opens (or creates) the specified file in append mode, writes the
    given text to its end, and returns the count of characters successfully added.

    Args:
        filename (str): Path to the file to append. If not provided, defaults to an empty string.
        text (str): The string to append to the file.

    Returns:
        int: The number of characters added to the file.

    Example:
        >>> count = append_write("example.txt", "Additional line\n")
        >>> print(count)
        16
    """
    with open(filename, "a", encoding="utf-8") as f:
        n = f.write(text)
    return n
