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
        print("", end="")
        return
    
    # Process the text
    result = ""
    i = 0
    length = len(text)
    
    # Skip leading spaces
    while i < length and text[i] == ' ':
        i += 1
    
    while i < length:
        result += text[i]
        
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            # Skip spaces after punctuation
            while i < length and text[i] == ' ':
                i += 1
            continue
        
        i += 1
    
    # Print without trailing newline
    print(result.rstrip(), end="")
