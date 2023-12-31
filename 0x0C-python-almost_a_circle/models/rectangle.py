#!/usr/bin/python3

""" Defines the class Rectangle """
from models.base import Base


class Rectangle(Base):
    """ The class Rectangle

    Args:
        width: Width of the rectangle.
        height: Height of the rectangle.
        x: X cordinate of the rectangle.
        y: Y cordinate of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """ Return the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Return the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Return the x cordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Return the y cordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Print the Rectangle instance with the character '#' """
        for i in range(self.y):
            print()
        for i in range(self.height):
            for k in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print('#', end='')
            print()

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} \
- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """ Update the values of the rectangle """
        if args:
            if len(args) >= 5:
                self.y = args[4]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 1:
                self.id = args[0]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Return the dictionary representation of the rectangle """
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "height": self.height,
                "width": self.width
                }
