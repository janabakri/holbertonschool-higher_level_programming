#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', and ':'.
    
    Args:
        text (str): The text to format.
    
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        return
    i = 0
    n = len(text)
    while i < n and text[i] == ' ':
        i += 1
    while i < n:
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i < n and text[i] == ' ':
                i += 1
            continue
        i += 1
