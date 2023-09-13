#!/usr/bin/python3

"""Defines a Student class"""


class Student:
    """Student class is defined"""

    def __init__(self, first_name, last_name, age):
        """Initializes the Student class

        Args:
            first_name (str): The student first name
            last_name (str): The student last name
            age (int): The student age
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student
            Instance"""

        return (self.__dict__)
