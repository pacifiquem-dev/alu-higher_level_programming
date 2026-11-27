#!/usr/bin/python3
"""Module that defines MyList, a list subclass with sorted printing."""


class MyList(list):
    """A list that can print itself in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
