#!/usr/bin/python3

"""Define a Square class"""


class Square:
    """Represent a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square class

        Args:
            size(int): size of the square
        """

        self.__size = size
        self.__position = position
   
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
    
    @property
    def position(self):
        """Retrieve the position attribute

        Returns: The postion attribute
        """

        return(self.__position)

    @position.setter
    def position(self, value):
        """Sets value for the position attribute

        Args:
            value(tuple): Tuple for the x and y coordinates
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square

        Returns: The square area
        """

        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size > 0:
            if self.__position[1] != 0:
                for y in range(0, self.__position[1]):
                    print()
            for i in range(self.__size):
                if self.__position[0] != 0:
                    for x in range(0, self.__position[0]):
                        print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print("")
