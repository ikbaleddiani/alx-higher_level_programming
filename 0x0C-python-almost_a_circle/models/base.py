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

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""

        j_str = '[]'
        j_list = []
        if list_objs is not None:
            for i in list_objs:
                j_list.append(i.to_dictionary())
            if len(j_list) > 0:
                j_str = Base.to_json_string(j_list)
        with open(cls.__name__ + '.json', 'w') as n:
            n.write(j_str)

