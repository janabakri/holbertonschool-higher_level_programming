#!/usr/bin/env python3
"""CountedIterator - iterator that counts how many items were fetched."""


class CountedIterator:
    """Wrap an iterable's iterator and count fetched items."""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)  # raises StopIteration when finished (as required)
        self._count += 1
        return item

    def get_count(self):
        """Return how many items have been iterated over so far."""
        return self._count
