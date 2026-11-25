#!/usr/bin/python3
"""This module defines a class Square that represents a square."""


class Square:
    """A class that defines a square by its private size attribute."""

    def __init__(self, size=0):
        """Initialize a new Square with an optional size.

        Args:
            size: the size of the square, which must be an integer
                greater than or equal to 0 (defaults to 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square, which is size squared."""
        return self.__size ** 2
