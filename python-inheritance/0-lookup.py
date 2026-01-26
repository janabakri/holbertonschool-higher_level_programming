#!/usr/bin/python3
lookup = __import__('0-lookup').lookup

# Test with various objects
print(lookup(object()))
print(lookup([]))
print(lookup({}))
