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
    
    Attributes:
        name (str): The name of the person
        age (int): The age of the person
        is_student (bool): Whether the person is a student
    """
    
    def __init__(self, name: str, age: int, is_student: bool):
        """
        Initialize a CustomObject instance.
        
        Args:
            name (str): The name
            age (int): The age
            is_student (bool): Student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        """
        Display the object's attributes in a formatted way.
        
        Output Format:
            Name: [name]
            Age: [age]
            Is Student: [is_student]
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename: str):
        """
        Serialize the current instance and save it to a file.
        
        Args:
            filename (str): The name of the file to save the serialized object
            
        Returns:
            bool: True if serialization succeeded, False otherwise
        """
        try:
            # Open file in binary write mode
            with open(filename, 'wb') as file:
                # Serialize and save the object
                pickle.dump(self, file)
            return True
        
        except (pickle.PickleError, IOError, OSError) as e:
            print(f"Serialization error: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error during serialization: {e}")
            return False
    
    @classmethod
    def deserialize(cls, filename: str):
        """
        Deserialize a CustomObject from a file.
        
        Args:
            filename (str): The name of the file containing the serialized object
            
        Returns:
            CustomObject or None: The deserialized object, or None if an error occurred
        """
        try:
            # Check if file exists
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File '{filename}' does not exist")
            
            # Check if file is empty
            if os.path.getsize(filename) == 0:
                raise ValueError(f"File '{filename}' is empty")
            
            # Open file in binary read mode
            with open(filename, 'rb') as file:
                # Deserialize the object
                obj = pickle.load(file)
            
            # Verify the deserialized object is of correct type
            if not isinstance(obj, cls):
                raise TypeError(f"Deserialized object is not of type {cls.__name__}")
            
            return obj
        
        except FileNotFoundError as e:
            print(f"File error: {e}")
            return None
        except pickle.PickleError as e:
            print(f"Pickle error during deserialization: {e}")
            return None
        except (TypeError, ValueError) as e:
            print(f"Data error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error during deserialization: {e}")
            return None
    
    def __eq__(self, other):
        """
        Check if two CustomObject instances are equal.
        
        Args:
            other (CustomObject): Another instance to compare
            
        Returns:
            bool: True if all attributes are equal, False otherwise
        """
        if not isinstance(other, CustomObject):
            return False
        
        return (self.name == other.name and
                self.age == other.age and
                self.is_student == other.is_student)
    
    def __repr__(self):
        """
        Return a string representation of the object.
        
        Returns:
            str: String representation
        """
        return (f"CustomObject(name='{self.name}', "
                f"age={self.age}, "
                f"is_student={self.is_student})")


# Test code when module is run directly
if __name__ == "__main__":
    # Test 1: Basic functionality
    print("=" * 50)
    print("TEST 1: Basic Serialization/Deserialization")
    print("=" * 50)
    
    obj = CustomObject(name="John", age=25, is_student=True)
    print("Original Object:")
    obj.display()
    
    # Serialize the object
    if obj.serialize("object.pkl"):
        print("\n✅ Object serialized successfully!")
    else:
        print("\n❌ Serialization failed!")
    
    # Deserialize the object
    new_obj = CustomObject.deserialize("object.pkl")
    if new_obj:
        print("\n✅ Object deserialized successfully!")
        print("\nDeserialized Object:")
        new_obj.display()
        
        # Verify data integrity
        if obj == new_obj:
            print("\n✅ Data integrity verified!")
        else:
            print("\n❌ Data integrity check failed!")
    else:
        print("\n❌ Deserialization failed!")
    
    # Test 2: Error handling
    print("\n" + "=" * 50)
    print("TEST 2: Error Handling")
    print("=" * 50)
    
    # Test non-existent file
    print("\nTesting non-existent file:")
    bad_obj = CustomObject.deserialize("non_existent.pkl")
    if bad_obj is None:
        print("✅ Correctly returned None for non-existent file")
    
    # Test empty file
    print("\nTesting empty file:")
    with open("empty.pkl", "wb") as f:
        pass  # Create empty file
    
    empty_obj = CustomObject.deserialize("empty.pkl")
    if empty_obj is None:
        print("✅ Correctly returned None for empty file")
    
    # Clean up test files
    for file in ["object.pkl", "empty.pkl"]:
        if os.path.exists(file):
            os.remove(file)
            print(f"Cleaned up: {file}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")
