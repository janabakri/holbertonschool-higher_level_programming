#!/usr/bin/env python3
"""
Task 1: Pickling Custom Classes
Serialize and deserialize custom Python objects using the pickle module.
"""

import pickle
import os


class CustomObject:
    """
    A custom Python class that can be serialized and deserialized using pickle.
    """
    
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename: str) -> bool:
        """
        Serialize the current instance and save it to a file.
        
        Returns:
            bool: True if serialization succeeded, False otherwise
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            return True
        except Exception as e:
            print(f"Serialization error: {e}")
            return False
    
    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize a CustomObject from a file.
        
        Returns:
            CustomObject or None: The deserialized object, or None if an error occurred
        """
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File '{filename}' does not exist")
            
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            
            if not isinstance(obj, cls):
                raise TypeError(f"Deserialized object is not of type {cls.__name__}")
            
            return obj
        except Exception as e:
            print(f"Deserialization error: {e}")
            return None
