#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100,
        'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        current = roman[roman_string[i]]

        if (i + 1 < length and
                current < roman[roman_string[i + 1]]):
            total -= current
        else:
            total += current

    return total
