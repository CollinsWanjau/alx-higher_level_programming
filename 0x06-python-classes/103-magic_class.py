#!/usr/bin/python3
"""Similar to a python bytecode"""
import math


class MagicClass:
    """set up the magic"""

    def __init__(self, radius=0):
        """Disassembly of init"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Disassembly of area"""
        return self.radius ** 2 * math.pi

    def circumference(self):
        """Disassembly of circumference"""
        return math.pi * 2 * self.radius
