"""Unit tests for the calculator module."""

import unittest

from src.calculator import add


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add_valid_numbers(self) -> None:
        """Test adding two valid numbers."""
        assert add(2.0, 3.0) == 5.0

    def test_add_with_none_a(self) -> None:
        """Test adding when a is None."""
        with self.assertRaises(ValueError):
            add(None, 3.0)

    def test_add_with_none_b(self) -> None:
        """Test adding when b is None."""
        with self.assertRaises(ValueError):
            add(2.0, None)

    def test_add_with_none_both(self) -> None:
        """Test adding when both are None."""
        with self.assertRaises(ValueError):
            add(None, None)


if __name__ == "__main__":
    unittest.main()
