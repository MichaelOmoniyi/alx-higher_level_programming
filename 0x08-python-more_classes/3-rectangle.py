#!/usr/bin/python

""" This class defines a rectangle"""


class Rectangle:
    """ This is a class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """ This initializes the Rectangle class
        Args:
        width: This represents the Rectangle width.
        height: This represents the Rectangle height.

        Error:
        TypeError: if value is not an integer.
        ValueError: if value is less than zero.
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ This retrieves the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ This sets the rectangle width to a particular value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This retrieves the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ This sets the rectangle height to a particular value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ This returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return (perimeter)
        perimeter = (2 * self.__width) + (2 * self.__height)
        return perimeter

    def __str__(self) -> str:
        """Presents a rectangle like diagram"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.height):
            for row in range(self.width):
                rectangle += "#"
            if column < self.height - 1:
                rectangle += "\n"
        return (rectangle)
