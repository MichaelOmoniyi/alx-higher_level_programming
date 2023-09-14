#!/usr/bin/python3

""" This is class calculates basic geometry"""


class BaseGeometry:
    """ This class return values for basic geometry"""

    def area(self):
        """ Raises an Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ This validate value and returns an error if value is not validated

        Args:
            name (str): Attribute name
            value (int): Attribute value

        Errors:
            TypeError: if value is not an integer
            ValueError: if value is less than zero
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
