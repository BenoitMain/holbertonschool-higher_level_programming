#!/usr/bin/python3
"""
Module that defines a base class for geometry-related classes.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class to represent a square, inheriting from Rectangle.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        __init__(size):
            Initializes the Square with a validated size.
        area():
            Calculates and returns the area of the square.
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is not greater than 0.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
