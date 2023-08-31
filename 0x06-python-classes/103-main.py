#!/usr/bin/python3

MagicClass = __import__('103-magic_class').MagicClass

circle1 = MagicClass(7)
circle2 = MagicClass(5)
decimal_places = 3

print("circle1 area with radius {}: {:.{}f}".format(circle1.radius, circle1.area(), decimal_places))
print("circle2 area with radius {}: {:.{}f}".format(circle2.radius, circle2.area(), decimal_places))
print("circle1 circumference: {:.{}f}".format(circle1.circumference(), decimal_places))
print("circle2 circumference: {:.{}f}".format(circle2.circumference(), decimal_places))
