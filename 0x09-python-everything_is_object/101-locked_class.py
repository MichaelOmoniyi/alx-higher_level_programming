#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    Prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """

    __slot__ = ["first_name"]
