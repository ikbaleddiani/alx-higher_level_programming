#!/usr/bin/python3

"rectangle module"


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    "class Rectangle"

    def __init__(self, width, height):

        "initialisation an rectangle"

        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
