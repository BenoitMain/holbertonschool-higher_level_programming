#!/usr/bin/python3
"""
This module defines a Square class used to represent a square shape.

Classes:
    Square: Represents a square with a private size attribute.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.

        Args:
            size (int): The size of the square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Args:
        value (int): New size, must be integer >= 0.
        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is negative.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The current square’s area, computed as size squared.
        """
        return self.__size ** 2
