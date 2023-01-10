#!/usr/bin/python3

# a function that finds all multiples of 2 in a list
def divisible_by_2(my_list=[]):
    divisible_by_2 = []
    for i in my_list:
        if (i % 2) == 0:
            divisible_by_2.append(True)
        else:
            divisible_by_2.append(False)
    return divisible_by_2
