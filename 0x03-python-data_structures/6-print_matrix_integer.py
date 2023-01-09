#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i:

            # used to check if element 'j' is the last element
            # in list 'i'
            # the index method is used to find the index of j in
            # list 'i'
            # if this index is less 
            if i.index(j) < (len(i)-1):
                print("{:d}".format(j), end = " ")
            else:
                print("{:d}".format(j), end = "")
        print()

