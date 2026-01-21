#!/usr/bin/python3
"""
Module for text indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i] + "\n\n", end='')
            i += 1
            # Skip spaces after punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        print(text[i], end='')
        i += 1
