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
    
    # Flag to skip spaces at the beginning of a new line
    skip_spaces = False
    i = 0
    
    while i < len(text):
        # Print current character
        print(text[i], end='')
        
        # If we encounter .?:, print two new lines
        if text[i] in ".?:":
            print("\n")
            skip_spaces = True
        
        # Move to next character
        i += 1
        
        # Skip spaces at the beginning of a new line
        if skip_spaces and i < len(text) and text[i] == ' ':
            while i < len(text) and text[i] == ' ':
                i += 1
            skip_spaces = False
