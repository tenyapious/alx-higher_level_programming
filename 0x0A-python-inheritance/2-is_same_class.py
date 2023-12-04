#!/usr/bin/python3

""" Defines ``is_same_class`` function """


def is_same_class(obj, a_class):
    """ Returns True if an object is exactly an instance\
            of a class otherwise False.

    Returns:
        True if object is an instance of the class otherwise false.
    """

    return type(obj) is a_class
