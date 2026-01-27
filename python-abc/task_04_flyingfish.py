#!/usr/bin/env python3

# Parent class Fish
class Fish:
    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        print("The fish lives in water")


# Parent class Bird
class Bird:
    def fly(self):
        print("The bird is flying")

    def habitat(self):
        print("The bird lives in the sky")


# Child class FlyingFish with multiple inheritance
class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")

    def fly(self):
        print("The flying fish is soaring!")

    def habitat(self):
        print("The flying fish lives both in water and the sky!")
