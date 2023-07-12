#!/usr/bin/python3

"rectangle module"


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "class of square"

    def __init__(self, size):
        "initialisation of squere"

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""

        return self.__size ** 2

    def __str__(self):
        """return string"""

        return "[Square] {}/{}".format(self.__size, self.__size)
