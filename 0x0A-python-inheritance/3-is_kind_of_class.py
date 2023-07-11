#!/usr/bin/python3

"defines a function"


def is_kind_of_class(obj, a_class):

    "returns True if the object is an instance of"

    if type(obj) == a_class or isinstance(obj, a_class) is True:
        return True
    return False
