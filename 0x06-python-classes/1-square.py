#!/usr/bin/python3
"""
1. Define a class square
    Initialize a 'square' class that defines
    a square which accepts a size.
"""


class Square:
    """Represent a square"""

    def __init__(self, size):
        """
        Initialize class with size
        Args:
            size (int): The size of the new square
        """
        self.__size = size
