#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    # Use default values if the tuples are smaller than 2 elements
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    result = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return result
