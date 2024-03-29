#!/usr/bin/python3

"""rectrangle class models"""

from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instance initialization"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return self.__width

    @width.setter
    def width(self, width):
        """width setter method"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter method"""
        return self.__height

    @height.setter
    def height(self, height):
        """height setter method"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter method"""
        return self.__x

    @x.setter
    def x(self, x):
        """x setter method"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter method"""
        return self.__y

    @y.setter
    def y(self, y):
        """y setter method"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """return an area of reactangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle to stdout using"""

        for row in range(self.y):
            print()
        for row in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        """update: returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        return "[{}] ({}) {}/{} - {}/{}".format(self.__class__.__name__,
                                                self.id, self.__x,
                                                self.__y,
                                                self.__width, self.__height
                                                )

    def update(self, *args, **kwargs):
        """update attributes"""
        lists = ['id', 'width', 'height', 'x', 'y']
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
        """rectangle dictionary"""

        ob = {}
        for i in ['id', 'width', 'height', 'x', 'y']:
            ob[i] = getattr(self, i)
        return ob
