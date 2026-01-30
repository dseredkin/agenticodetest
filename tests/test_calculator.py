"""Unit tests for the calculator module."""

import unittest

from src.calculator import add


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add_success(self) -> None:
        """Test successful addition of two numbers."""
        self.assertEqual(add(1.0, 2.0), 3.0)

    def test_add_with_none_first(self) -> None:
        """Test addition when the first input is None."""
        with self.assertRaises(ValueError):
            add(None, 1.0)

    def test_add_with_none_second(self) -> None:
        """Test addition when the second input is None."""
        with self.assertRaises(ValueError):
            add(1.0, None)

    def test_add_with_both_none(self) -> None:
        """Test addition when both inputs are None."""
        with self.assertRaises(ValueError):
            add(None, None)
