#!/usr/bin/python3

# a function that deletes the item at a specific position in a list
def delete_at(my_list=[], idx=0):

    # This function checks whether the index is within the valid 
    # range (between 0 and the length of the list minus 1), and 
    # if it is not, it returns the original list without making 
    # any changes. 
    if not (0 <= idx < len(my_list)):
        return my_list
    my_list.remove(my_list[idx])
    return my_list
