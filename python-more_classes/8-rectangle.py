#!/usr/bin/python3
"""This module defines a Rectangle class with width and height,
supports area, perimeter, comparison, and tracks instances.
"""


class Rectangle:
    """Defines a rectangle with width and height, tracks instances,
    and supports comparison.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value
