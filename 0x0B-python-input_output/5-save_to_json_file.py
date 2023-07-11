#!/usr/bin/python3

"""defines a function save_to_json_file"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to text file using a JSON representation"""

    with open(filename, 'w', encoding="utf8") as f:
        return f.write(json.dumps(my_obj))
