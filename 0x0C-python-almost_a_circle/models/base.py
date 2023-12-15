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
        """ Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list objects to a file

        Args:
            list_objs: list objects
        """
        with open(cls.__name__ + ".json", 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string

        Args:
            json_string: the json string
        """
        if json_string is None or len(json_string) <= 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set

        Args:
            dictionary: double pointer to a dictionary
        """
        if dictionary and dictionary is not {}:
            if cls.__name__ == "Rectangle":
                inst = cls(1, 2)
            else:
                inst = cls(1)

            return inst.update(**dictionary)
