#!/usr/bin/python3

class Rectangle:
    """A class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialise the Rectangle class"""
        self.width
        self.height

    @property
    def width(self):
        """Retrieve the width value
        Args:
            width: Represent the width of the rectangle.
            height: Represent the height of the rectagle.

        Raise:
            TypeError: Raises error if value not an integer.
            ValueError: Raises error if value less than 0.
        """
        self.__width = width
        self.__height = height

    @width.setter
    def width(self, value):
        """Sets a value for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a value for height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (__width * __height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return (__width * 2) + (__height * 2)
