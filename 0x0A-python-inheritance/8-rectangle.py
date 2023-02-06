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


