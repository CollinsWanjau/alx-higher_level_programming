#!/usr/bin/python3
"""
A module that adds a new attribute to an obj
"""


def add_attribute(obj, attr, value):
    """
    A function that adds a new attribute to an object if it's possible
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
