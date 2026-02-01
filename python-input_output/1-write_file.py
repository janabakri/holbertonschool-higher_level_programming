#!/usr/bin/python3
"""
Module for writing a string to a text file and
returning the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns
    the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text string to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
        return characters_written
