#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_list(self):
        """Test with regular ordered list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_descending_order(self):
        """Test with descending ordered list"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_all_negative(self):
        """Test with all negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_negative_positive(self):
        """Test with mixed negative and positive numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_single_element(self):
        """Test with single element list"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))

    def test_duplicate_max(self):
        """Test with duplicate maximum values"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

    def test_large_numbers(self):
        """Test with large numbers"""
        self.assertEqual(max_integer([1000, 2000, 3000]), 3000)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

    def test_mixed_int_float(self):
        """Test with mixed integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.2]), 4.2)

    def test_beginning_max(self):
        """Test with maximum at beginning"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_middle_max(self):
        """Test with maximum in middle"""
        self.assertEqual(max_integer([1, 2, 10, 4, 5]), 10)

    def test_end_max(self):
        """Test with maximum at end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_zero_in_list(self):
        """Test with zero in the list"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_single_negative(self):
        """Test with single negative number"""
        self.assertEqual(max_integer([-5]), -5)

    def test_very_large_list(self):
        """Test with a large list"""
        large_list = list(range(1000))
        self.assertEqual(max_integer(large_list), 999)


if __name__ == '__main__':
    unittest.main()
