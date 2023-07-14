#!/usr/bin/python3
"""
A class that inherits from int
"""


class MyInt(int):
    """
    a class MyInt that inherits from int
    """

    def __eq__(self, value):
        """
        Override == operator with !=
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override != operator with ==
        """
        return self.real == value
