#!/usr/bin/python3

"""Class Module"""

import json


class Base:

    """
    Attributes of class Base:
    _nb_objects: number of objects created
    id: id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initiation method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Update the class Base by adding the static method"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
