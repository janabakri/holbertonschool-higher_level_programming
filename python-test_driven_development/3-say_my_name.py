#!/usr/bin/python3
"""Module for say_my_name function."""


def say_my_name(first_name, last_name=""):
    """Print a name in the format 'My name is <first_name> <last_name>'.
    
    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".
    
    Raises:
        TypeError: If first_name or last_name is not a string.
    
    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Bob")
        My name is Bob
        >>> say_my_name("Bob", "")
        My name is Bob
        >>> try:
        ...     say_my_name(12, "White")
        ... except Exception as e:
        ...     print(e)
        first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    # Print without extra space when last_name is empty
    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
