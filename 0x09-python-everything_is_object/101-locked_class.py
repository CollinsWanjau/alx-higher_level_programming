#!/usr/bin/python3
"""Explicitly define the attrs a class can have"""


class LockedClass:
    """Prevents the user from dynamically creating new instance attributes"""

    __slots__ = ["first_name"]
