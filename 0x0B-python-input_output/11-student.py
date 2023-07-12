#!/usr/bin/python3

"""student to json"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """Initalizes a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a json representatiion of the object"""

        if attrs is None:
            return self.__dict__

        else:
            jsn_dic = {}
            for ite in attrs:
                for k in self.__dict__:
                    if k == ite:
                        jsn_dic[k] = self.__dict__[k]
            return jsn_dic

    def reload_from_json(self, json):
        """"reload from json"""

        self.__dict__.update(json)
