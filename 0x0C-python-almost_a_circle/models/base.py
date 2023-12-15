#!/usr/bin/python3

""" Defines a class Base """
import json


class Base:
    """ The Base class

    Args:
        id (int): object id

    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"

        return json.dumps(list_dictionaries)
