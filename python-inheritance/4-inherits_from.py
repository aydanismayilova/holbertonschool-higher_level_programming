#!/usr/bin/python3
"""
Module that defines a function to check if an object
is an instance of a subclass that inherits from a_class
(but not the exact class itself).
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that
    inherited (directly or indirectly) from a_class,
    but not if it is exactly an instance of a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
