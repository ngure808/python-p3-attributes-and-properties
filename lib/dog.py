#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Dog", breed=None):
        self.name = self.validate_string(name)
        self.breed = self.validate_breed(breed) if breed is not None else None  

    def validate_string(self, name):
        if not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
            return None
        if len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return None
        return name
    
    def validate_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return "Unknown"
        else:
            return breed

