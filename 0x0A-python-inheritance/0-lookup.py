#!/usr/bin/python3

""" Defines a function lookup """


def lookup(obj):
    """ lookups the attributes and methods of available to objects

    Args:
        obj: the object to lookup

    Return:
        list: Available attributes and methods

    """

    return dir(obj)
