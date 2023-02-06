#!/usr/bin/python3

"""This is a subclass of the BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This a class called Rectangle"""

    def __init__(self, width, height):
        """This initializes the subclass Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the Rectangle area"""
        return (self.__width * self.__height)

    def __str__(self) -> str:
        """Return a description of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
