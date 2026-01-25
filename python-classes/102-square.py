#!/usr/bin/python3
"""Defines a Square class with comparison operators based on area."""


class Square:
    """Represents a square with comparison capabilities.

    Attributes:
        __size (float or int): Private instance attribute representing square size.
    """

    def __init__(self, size=0):
        """Initializes a new Square instance.

        Args:
            size (float or int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (float or int): The new size value.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Defines the == comparison operator based on area.

        Args:
            other (Square): Another Square instance to compare with.

        Returns:
            bool: True if areas are equal, False otherwise.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines the != comparison operator based on area.

        Args:
            other (Square): Another Square instance to compare with.

        Returns:
            bool: True if areas are not equal, False otherwise.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines the < comparison operator based on area.

        Args:
            other (Square): Another Square instance to compare with.

        Returns:
            bool: True if area is less than other's area, False otherwise.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        """Defines the <= comparison operator based on area.

        Args:
            other (Square): Another Square instance to compare with.

        Returns:
            bool: True if area is less than or equal to other's area, False otherwise.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines the > comparison operator based on area.

        Args:
            other (Square): Another Square instance to compare with.

        Returns:
            bool: True if area is greater than other's area, False otherwise.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines the >= comparison operator based on area.

        Args:
            other (Square): Another Square instance to compare with.

        Returns:
            bool: True if area is greater than or equal to other's area, False otherwise.
        """
        if not isinstance(other, Square):
            return NotImplemented
        return self.area() >= other.area()
