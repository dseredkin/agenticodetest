"""Tests for the calculator module."""

import unittest

from src.calculator import add


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add_success(self) -> None:
        """Test adding two valid numbers."""
        result = add(2.0, 3.0)
        self.assertEqual(result, 5.0)

    def test_add_with_none_first(self) -> None:
        """Test adding when the first argument is None."""
        with self.assertRaises(ValueError):
            add(None, 3.0)

    def test_add_with_none_second(self) -> None:
        """Test adding when the second argument is None."""
        with self.assertRaises(ValueError):
            add(2.0, None)

    def test_add_with_both_none(self) -> None:
        """Test adding when both arguments are None."""
        with self.assertRaises(ValueError):
            add(None, None)
