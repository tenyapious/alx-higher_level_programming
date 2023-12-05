#!/usr/bin/python3
""" Defines Student class """


class Student:
    """
    Student class

    Args:
        first_name: First name of student.
        last_name: Last name of student.
        age: Age of student.

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns the dictionary discription of instances

        Args:
            attrs: Attribute to look for.

        Returns:
            The whole instance dictionary or the specified values.
        """

        if attrs is None:
            return self.__dict__
        else:
            attr_dict = {}

            for attr in attrs:
                if attr in self.__dict__:
                    attr_dict[attr] = self.__dict__[attr]
            return attr_dict

    def reload_from_json(self, json):
        """ Rebuild an object based on a JSON representation

        Args:
            json: The JSON representation.
        """

        for key in json:
            if key in self.__dict__:
                setattr(self, key, json[key])
