#!/usr/bin/env python3
"""Implementation of Person class"""
class Person:
    """Person class"""
    def __init__ (self, name, birthday):
        self.name = name
        self.birthday = birthday

    def to_string(self):
        """Print the details of the person in a string"""
        print(self.name + "'s birthday is on " + self.birthday)

#p1 = person("Ng Shien Ming", "02/06/2002")
#p1.toString()
print(__name__)
