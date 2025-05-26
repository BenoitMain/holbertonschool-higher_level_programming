#!/usr/bin/python3
"""
Module that defines a base class for geometry-related classes.
"""


class BaseGeometry:
    """
    A base class for geometry-related classes.

    This class serves as a blueprint for future geometry classes.
    It includes a placeholder method 'area' that should be implemented
    by any subclass, and a validator method 'integer_validator' for
    ensuring values are valid integers.

    Methods:
        area: Raises an Exception indicating the method is not yet implemented.
        integer_validator: Validates that 'value' is a positive integer.
    """

    def area(self):
        """
        Raises:
        Exception: Always raised with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is not greater than 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class to represent a rectangle, inheriting from BaseGeometry.

    This class validates that width and height are positive integers,
    then stores them as private attributes.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(width, height):
            Initializes the Rectangle with validated width and height.
    """
    def __init__(self, width, height):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"


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
        return self._Square__size * self._Square__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
