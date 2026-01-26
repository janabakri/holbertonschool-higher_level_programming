#!/usr/bin/python3
"""Module for Rectangle class."""


class BaseGeometry:
    """Base geometry class with area and integer validator methods."""
    
    def area(self):
        """Raise exception since area is not implemented."""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.
        
        Args:
            name (str): The name of the value
            value (int): The value to validate
            
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is not greater than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A rectangle class that inherits from BaseGeometry."""
    
    def __init__(self, width, height):
        """Initialize a new rectangle.
        
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            
        The width and height are validated and stored as private attributes.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        """Calculate the area of the rectangle.
        
        Returns:
            int: The area (width * height)
        """
        return self.__width * self.__height
