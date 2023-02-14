#!/usr/bin/python3

"""This class is a subclass of the base class, i.e. inherits from Base"""


class Rectangle(Base):
    """This class defines a Rectangle"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """This module initializes the class
        Args:
            width: This represents the rectangle width
            height: This represents the rectangle height
            x:
            y: 
            id:
        Raises:
            TypeError: if argument is not an integer
            ValueError: if argument is less than 0

        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
