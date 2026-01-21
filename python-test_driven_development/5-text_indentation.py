#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after ., ? and :

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip_space = False

    for char in text:
        if char in ".?:":
            print(char, end="")
            print("\n")
            skip_space = True
        else:
            if skip_space and char == " ":
                continue
            print(char, end="")
            skip_space = False
