#!/usr/bin/python3
"""This module defines a class Rectangle that represents a rectangle."""


class Rectangle:
    """A class that defines a rectangle by its width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with an optional width and height.

        Args:
            width: the width of the rectangle, an integer >= 0.
            height: the height of the rectangle, an integer >= 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle after validating the value.

        Args:
            value: the new width, which must be an integer >= 0.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle after validating the value.

        Args:
            value: the new height, which must be an integer >= 0.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle.

        The perimeter is 0 if the width or the height is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the rectangle drawn with the # character.

        An empty string is returned if the width or the height
        is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        row = "#" * self.__width
        return "\n".join([row] * self.__height)
