#!/usr/bin/python3
"""
Text indentation module
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    n = len(text)

    # Skip leading spaces
    while i < n and text[i] == ' ':
        i += 1

    while i < n:
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            i += 1
            # Skip spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
            continue

        i += 1
