#!/usr/bin/python3
"""
A class that inherits from list
"""


class MyList(list):
    """
    class myList inherits from list
    """

    def print_sorted(self):
        """
        Public instance methods.Prints the list, but sorted
        """
        print(sorted(self))
