#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        # initialize a variable to the first element of the input
        biggest = my_list[0]

        # iterate through the list and check each element to see
        # if it is larger
        # than the current value of biggest
        for i in range(1, len(my_list)):
            if my_list[i] > biggest:
                biggest = my_list[i]
        return biggest
