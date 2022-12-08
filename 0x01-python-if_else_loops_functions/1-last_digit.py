#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = random.randint(0, 6)
if (lastDigit > 5):
    print(f"Last digit of {number} is {lastDigit} and greater than 5")
elif (lastDigit == 0):
    print(f"Last digit of {number} is {lastDigit} and is 0")
else:
    print(f"Last digit of {number} is {lastDigit} and is less than 6 \
        / and not 0")
