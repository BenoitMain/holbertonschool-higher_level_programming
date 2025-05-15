#!/usr/bin/python3

"""
Module 3-say_my_name
Defines the function say_my_name.
Affiche 'My name is <first_name> <last_name>'.
"""


def say_my_name(first_name, last_name=""):
    """
     Prints 'My name is <first_name> <last_name>'.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
