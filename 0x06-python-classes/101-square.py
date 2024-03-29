#!/usr/bin/python3
"""
1. Define a class square
    Initialize a 'square' class that defines
    a square which accepts a size.
"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
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
        self.size = size
        self.position = position

    def __str__(self):
        return self.my_print()[:-1]

    @property
    def size(self):
        """
        Retrieves size of a square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Retrieve position of a square
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Modified to return the string representation of the square instead
        of directly printing it.
        """
        result = ""

        if self.size == 0:
            return "\n"
        for _ in range(self.position[1]):
            result += "\n"
        for _ in range(self.size):
            for _ in range(self.position[0]):
                result += " "
            for _ in range(self.size):
                result += "#"
            result += "\n"
        return result
