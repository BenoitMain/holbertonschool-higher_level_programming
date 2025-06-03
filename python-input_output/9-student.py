#!/usr/bin/python3
"""
Module 9-student

Defines a Student class with public attributes first_name, last_name, and age,
and a method to_json() that returns a dictionary representation of the instance.
"""

class Student:
    """Represents a student with first name, last name, and age.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of the Student instance.

        The returned dictionary contains only the public instance attributes:
        'first_name', 'last_name', and 'age'.

        Returns:
            dict: Dictionary with keys 'first_name', 'last_name', and 'age'.
        """
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age
        }
