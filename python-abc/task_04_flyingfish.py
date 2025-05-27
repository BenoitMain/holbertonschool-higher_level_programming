#!/usr/bin/python3
"""
Module defining Fish, Bird, and FlyingFish classes to demonstrate
multiple inheritance and method resolution order (MRO) in Python.
"""


class Fish:
    """A class representing a fish.

    Methods:
        swim(): Print a message indicating that the fish is swimming.
        habitat(): Print a message indicating the fish's habitat.
    """

    def swim(self):
        """Print a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message indicating the fish's habitat (water)."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird.

    Methods:
        fly(): Print a message indicating that the bird is flying.
        habitat(): Print a message indicating the bird's habitat.
    """

    def fly(self):
        """Print a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message indicating the bird's habitat (sky)."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish, inheriting from both Fish and Bird.

    Methods:
        fly(): Print a message indicating that the flying fish is soaring.
        swim(): Print a message indicating that the flying fish is swimming.
        habitat():Print a  indicating the dual habitat of the flying fish.
    """

    def fly(self):
        """Print a message indicating that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print a message indicating the flying fish's dual habitat."""
        print("The flying fish lives both in water and the sky!")
