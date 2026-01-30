"""Unit tests for the calculator module."""

import unittest

from src.calculator import add


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_add_success(self) -> None:
        """Test successful addition of two numbers."""
        result = add(2, 3)
        self.assertEqual(result, 5)

    def test_add_with_none_first(self) -> None:
        """Test addition when the first input is None."""
        with self.assertRaises(ValueError):
            add(None, 3)

    def test_add_with_none_second(self) -> None:
        """Test addition when the second input is None."""
        with self.assertRaises(ValueError):
            add(2, None)

    def test_add_with_non_number_first(self) -> None:
        """Test addition when the first input is not a number."""
        with self.assertRaises(ValueError):
            add("a", 3)

    def test_add_with_non_number_second(self) -> None:
        """Test addition when the second input is not a number."""
        with self.assertRaises(ValueError):
            add(2, "b")


if __name__ == "__main__":
    unittest.main()
