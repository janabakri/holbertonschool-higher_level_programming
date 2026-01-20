#!/usr/bin/python3
"""
This module prints a square with the character '#'
of any positive integer size.

Example:

    ###
    ###
    ###

    * The size must be an integer greater than 0.
"""


def print_square(size):
    """
    Prints a square with the character '#'

    Args:
        size (int): The size of the square to print.

    Raises:
        TypeError: If `size` isn't integer.
        ValueError: If `size` is less than 0.
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    for i in range(size):
        print("#" * size)
