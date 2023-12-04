#!/usr/bin/python3

""" Defines ``is_kind_of_class`` function """


def is_kind_of_class(obj, a_class):
    """ Returns True if an object is an instance of\
            a direct or inherited class otherwise False.

    Returns:
        True if ``obj`` is a instance of ``a_class`` otherwise False.
    """

    return isinstance(obj, a_class)
