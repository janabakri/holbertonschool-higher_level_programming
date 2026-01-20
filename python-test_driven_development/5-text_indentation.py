#!/usr/bin/python3
"""
Module: 5-text_indentation

Contains function: text_indentation(text)
Prints a text with 2 new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each ., ? and :
    Args:
        text: The text to process (must be a string)

    Returns:
        None

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    i = 0
    length = len(text)

    while i < length:
        result += text[i]

        if text[i] in ".?:":
            result += "\n\n"

            i += 1
            while i < length and text[i] == ' ':
                i += 1
            continue

        i += 1

    lines = result.split('\n')
    for j, line in enumerate(lines):
        print(line.strip(), end='' if j == len(lines) - 1 else '\n')
