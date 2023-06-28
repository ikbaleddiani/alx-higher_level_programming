#!/usr/bin/python3

"Defines a Square class."


class Square:

    "Initializes a square with attriute size"
    
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
