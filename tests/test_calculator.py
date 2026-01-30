"""Unit tests for the calculator module."""

import unittest

from src.calculator import add


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add_success(self) -> None:
        """Test successful addition of two numbers."""
        assert add(1.0, 2.0) == 3.0

    def test_add_none_first(self) -> None:
        """Test addition when the first argument is None."""
        with self.assertRaises(ValueError):
            add(None, 1.0)

    def test_add_none_second(self) -> None:
        """Test addition when the second argument is None."""
        with self.assertRaises(ValueError):
            add(1.0, None)

    def test_add_none_both(self) -> None:
        """Test addition when both arguments are None."""
        with self.assertRaises(ValueError):
            add(None, None)
