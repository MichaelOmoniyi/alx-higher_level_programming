#!/usr/bin/python3

""" This class defines a rectangle"""


class Rectangle:
    """ This is a class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ This initializes the Rectangle class
        Args:
        width: This represents the Rectangle width.
        height: This represents the Rectangle height.

        Error:
        TypeError: if value is not an integer.
        ValueError: if value is less than zero.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ This retrieves the rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ This sets the rectangle width to a particular value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This retrieves the rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ This sets the rectangle height to a particular value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """ This returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
            return (perimeter)
        perimeter = (2 * self.__width) + (2 * self.__height)
        return perimeter

    def __str__(self) -> str:
        """ This diagramatically shows a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                try:
                    rectangle += str(self.print_symbol)
                except Exception:
                    rectangle += type(self).print_symbol
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the Rectangle with bigger area

        Args:
            rect_1 (Rectangle): An instance of Rectangle
            rect_2 (Rectangle): An instance of Rectangle

        Raises:
            TypeError: If either of rect_1 or rect_2
            is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
