#!/usr/bin/python3

# a function that retrieves an element from a list like in C
def element_at(my_list, idx):
    # If idx is negative, the function should return None
    # If idx is out of range (> of number of element in my_list),
    # the function should return None
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
