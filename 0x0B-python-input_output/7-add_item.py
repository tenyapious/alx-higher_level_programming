#!/usr/bin/python3
""" Define add_item function """
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    args = sys.argv

    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        save_to_json_file([], "add_item.json")
        my_list = []

    for idx, arg in enumerate(args):
        if idx > 0:
            my_list.append(arg)

    save_to_json_file(my_list, "add_item.json")
