#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([4, 2, 1, 3]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 3, 1]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 5, 3, -2]), 5)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 3.2, 2.1]), 3.2)

    def test_strings(self):
        self.assertEqual(max_integer("abcde"), 'e')

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none_argument(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_not_iterable(self):
        with self.assertRaises(TypeError):
            max_integer(123)
if __name__ == "__main__":
    unittest.main()
