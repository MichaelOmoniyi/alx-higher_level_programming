#!/usr/bin/python3

"""This module will be the base class for other projects in this directory"""


import json
import turtle


class Base:
    """The Base class helps manage id attribute in  future classes and
    to avoid duplicating the same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """This method check if id value is None, then increments __nb_objects
        by 1. If id value is not None, it assigns the argument value to it.
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation string representation of
            list_dictionaries"""

        if list_dictionaries is None:
            return (str([]))
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances who inherits of Base
        """

        filename = cls.__name__ + ".json"
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""

        if json_string is None:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns a new instance with all attributes already set

        Args:
            dictionary (dict): Key/value pairs of attributes
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_instance = cls(2, 2)
            else:
                new_instance = cls(2)
            new_instance.update(**dictionary)

            return (new_instance)

    @classmethod
    def load_from_file(cls):
        """Returns list of instantiated classes"""

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as file:
                list_dicts = Base.from_json_string(file.read())
                return [cls.create(**dicts) for dicts in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV seriailization of a list of objecst to a file

        Args:
            list_objs (list): A list of instances inherited from Base
        """

        filename = str(cls.__name__) + ".csv"
        with open(filename, "w") as fileCsv:
            if list_objs is None:
                fileCsv.write("[]")
            else:
                obj_dict = [obj.to_dictionary() for obj in list_objs]
                fileCsv.write(Base.to_json_string(obj_dict))

    @classmethod
    def load_from_file_csv(cls):
        """Reads the CSV deserialization of a list of objects from a file

        Returns:
            A list of instances inherited from the Base class
        """

        filename = str(cls.__name__) + ".csv"
        try:
            with open(filename, "r") as fileCsv:
                obj_dicts = Base.from_json_string(fileCsv.read())
                return ([cls.create(**objs) for objs in obj_dicts])
        except IOError:
            return ([])

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the rectangles and squares

        Args:
            list_rectangle (list): A list of the rectangle instances
            list_squares (list): A list of the square instances
        """

        tl = turtle.Turtle()
        tl.screen.bgcolor("#0000ff")
        tl.pensize(4)
        tl.shape("turtle")

        tl.color("#ffffff")
        for rectangle in list_rectangles:
            tl.showturtle()
            tl.up()
            tl.goto(rectangle.x, rectangle.y)
            tl.down()

            for i in range(2):
                tl.forward(rectangle.width)
                tl.left(90)
                tl.forward(rectangle.height)
                tl.left(90)
            tl.hideturtle()
            tl._delay(25)

        tl.color("#ffa500")
        for square in list_squares:
            tl.showturtle()
            tl.up()
            tl.goto(square.x, square.y)
            tl.down()

            for i in range(2):
                tl.forward(square.width)
                tl.left(90)
                tl.forward(square.height)
                tl.left(90)
            tl.hideturtle()
            tl._delay(25)

        turtle.exitonclick()
