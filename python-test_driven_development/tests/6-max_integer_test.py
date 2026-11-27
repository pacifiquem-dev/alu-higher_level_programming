#!/usr/bin/python3
"""Unit tests for max_integer."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 1, 3, 2]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_float_values(self):
        self.assertEqual(max_integer([1.1, 4.5, 2.2]), 4.5)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "c", "b"]), "c")


if __name__ == "__main__":
    unittest.main()
