#!/usr/bin/python3
"""This defines the Square class which inherits
    from the Rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This defines the square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """This initializes the Square class

        Args:
            size (int): The height or width of
                the Square
            x (int): The x-coordinate of the square
            y (int): The y-coordinate of the square
            id (id): The square Unique id
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the size of the square"""

        return self.width

    @size.setter
    def size(self, value):
        """Assign new value to size attribute"""

        self.width = value
        self.height = value

    def __str__(self):
        """Defines the string representation of the Square class"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """This assign key/value arguments to attributes

        Args:
            *args (ints):New attribute values
                - 1st argument represents id attribute
                - 2nd argument represents size attribute
                - 3rd argument represents x attribute
                - 4th argument represents y attribute
            **kwargs (dict): Key/value pair of attributes"""

        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        if kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Square"""

        return ({
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
                )
