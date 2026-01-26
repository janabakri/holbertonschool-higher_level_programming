#!/usr/bin/python3
"""Module for Square class."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    
    def __init__(self, size):
        """Initialize Square with size.
        
        Args:
            size (int): Size of square (both width and height)
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
