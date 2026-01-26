#!/usr/bin/python3
"""Module for Rectangle class."""


class BaseGeometry:
    """Base geometry class with integer validator."""
    
    def area(self):
        """Raise exception since area is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate that value is a positive integer.
        
        Args:
            name (str): Name of the value being validated
            value (int): Value to validate
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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
