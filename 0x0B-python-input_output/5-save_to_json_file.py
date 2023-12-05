#!/usr/bin/python3
""" Defines save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    """
    Write the JSON representation of an object to a file.

    Args:
        my_obj: The object.
        filename: The file to write the JSON string to.
    """

    with open(filename, 'w', encoding="utf-8") as f:

        f.write(json.dumps(my_obj))
