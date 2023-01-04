#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > -10 or number < 10:
    print(f"{number}")
elif number > -100 or number > 100:
    print(f"{number % 10}")
elif number > -1000 or number > 100:
    print(f"{(number % 100) % 10}")
elif number > -10000 or number > 10000:
    print(f"{((number % 1000) % 100) % 10}")
elif number == -10000 or number == 10000:
    print(f"{(((number % 10000) % 1000) % 100) % 10}")
