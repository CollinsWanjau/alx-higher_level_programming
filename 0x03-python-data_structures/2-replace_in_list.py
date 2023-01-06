#!/usr/bin/python3

# a function that replaces an element of a list at a specific position
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
