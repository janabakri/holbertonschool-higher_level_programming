#!/usr/bin/python3
"""
Script that adds all command line arguments to a Python list,
and saves them to a JSON file.
"""

import sys
import os

# Import functions from previous tasks
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Filename for storing the list
filename = "add_item.json"


def main():
    """
    Main function to load existing list, add new arguments,
    and save back to file.
    """
    # Load existing list or create empty list if file doesn't exist
    if os.path.exists(filename):
        my_list = load_from_json_file(filename)
    else:
        my_list = []

    # Add all command line arguments to the list
    # sys.argv[0] is the script name, so we skip it
    for arg in sys.argv[1:]:
        my_list.append(arg)

    # Save the updated list to the file
    save_to_json_file(my_list, filename)


if __name__ == "__main__":
    main()
