#!/usr/bin/python3

import math
"""Defines a class called MagicClass"""


class MagicClass:
    """The MagicClass class"""

    def __init__(self, radius=0):
        """Initializes the MagicClass class

        Args:
            radius (int or float): An attribute
        """

        if isinstance(radius, int) or isinstance(radius,float):
            self.__radius = radius
        else:
            raise TypeError("radius must be a number")

    @property
    def radius(self):
        """Retreives the radius attribute"""
        return(self.__radius)
    
    def area(self):
        """Returns area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns circuference"""
        return (2 * math.pi * self.__radius)
