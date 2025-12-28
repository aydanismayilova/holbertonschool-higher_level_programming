#!/usr/bin/python3
"""
Module that defines a BaseGeometry class.
"""


class BaseGeometry:
    """BaseGeometry class with an unimplemented area method."""

    def area(self):
        """Raises an Exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")
