#!/usr/bin/python3

""" Defines the ``inherits_from`` function """


def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of a class that
        inherited (directly or indirectly) from the specified class.

        Args:
            obj: the object to check it class
            a_class: the class to check against the ``obj`` class

        Return:
            Bool: True if ``obj`` is an instance of a class that inherited
                (directly or indirectly from ``a_class`` otherwise False
    """

    if obj.__class__.__name__ != a_class.__name__:
        return issubclass(obj.__class__, a_class)
