#!/usr/bin/python3

"""This class will be the base class for other projects in this directory"""


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
