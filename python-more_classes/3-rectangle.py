#!/usr/bin/python3
"""Rectangle sinfini təyin edir"""


class Rectangle:
    """Düzbucaqlı (Rectangle) sinfi"""

    def __init__(self, width=0, height=0):
        """Rectangle obyektini yaradır"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width dəyərini qaytarır"""
        return self.__width

    @width.setter
    def width(self, value):
        """width dəyərin
