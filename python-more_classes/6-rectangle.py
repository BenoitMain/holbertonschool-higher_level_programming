#!/usr/bin/python3
"""
This module provides the Rectangle class.

It supports computing area, perimeter, and text-based rendering.
"""


class Rectangle:
    """Representation of a rectangle.

    Attributes:
        number_of_instances (int): Tracks the number of Rectangle instances.
        width (int): Width of the rectangle (must be >= 0).
        height (int): Height of the rectangle (must be >= 0).
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle, increment instance counter.

        Args:
            width (int, optional): Initial width. Defaults to 0.
            height (int, optional): Initial height. Defaults to 0.

        Raises:
            TypeError: If `width` or `height` is not an int.
            ValueError: If `width` or `height` is < 0.
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle.

        The width must be an integer greater than or equal to 0.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle.

        The height must be an integer greater than or equal to 0.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area computed as width * height.
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter computed as 2*(width + height).
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Generate string representation using '#' characters.

        Returns:
            str: Multiline string of '#' forming the rectangle dimensions,
                 or an empty string if width or height is 0.
        """
        if self.width == 0 or self.height == 0:
            return ""
        lines = ["#" * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Generate an “official” string representation.

        Returns:
        str: A string that can be passed to eval() to recreate this instance.
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Print a message upon deletion and decrement instance counter."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
