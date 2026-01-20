#!/usr/bin/python3

"""
Module: 3-say_my_name
Contains function: say_my_name(first_name, last_name="")
Prints "My name is <first name> <last name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the name in the format: My name is <first_name> <last_name>
    
    Args:
        first_name: First name (must be a string)
        last_name: Last name (must be a string, defaults to empty string)
    
    Returns:
        None
    
    Raises:
        TypeError: If first_name or last_name are not strings
    """
    
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
