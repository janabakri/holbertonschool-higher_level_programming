#!/usr/bin/env python3
"""Extending Python list with notifications."""


class VerboseList(list):
    """A list that prints notifications on modifications."""

    def append(self, item):
        """Add an item and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend list and print how many items were added."""
        items = list(iterable)
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """Remove an item and print a notification (before removal)."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and print a notification (before popping)."""
        item = self[index]  # may raise IndexError (same as normal list)
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
