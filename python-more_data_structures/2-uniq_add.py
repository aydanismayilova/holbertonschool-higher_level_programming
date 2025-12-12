#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in my_list:
        if my_list.count(i) == 1 or i not in my_list[:my_list.index(i)]:
            total += i
    return total
