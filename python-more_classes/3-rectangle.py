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
        """width dəyərini təyin edir"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height dəyərini qaytarır"""
        return self.__height

    @height.setter
    def height(self, value):
        """height dəyərini təyin edir"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Düzbucaqlının sahəsini qaytarır"""
        return self.__width * self.__height

    def perimeter(self):
        """Düzbucaqlının perimetrini qaytarır"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Düzbucaqlını # işarəsi ilə çap edir"""
        if self.__width == 0 or self
