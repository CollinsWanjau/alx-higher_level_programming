#!/usr/bin/python3

# a function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in list(reversed(my_list)):
        print("{:d}".format(i))
