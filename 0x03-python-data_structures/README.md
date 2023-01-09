# 0x03. Python - Data Structures: Lists, Tuples

# Tasks

## 0.Print a list of integers

* Write a function that prints all integers of a list.

	* Prototype: def print_list_integer(my_list=[]):
	* Format: one integer per line. See example
	* You are not allowed to import any module
	* You can assume that the list only contains integers
	* You are not allowed to cast integers into strings
	* You have to use str.format() to print integers
```
#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))
```
## 1. Secure access to an element in a list

* Write a function that retrieves an element from a list like in C.

	* Prototype: def element_at(my_list, idx):
	* If idx is negative, the function should return None
	* If idx is out of range (> of number of element in my_list), the function should return None
	* You are not allowed to import any module
	* You are not allowed to use try/except
```
#!/usr/bin/python3

# a function that retrieves an element from a list like in C
def element_at(my_list, idx):
    # If idx is negative, the function should return None
    # If idx is out of range (> of number of element in my_list),
    # the function should return None
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
```
## 2. Replace element

* Write a function that replaces an element of a list at a specific position (like in C).

	* Prototype: def replace_in_list(my_list, idx, element):
	* If idx is negative, the function should not modify anything, and returns the original list
	* If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
	* You are not allowed to import any module
	* You are not allowed to use try/except
```
#!/usr/bin/python3

# a function that replaces an element of a list at a specific position
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return None
    if idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
```

## 3. Print a list of integers... in reverse!

* Write a function that prints all integers of a list, in reverse order.
	* Prototype: def print_reversed_list_integer(my_list=[]):
	* Format: one integer per line. See example
	* You are not allowed to import any module
	* You can assume that the list only contains integers
	* You are not allowed to cast integers into strings
	* You have to use str.format() to print integers
```
#!/usr/bin/python3

# a function that prints all integers of a list, in reverse order.
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for i in list(reversed(my_list)):
        print("{:d}".format(i))
```

## 4. Replace in a copy

* Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

	* Prototype: def new_in_list(my_list, idx, element):
```
#!/usr/bin/python3

# a function that replaces an element in a list at a specific position
# without modifying the original list
def new_in_list(my_list, idx, element):

    # If idx is negative, the function should return a copy of the
    # original list
    # If idx is out of range (> of number of element in my_list), the function
    # should return a copy of the original list
    if idx < 0 and idx >= len(my_list):
        return my_list[:]
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
```

## 5. Can you C me now?

    * Write a function that removes all characters c and C from a string.

    * Prototype: def no_c(my_string):
    * The function should return the new string
    * You are not allowed to import any module
    * You are not allowed to use str.replace()
[Solution](https://github.com/colloso999/alx-higher_level_programming/blob/main/0x03-python-data_structures/5-no_c.py)

## 6. Lists of lists = Matrix

Write a function that prints a matrix of integers.

    * Prototype: def print_matrix_integer(matrix=[[]]):
    * Format: see example
    * You are not allowed to import any module
    * You can assume that the list only contains integers
    * You are not allowed to cast integers into strings
    * You have to use str.format() to print integers
[Solution](6-print_matrix_integer.py)
