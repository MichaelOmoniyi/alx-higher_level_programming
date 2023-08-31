#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """Represent a square class"""

    def __init__(self, size=0):
        """Initializes a square class

        Args:
            size(int): size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retrieve the size attribute

        Returns: The size attribute
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """Sets value for the square size

        Args:
            value(int): The square size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square

        Returns: The square area
        """

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size > 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print("")
