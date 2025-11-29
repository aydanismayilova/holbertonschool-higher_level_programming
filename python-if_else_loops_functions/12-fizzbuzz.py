#!/usr/bin/python3
def fizzbuzz():
    """1-dən 100-ə qədər ədədləri Fizz/Buzz qaydasına görə çap edir."""
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
