#!/usr/bin/python3

"defines an  class"


class BaseGeometry:

    "presents base geometry"

    def area(self):
        raise Exception("area() is not implemented")
