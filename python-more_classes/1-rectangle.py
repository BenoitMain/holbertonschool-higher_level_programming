#!/usr/bin/python3

class Rectangle:
    """
    Representation of a rectangle.
        Attributes:
        width (int): Rectangle width (must be >= 0).
        height (int): Rectangle height (must be >= 0).
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int, optional): Initial width. Defaults to 0.
            height (int, optional): Initial height. Defaults to 0.

        Raises:
            TypeError: If either `width` or `height` is not an int.
            ValueError: If either `width` or `height` is < 0.
        """
        self.width = width
        self.height = height

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
