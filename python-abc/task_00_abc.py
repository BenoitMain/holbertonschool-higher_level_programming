#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal.

    This class defines the interface that all animal subclasses
    must implement. It ensures that every subclass provides
    its own implementation of the `sound` method.

    Attributes:
        None
    """
    @abstractmethod
    def sound(self):
        """Return the sound made by the animal.

        Returns:
            str: The sound specific to the animal subclass.
        """
        pass


class Dog(Animal):
    """Dog class inheriting from Animal.

    This class implements the sound method to return "Bark".
    """

    def sound(self):
        """Return the sound made by a dog.

        Returns:
            str: The string "Bark".
        """
        return ("Bark")


class Cat(Animal):
    """Return the sound made by a cat.

        Returns:
            str: The string "Meow".
        """

    def sound(self):
        return ("Meow")
