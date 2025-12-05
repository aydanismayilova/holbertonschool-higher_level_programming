#!/usr/bin/python3
from add_0 import add


def fake_add(a, b):
    """FAKE add function: performs subtraction instead of addition"""
    return a - b


if __name__ == "__main__":
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, fake_add(a, b)))
