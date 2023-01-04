#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lnum = abs(number) % 10

if number < 0:
    number = (number)
    lnum = -(lnum)

if lnum > 5:
    string = "and is greater than 5"
elif lnum < 6 and lnum != 0:
    string = "and is less than 6 and not 0"
else:
    string = "and is 0"

print(f"Last digit of {number} is {lnum} {string}")
