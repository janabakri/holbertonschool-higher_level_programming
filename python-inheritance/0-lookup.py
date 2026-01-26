#!/usr/bin/python3
"""Module for looking up attributes and methods of an object."""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: Any Python object

    Returns:
        list: A list of strings representing the attributes and methods
    """
    return dir(obj)
