#!/usr/bin/python3
"""
Class Rectangle that defines a rectangle with width and height,
and calculates area and perimeter.
"""


class Rectangle:
    """Rectangle class with width and height properties"""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter, 0 if width or height is 0"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)
