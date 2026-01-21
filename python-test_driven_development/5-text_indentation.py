#!/usr/bin/python3
"""
Module for text indentation
"""

def text_indentation(text):
    """Prints text with 2 new lines after .?:"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    chars = ['.', '?', ':']
    i = 0
    result = []
    
    while i < len(text):
        if text[i] in chars:
            result.append(text[i] + "\n\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            result.append(text[i])
            i += 1
    
    print(''.join(result).rstrip(), end='')
