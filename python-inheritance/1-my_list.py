#!/usr/bin/python3
"""
Module that defines a MyList class inheriting from list.
"""


class MyList(list):
    """
    MyList class that extends the built-in list.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order
        without modifying the original list.
        """
        print(sorted(self))
