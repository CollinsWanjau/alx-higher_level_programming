#!/usr/bin/python3
"""
Returns true if the object is an instance of a class that inherited(directly or indirectly)
from the specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if an instance is inherited
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
