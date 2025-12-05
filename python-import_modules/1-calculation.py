#!/usr/bin/python3
import calculator_1


def main(a, b):
    """Perform all calculations with a and b and print results"""
    print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))


if __name__ == "__main__":
    a = 10
    b = 5
    main(a, b)
