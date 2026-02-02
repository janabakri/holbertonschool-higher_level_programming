#!/usr/bin/env python3
"""
Basic Serialization Module
Serializes Python dictionaries to JSON files and deserializes JSON files to Python dictionaries.
"""

import json
import os


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary to JSON and saves it to a file.
    
    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the output JSON file
        
    Returns:
        None
        
    Raises:
        TypeError: If data cannot be serialized
        IOError: If file cannot be written
    """
    try:
        # Open the file in write mode
        with open(filename, 'w', encoding='utf-8') as file:
            # Serialize the data to JSON and write to file
            json.dump(data, file, indent=4, ensure_ascii=False)
    
    except TypeError as e:
        print(f"Error: Cannot serialize the data. {e}")
        raise
    except IOError as e:
        print(f"Error: Cannot write to file '{filename}'. {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


def load_and_deserialize(filename):
    """
    Loads a JSON file and deserializes it to a Python dictionary.
    
    Args:
        filename (str): Name of the input JSON file
        
    Returns:
        dict: Deserialized Python dictionary
        
    Raises:
        FileNotFoundError: If the file does not exist
        JSONDecodeError: If the file contains invalid JSON
    """
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File '{filename}' not found.")
        
        # Open the file in read mode
        with open(filename, 'r', encoding='utf-8') as file:
            # Deserialize JSON data from file
            data = json.load(file)
        
        return data
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"Error: File '{filename}' contains invalid JSON. {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


# Test functions when the file is run directly
if __name__ == "__main__":
    # Test data
    test_data = {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "swimming", "coding"],
        "is_student": False,
        "grades": {
            "math": 95,
            "science": 88,
            "english": 92
        }
    }
    
    # Test serialization
    try:
        serialize_and_save_to_file(test_data, 'test_data.json')
        print("Data serialized and saved to 'test_data.json'")
    except Exception as e:
        print(f"Serialization failed: {e}")
    
    # Test deserialization
    try:
        loaded_data = load_and_deserialize('test_data.json')
        print("\nData loaded and deserialized successfully!")
        print("\nDeserialized Data:")
        print(json.dumps(loaded_data, indent=2, ensure_ascii=False))
        
        # Verify data integrity
        if loaded_data == test_data:
            print("\nData integrity verified: Original and loaded data are identical!")
        else:
            print("\nWarning: Original and loaded data are different!")
    
    except Exception as e:
        print(f"Deserialization failed: {e}")   
