#!/usr/bin/python3
"""
A module that contains inherited class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Instantiation with width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description
        """
        return ("[{}] {}/{}".
                format(self.__class__.__name__, self.__width, self.__height))
