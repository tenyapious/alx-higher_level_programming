#!/usr/bin/python3

""" Define a class Square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ The class Square """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} \
- {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """ Update square values

        args:
            args: list of arguments
            kwargs: list of kew-worded arguments
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Return a dictionary representation of instances of square """
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }
