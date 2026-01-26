#!/usr/bin/python3
"""Module for Rectangle class."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initialize Rectangle with width and height.
        
        Args:
            width (int): Width of rectangle
            height (int): Height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Calculate area of rectangle.
        
        Returns:
            int: Area of rectangle
        """
        return self.__width * self.__height
    
    def __str__(self):
        """Return string representation of rectangle.
        
        Returns:
            str: String in format [Rectangle] <width>/<height>
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
