#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This represent a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialise the Rectangle class
        Args:
            width: Represents the width of the Rectangle.
            height: Represents the height of the Rectangle.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves height attributes"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attributes"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        return (self.__width * 2) + (self.__height * 2)
