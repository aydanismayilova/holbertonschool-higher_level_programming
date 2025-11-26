#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if not isinstance(number, int):
    print("wrong type")
elif number > 0:
    print("positive")
elif number == 0:
    print("zero")
else:
    print("negative")
