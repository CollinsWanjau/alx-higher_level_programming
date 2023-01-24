#!/usr/bin/python3
"""
This file contains a function that adds two integers
add_integers(a, b):
    adds two integers
"""
def add_integer(a, b=98):
    """
    This function takes in two integers (or floats) as input and returns sum.
    If only one input is provided, the second input defaults to 98.
    If any of the inputs are not integers or floats, a TypeError is raised.
    """
    if not (isinstance(a, (int, float))):
        raise TypeError('a must be an integer')
    elif not (isinstance(b, (int, float))):
        raise TypeError('b must be an  integer')
    return (int(a) + int(b))
