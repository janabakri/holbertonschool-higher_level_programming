#!/usr/bin/python3
"""
This module contains a function that prints a text with indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?' and ':' characters.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    length = len(text)
    result = ""
    
    while i < length:
        result += text[i]
        
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            # Skip spaces after punctuation
            while i < length and text[i] == " ":
                i += 1
            continue
        
        i += 1
    
    # Print without extra newlines
    lines = result.split("\n")
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            print(line.strip(), end="")
        else:
            print(line.strip())
