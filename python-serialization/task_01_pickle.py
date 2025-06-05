#!/usr/bin/python3
""""
Learn how to serialize and deserialize custom Python objects using
 the pickle module.

"""


import pickle


class CustomObject:
    """Represents an object with name, age, and student status,
    serializable via pickle.

    Attributes:
        name (str): The name of the object.
        age (int): The age of the object.
        is_student (bool): True if the object represents a student.
    """

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance.

        Args:
            name (str): The name to assign to the instance.
            age (int): The age to assign to the instance.
            is_student (bool): The student status of the instance.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in a readable format.

        The output format is:
            Name: <name>
            Age: <age>
            Is Student: <is_student>
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize this instance to a binary file using pickle.

        Attempts to open `filename` in binary write mode and pickle this
        instance into it. If any exception occurs (e.g., permission error,
        disk full), returns None.

        Args:
            filename (str): Path to the file where the instance will be saved.

        Returns:
            bool or None: True if serialization was successful, None otherwise.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject instance from a pickle file.

        Attempts to open `filename` in binary read mode and unpickle an
        object from it. If the file does not exist, is not a valid pickle,
        or the unpickled object is not a CustomObject, returns None.

        Args:
            filename (str): Path to the pickle file to read.

        Returns:
            CustomObject or None: The deserialized instance, or None .
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if not isinstance(obj, cls):
                    return None
                return obj
        except Exception:
            return None
