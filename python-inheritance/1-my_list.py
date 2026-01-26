#!/usr/bin/python3
"""Module for MyList class that inherits from list."""


class MyList(list):
    """A custom list class that inherits from the built-in list class."""

    def print_sorted(self):
        """Print the list sorted in ascending order.

        This method does not modify the original list, it only prints
        a sorted version of it.
        """
        sorted_list = sorted(self)
        print(sorted_list)
