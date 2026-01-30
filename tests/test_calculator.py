"""Unit tests for the calculator module."""

import unittest

from src.calculator import divide


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_divide_positive_numbers(self) -> None:
        """Test division with positive numbers."""
        result = divide(10.0, 2.0)
        self.assertEqual(result, 5.0)

    def test_divide_negative_numbers(self) -> None:
        """Test division with negative numbers."""
        result = divide(-10.0, 2.0)
        self.assertEqual(result, -5.0)

    def test_divide_by_zero(self) -> None:
        """Test division by zero raises an error."""
        with self.assertRaises(ValueError):
            divide(10.0, 0)

    def test_divide_zero_by_number(self) -> None:
        """Test dividing zero by a number."""
        result = divide(0.0, 5.0)
        self.assertEqual(result, 0.0)
