#!/usr/bin/python3
"""This module defines a class Square that represents a square."""


class Square:
    """A class that defines a square by its private size attribute."""

    def __init__(self, size):
        """Initialize a new Square with the given size.

        Args:
            size: the size of the square, stored as a private attribute.
        """
        self.__size = size
