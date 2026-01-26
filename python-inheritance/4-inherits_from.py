#!/usr/bin/python3
"""Check if object inherits from class."""


def inherits_from(obj, a_class):
    """Check if object is instance of class that inherited from a_class.

    Args:
        obj: The object to check
        a_class: The class to compare against

    Returns:
        bool: True if obj is instance of subclass of a_class, False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
