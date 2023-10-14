#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, w, h, x_co=0, y_co=0, identity=None):
        """Initialize a new Rectangle.

        Args:
            w (int): The w of the new Rectangle.
            h (int): The h of the new Rectangle.
            x_co (int): The x coordinate of the new Rectangle.
            y_co (int): The y coordinate of the new Rectangle.
            identity (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of w or h is not an int.
            ValueError: If either of w or h <= 0.
            TypeError: If either of x_co or y_co is not an int.
            ValueError: If either of x_co or y_co < 0.
        """
        if not isinstance(w, int):
            raise TypeError("w must be an integer")
        if w <= 0:
            raise ValueError("w must be > 0")
        if not isinstance(h, int):
            raise TypeError("h must be an integer")
        if h <= 0:
            raise ValueError("h must be > 0")
        if not isinstance(x_co, int):
            raise TypeError("x_co must be an integer")
        if x_co < 0:
            raise ValueError("x_co must be >= 0")
        if not isinstance(y_co, int):
            raise TypeError("y_co must be an integer")
        if y_co < 0:
            raise ValueError("y_co must be >= 0")

        self.w = w
        self.h = h
        self.x_co = x_co
        self.y_co = y_co
        super().__init__(identity)

    @property
    def w(self):
        """Set/get the w of the Rectangle."""
        return self.__w

    @w.setter
    def w(self, value):
        if not isinstance(value, int):
            raise TypeError("w must be an integer")
        if value <= 0:
            raise ValueError("w must be > 0")
        self.__w = value

    @property
    def h(self):
        """Set/get the h of the Rectangle."""
        return self.__h

    @h.setter
    def h(self, value):
        if not isinstance(value, int):
            raise TypeError("h must be an integer")
        if value <= 0:
            raise ValueError("h must be > 0")
        self.__h = value

    @property
    def x_co(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x_co

    @x_co.setter
    def x_co(self, value):
        if not isinstance(value, int):
            raise TypeError("x_co must be an integer")
        if value < 0:
            raise ValueError("x_co must be >= 0")
        self.__x_co = value

    @property
    def y_co(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y_co

    @y_co.setter
    def y_co(self, value):
        if not isinstance(value, int):
            raise TypeError("y_co must be an integer")
        if value < 0:
            raise ValueError("y_co must be >= 0")
        self.__y_co = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.w * self.h

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.w == 0 or self.h == 0:
            print("")
            return

        [print("") for y in range(self.y_co)]
        for h in range(self.h):
            [print(" ", end="") for x in range(self.x_co)]
            [print("#", end="") for w in range(self.w)]
            print("")

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                self.x_co, self.y_co,
                                                self.w, self.h)

    def update(self, *args, **kwargs):
        """Update the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents w attribute
                - 3rd argument represents h attribute
                - 4th argument represents x_co attribute
                - 5th argument represents y_co attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.w, self.h, self.x_co, self.y_co)
                    else:
                        self.id = arg
                elif a == 1:
                    self.w = arg
                elif a == 2:
                    self.h = arg
                elif a == 3:
                    self.x_co = arg
                elif a == 4:
                    self.y_co = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.w, self.h, self.x_co, self.y_co)
                    else:
                        self.id = v
                elif k == "w":
                    self.w = v
                elif k == "h":
                    self.h = v
                elif k == "x_co":
                    self.x_co = v
                elif k == "y_co":
                    self.y_co = v
