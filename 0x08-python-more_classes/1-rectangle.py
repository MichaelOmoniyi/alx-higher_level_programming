#!usr/bin/python3

"""A class that defines a Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle class

        Args:
            width: Represent the width of the Rectangle.
            height: Represent the height of the Rectangle.

        Raises:
            TypeError: Raises error if value not an integer.
            ValueError: Raises error if value less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
