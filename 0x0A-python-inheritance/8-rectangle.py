#!/usr/bin/python3

"BaseGeometry module"


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    "class Rectangle"

    def __init__(self, width, height):
        self.__height = height
        self.integer_validator("height", height)
        self.__width = width
        self.integer_validator("width", width)
