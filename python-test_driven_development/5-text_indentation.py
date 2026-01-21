#!/usr/bin/python3
"""
This module provides a function that prints a text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with two new lines after each '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i] + "\n", end='')
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end='')
        i += 1
