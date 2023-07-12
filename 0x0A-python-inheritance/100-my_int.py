#!/usr/bin/python3

"""defines a class MyInt"""


class MyInt(int):
    """class Myint"""

    def __eq__(self, other):
        """if it's equals"""
        if self.numerator == other.numerator:
            return int(self) != int(other)

    def __ne__(self, other):
        """not equals"""
        return int(self) == int(other)
