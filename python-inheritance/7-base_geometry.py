#!/usr/bin/python3
"""Module that defines BaseGeometry with an integer validator."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0.

        Raises TypeError if value is not an integer and ValueError
        if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
