#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after each '.', '?', and ':'.
    
    Args:
        text (str): The text to format.
    
    Raises:
        TypeError: If text is not a string.
    
    Examples:
        >>> text_indentation("Hello. How are you? Fine: thanks.")
        Hello.
        <BLANKLINE>
        How are you?
        <BLANKLINE>
        Fine:
        <BLANKLINE>
        thanks.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    if not text:
        return
    
    # Remove leading and trailing spaces
    text = text.strip()
    
    result = ""
    i = 0
    length = len(text)
    
    while i < length:
        result += text[i]
        if text[i] in ".?:":
            result += "\n\n"
            # Skip any spaces immediately after the punctuation
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
    
    # Print the result without trailing newline at the end
    print(result.rstrip())

# Alternative implementation using split and join
def text_indentation_alternative(text):
    """Alternative implementation of text_indentation."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    if not text:
        return
    
    # Initialize variables
    result = ""
    i = 0
    n = len(text)
    
    # Skip leading spaces
    while i < n and text[i] == ' ':
        i += 1
    
    # Process the text
    while i < n:
        # Add current character
        result += text[i]
        
        # If we encounter punctuation, add two newlines
        if text[i] in ".?:":
            result += "\n\n"
            i += 1
            # Skip any spaces after punctuation
            while i < n and text[i] == ' ':
                i += 1
            continue
        
        i += 1
    
    # Remove trailing whitespace and print
    print(result.rstrip())
