#!/usr/bin/python3

"defines a function"


def inherits_from(obj, a_class):

    """returns True if the object is an instance of a class
    that inherited or false otherwise"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
