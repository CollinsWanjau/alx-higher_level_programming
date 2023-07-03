#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()
print(my_square_1.size)
print(my_square_1.area())
print(my_square_1.position)

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()
print(my_square_2.size)
print(my_square_2.area())
print(my_square_2.position)

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()
print(my_square_3.size)
print(my_square_3.area())
print(my_square_3.position)

print("--")

my_square_5 = Square(5, (3,2))
my_square_5.my_print()
print(my_square_5.size)
print(my_square_5.area())
print(my_square_5.position)

my_square_6 = Square(0, (10,3))
my_square_6.my_print()
print(my_square_6.size)
print(my_square_6.area())
print(my_square_6.position)

my_square_7 = Square(3, (1, -3))
my_square_7.my_print()
