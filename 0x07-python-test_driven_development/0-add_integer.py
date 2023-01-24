#!/usr/bin/python3
"""
This file contains a function that adds two integers
add_integers(a, b):
    adds two integers
"""


def add_integer(a, b=98):
    """
    add two integers a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
