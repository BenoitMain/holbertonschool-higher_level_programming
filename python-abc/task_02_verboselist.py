#!/usr/bin/python3
"""
Module defining a VerboseList class that extends the built-in list
and provides notifications for append, extend, remove, and pop operations.
"""


class VerboseList(list):
    """A custom list that prints notifications for modifications.

    This class extends the built-in list class and overrides
    methods that modify the list to print informative messages
    whenever an item is added or removed.

    Methods:
        append(object): Add an object to the list and print a notification.
        extend(iterable): Extend the list an iterable and print a notification.
        remove(value): Remove a value from the list and print a notification.
        pop(index=-1): Remove and return an item at a given index
            and print a notification.
    """

    def append(self, object):
        """Add an object to the end of the list.

        Args:
            object (any): The object to add to the list.
        """
        super().append(object)
        print(f"Added [{object}] to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable.

        Args:
            iterable (iterable): The iterable whose items will be added
                to the list.
        """
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, value):
        """Remove the first occurrence of value from the list.

        Args:
            value (any): The value to remove from the list.

        Raises:
            ValueError: If the value is not present in the list.
        """
        super().remove(value)
        print(f"Removed [{value}] from the list.")

    def pop(self, index=-1):
        """Remove and return an item at the given position.

        Args:
            index (int, optional): The index of the item to remove.
                Defaults to -1 (the last item).

        Returns:
            any: The item that was removed.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
