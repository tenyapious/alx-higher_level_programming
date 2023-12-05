#!/usr/bin/python3
""" Defines load_from_json_file function """
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Args:
        filename: The file containing the JSON string.

    Returns:
        The object created from ``filename``.
    """

    with open(filename, encoding="utf-8") as f:
        data = f.read()

    return json.loads(data)
