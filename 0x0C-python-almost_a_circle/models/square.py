#!/usr/bin/python3

"""square class models"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ method inistialization"""

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """update: returns [Square] (<id>) <x>/<y> - <size>"""

        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size of square"""
        return self.height

    @size.setter
    def size(self, size):
        """size of square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updating attributes"""

        lists = ['id', 'size', 'x', 'y']
        if args:
            i = 0
            for arg in args:
                setattr(self, lists[i], arg)
                i = i + 1
        else:
            for key in kwargs:
                if key in lists:
                    self.__setattr__(key, kwargs[key])

    def to_dictionary(self):
        """dictionary of Square"""

        ob = {}
        for i in ['id', 'size', 'x', 'y']:
            ob[i] = getattr(self, i)
        return ob
