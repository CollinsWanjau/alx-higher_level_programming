#!/usr/bin/python3
"""
A class that inherits from class Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes with size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
