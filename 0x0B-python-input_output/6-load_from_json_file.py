#!/usr/bin/python3
"""This module defines JSON representation"""
import json


def to_json_string(my_obj):
    """This function that creates an Object from a “JSON file”"""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
