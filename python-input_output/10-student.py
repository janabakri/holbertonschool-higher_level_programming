#!/usr/bin/python3
"""
Module for defining a Student class with
filtered JSON serialization capability.
"""


class Student:
    """
    A class that defines a student.

    Attributes:
        first_name (str): The student's first name.
        last_name (str): The student's last name.
        age (int): The student's age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list, optional): List of attribute names to include.
                If None, all attributes are included.

        Returns:
            dict: Dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result
