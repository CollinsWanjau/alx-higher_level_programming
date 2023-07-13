#!/usr/bin/python3
"""
Return True if the object is an instance of, or if the object is an
instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance or a child class
    """
    return (isinstance(obj, a_class))
