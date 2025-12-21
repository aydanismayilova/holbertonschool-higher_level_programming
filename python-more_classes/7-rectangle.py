#!/usr/bin/python3
"""
This module defines a Rectangle class with width, height, area, perimeter,
string representation, class-level instance counting, and customizable print symbol.
"""


class Rectangle:
    """Defines a rectangle with width and height"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width"""
        return self.__width
