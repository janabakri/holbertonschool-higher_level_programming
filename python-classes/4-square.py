#!/usr/bin/python3
"""Defines a Square class with a validated size property and area method."""


class Square:
    """Represents a square with a private validated size."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size."""
        self.size = size  # uses the setter (validates)

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
