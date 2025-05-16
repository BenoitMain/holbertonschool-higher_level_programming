#!/usr/bin/python3
"""
Module 5-text_indentation

This module defines the text_indentation(text) function, which displays text
by inserting two newlines after each '.', '?', or ':'.
The text must not begin or end with a space on any line.
"""


def text_indentation(text):
    """
    Displays text with two line breaks after each '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    buffer = ""
    for i in text:
        buffer += i
        if i in ".?:":
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip(), end="")
