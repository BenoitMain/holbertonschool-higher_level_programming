#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_value = set(my_list)
    total = 0
    for value in uniq_value:
        total += value
    return total
