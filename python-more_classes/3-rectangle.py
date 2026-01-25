#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle with width and height attributes."""
    
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        
        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.
        
        Args:
            value (int): The new width value.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.
        
        Args:
            value (int): The new height value.
            
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
    
    def area(self):
        """Calculates and returns the area of the rectangle.
        
        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height
    
    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle.
        
        Returns:
            int: The perimeter of the rectangle, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """Returns a string representation of the rectangle using '#' characters.
        
        Returns:
            str: The string representation, or empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str
    
    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction.
        
        Returns:
            str: A string that can be used to recreate the rectangle instance.
        """
        return f"<3-rectangle.Rectangle object at {hex(id(self))}>"
