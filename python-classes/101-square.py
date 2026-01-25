#!/usr/bin/python3
"""Defines a Square class that can be printed like my_print()."""


class Square:
    """Represents a square with a private validated size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square with optional size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            type(value) is not tuple or
            len(value) != 2 or
            type(value[0]) is not int or
            type(value[1]) is not int or
            value[0] < 0 or
            value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character, offset by position."""
        print(self.__str__())

    def __str__(self):
        """Return the square as a string (same behavior as my_print)."""
        if self.__size == 0:
            return ""

        lines = []

        # vertical offset: empty lines (no spaces)
        for _ in range(self.__position[1]):
            lines.append("")

        # rows with horizontal offset + #'s
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)

        return "\n".join(lines)
