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

    def to_json(self):
        """ Returns the dictionary discription of instances """

        return self.__dict__
