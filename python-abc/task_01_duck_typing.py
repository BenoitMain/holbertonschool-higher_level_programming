#!/usr/bin/python3
"""
Defines Shape, Circle, Rectangle classes and shape_info function.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        """Initialize Circle."""
        self.radius = radius
        if self.radius <= 0:
            raise ValueError("radius must be greater than 0")

    def area(self):
        """Calculate area."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize Rectangle."""
        self.width = width
        self.height = height
        if self.height <= 0 or self.width <= 0:
            raise ValueError("width and height must be greater than 0")

    def area(self):
        """Calculate area."""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of shape (duck typing)."""
    print("Area:", shape.area())
    print("Perimeter:", shape.perimeter())
