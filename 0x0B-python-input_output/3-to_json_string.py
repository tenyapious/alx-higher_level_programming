#!/usr/bin/python3
import json

""" Defines to_json_string function """


def to_json_string(my_obj):
    """
    Serializes an object and returns it.

    Args:
        my_obj: The object to be serialize.

    Return:
        str: The JSON representation of ``my_obj``.
    """

    return json.dumps(my_obj)
