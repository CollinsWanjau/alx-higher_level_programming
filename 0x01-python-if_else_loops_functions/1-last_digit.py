#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = 0

if (lastDigit >= 0):
    lastDigit = number % 10
else:
    lastDigit = (-number % 10) * -1

message = f"Last digit of {number} is {lastDigit}"

if lastDigit > 5 and lastDigit % 10 != 0:
    print(f"{message} and greater than 5")
elif lastDigit == 0:
    print(f"{message} and is 0")
else:
    print(f"{message} and is less than 6 and not 0")
