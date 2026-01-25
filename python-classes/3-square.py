#!/usr/bin/python3
"""Defines a Square class with size validation and an area method."""


class Square:
    """Represents a square with a private validated size."""

    def __init__(self, size=0):
        """Initialize a new Square with a validated size."""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
