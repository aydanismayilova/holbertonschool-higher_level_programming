#!/usr/bin/python3
"""Define a Square class with a private instance attribute 'size'"""


class Square:
    """Represents a square"""

    def __init__(self, size):
        """Initialize a new Square instance with a private size"""
        self.__size = size
