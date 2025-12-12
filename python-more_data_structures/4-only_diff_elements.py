#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = set()
    for element in set_1:
        if not element in set_2:
            result.add(element)
    for element in set_2:
        if not element in set_1:
            result.add(element)
    return result
