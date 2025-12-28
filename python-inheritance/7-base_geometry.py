#!/usr/bin/python3
"""
Module that defines a BaseGeometry class with area and integer_validator methods.
"""


class BaseGeometry:
    """BaseGeometry class with area method and integer validation."""

    def area(self):
        """Raises an Exception indicating the method is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.
        Raises TypeError or ValueError with appropriate messages.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
