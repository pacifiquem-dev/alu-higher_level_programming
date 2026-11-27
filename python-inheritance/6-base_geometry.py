#!/usr/bin/python3
"""Module that defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
