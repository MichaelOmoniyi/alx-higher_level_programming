#!/usr/bin/python3

"""This class is a subclass of class int"""


class MyInt(int):
    """Inverts opertors == and !="""


    def __eq__(self, value):
        """Override == operator with != operator"""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == operator"""
        return self.real == value
