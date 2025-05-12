#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) >= 1:
        a0 = tuple_a[0]
    else:
        a0 = 0
    if len(tuple_a) >= 2:
        a1 = tuple_a[1]
    else:
        a1 = 0
    if len(tuple_b) >= 1:
        b0 = tuple_b[0]
    else:
        b0 = 0
    if len(tuple_b) >= 2:
        b1 = tuple_b[1]
    else:
        b1 = 0
    sum0 = a0 + b0
    sum1 = a1 + b1
    return (sum0, sum1)
