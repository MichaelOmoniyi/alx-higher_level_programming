#!/usr/bin/python3
"""This module defines JSON representation"""
import json


def to_json_string(my_obj):
    """This function returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
