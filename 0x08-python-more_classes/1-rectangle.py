#!usr/bin/python3

"""A class that defines a Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle class
        Args:
            width: Represent the width of the Rectangle.
            height: Represent the height of the Rectangle.

        Raises:
            TypeError: if value not an integer.
            ValueError: if value less than 0.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """retrieves width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attributes"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
