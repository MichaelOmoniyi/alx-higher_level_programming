#!/usr/bin/python3

"""Defines a Student class"""


class Student:
    """Student class is defined"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student class

        Args:
            first_name (str): The firstname of the student
            last_name (str): The lastname of the student
            age (int): The age of the student

        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student
            Instance

        Args:
            attrs (list): (optional) List to be converted to dictionary"""

        if (isinstance(attrs, list) and all(isinstance(string, str)
                                            for string in attrs)):
            return {atr: getattr(self, atr)
                    for atr in attrs if hasattr(self, atr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance

        Args:
            json (dict): A dictionary containing attribute keys and their
            values
        """
        for atr in json:
            if (hasattr(self, atr)):
                setattr(self, atr, json[atr])
