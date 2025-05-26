#!/usr/bin/python3
class MyList(list):
    """Custom list class that extends the built-in list.

    This class adds a method to print the list in ascending order.
    """
    def print_sorted(self):
        """Prints the list in ascending order.

        This method does not modify the original list.
        """
        print(sorted(self))
