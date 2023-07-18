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

        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                            self.id, self.x,
                                            self.y, self.width))
