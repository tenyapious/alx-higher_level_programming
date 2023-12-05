#!/usr/bin/python3
""" Defines class_to_json function """


def class_to_json(obj):
    """ Returns the dictionary discription of an obj """

    return obj.__dict__
