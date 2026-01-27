#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A base geometry class."""

    def area(self):
        """Calculate area - not implemented.

        Raises:
            Exception: Always, with message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name: Name of the value (always a string)
            value: Value to validate

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
