#!/usr/bin/python3
"""Module for text_indentation."""


def text_indentation(text):
    """Print text with 2 new lines after .?:"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    if text == "":
        return
    
    text = text.strip()
    
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    
    lines = result.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if i == len(lines) - 1:
            print(line, end="")
        else:
            print(line)
