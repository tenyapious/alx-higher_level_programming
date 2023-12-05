#!/usr/bin/python3
""" Defines from_json_string function """
import json


def from_json_string(my_str):
    """
    Decods JSON string to object.

    Args:
        my_str: The JSON string to decode.

    Returns:
        The object represented by ``my_str``.
    """

    return json.loads(my_str)
