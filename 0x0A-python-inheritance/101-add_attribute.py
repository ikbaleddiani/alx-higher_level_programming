#!/usr/bin/python3

"""add attribute"""


def add_attribute(obj, add_att, ad_value):
    """Adds an attribute to obj"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, add_att, ad_value)
