#!/usr/bin/python3

"""This is a subclass of the Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This a class called Square"""

    def __init__(self, size):
        """This initializes the subclass Rectangle"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
