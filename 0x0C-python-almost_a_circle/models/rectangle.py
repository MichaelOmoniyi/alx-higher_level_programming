#!/usr/bin/python3

"""This class is a subclass of the base class, i.e. inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """This class defines a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """This module initializes the class
        Args:
            width: This represents the rectangle width
            height: This represents the rectangle height
            x: This represents the x-coordinate of the rectangle's
            upper-left corner (defaulted to 0).
            y: This represents the y-coordinate of the rectangle's
            upper-left corner (defaulted to 0)
            id: This represents the class id.
        Raises:
            TypeError: if argument is not an integer
            ValueError: if argument is less than 0

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @property
    def height(self):
        """retrieves the height attribute"""
        return self.__height

    @property
    def x(self):
        """Retrieves the x attribute"""
        return self.__x

    @property
    def y(self):
        """Retrieves the y attribute"""
        return self.__y

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x attribute"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y attribute"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """The method return the rectangle area"""
        return self.__width * self.__height

    def display(self):
        """This displays the rectangle using '#'"""
        for y in range(self.y):
            print("")
        for column in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for row in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Defines string representation format for the Rectangle"""
        return f"[Rectagnle] ({self.id}) {self.x}/{self.y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """This assigns an argument and key/value argument to  attributes"""
        
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
