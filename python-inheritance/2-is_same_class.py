#!/usr/bin/python3
"""Module for checking if an object is exactly an instance of a class."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specific class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
