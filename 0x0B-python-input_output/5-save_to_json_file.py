#!/usr/bin/python3
"""This module defines JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """This function writes an Object to a text file, using a JSON representation"""
    return json.dump(my_obj, filename)
