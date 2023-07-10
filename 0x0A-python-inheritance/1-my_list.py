#!/usr/bin/python3

"Defines subclass MyList"


class MyList(list):

    "MyList class"

    def print_sorted(self):
        print("{}".format(sorted(self)))
