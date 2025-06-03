#!/usr/bin/python3

def read_file(filename=""):
    """Read a UTF-8 text file and print its contents to
    stdout without a trailing newline.

    This function opens the specified file in read mode, reads its entire
    content, strips a single trailing newline character (if present),
    and prints the result to standard output without adding an extra newline.

    Args:
        filename (str): Path to the text file to be read.

    Returns:
        None
    """

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read().strip('\n') ,end="")
