#!/usr/bin/python3
"""Module for checking if object is instance of class or its subclass."""


def is_kind_of_class(obj, a_class):
    """Check if object is instance of, or inherited from, a class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is instance of a_class or subclass, False otherwise
    """
    return isinstance(obj, a_class)
