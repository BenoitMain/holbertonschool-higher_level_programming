#!/usr/bin/python3
"""
Module that defines an abstract Shape class and concrete implementations:
Circle and Rectangle. It also includes a function to display shape info
using duck typing.

Classes:
    Shape: Abstract base class for shapes.
    Circle: Concrete implementation of a circle.
    Rectangle: Concrete implementation of a rectangle.

"""


import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a generic shape.

    This class defines the interface that all shape subclasses
    must implement. It includes abstract methods for calculating
    the area and perimeter of the shape.
    """

    @abstractmethod
    def area(self):
        """Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape.

        Returns:
            float: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """Concrete class representing a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """Initialize a circle with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """Calculate the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width, height):
        """Initialize a rectangle with given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Print the area and perimeter of a shape object.

    This function relies on duck typing and assumes that the
    object has `area()` and `perimeter()` methods.

    Args:
        obj (object): An object representing a shape,
            expected to have `area()` and `perimeter()` methods.
    """

    print(f"Area:", obj.area())
    print(f"Perimeter:", obj.perimeter())
