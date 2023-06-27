#!/usr/bin/python3
"""
1. Define a class square
    Initialize a 'square' class that defines
    a square which accepts a size.
"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """
        Initialize class with size
        Args:
            size (int): The size of the new square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Returns:
            The area of the square
        """
        return (self.__size ** 2)
