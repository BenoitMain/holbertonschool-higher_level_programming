class CountedIterator:
    """Iterator wrapper that counts how many items have been fetched."""

    def __init__(self, iterable):
        """Initialize with an iterable and start count at 0."""
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the current count of iterated items."""
        return self.count

    def __next__(self):
        """Return the next item and increment the count.

        Raises:
            StopIteration: When no more items are left to iterate.
        """
        item = next(self.iterator)  # Appelle l’itérateur interne
        self.count += 1
        return item
