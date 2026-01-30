"""Tests for the calculator module."""

import unittest

from src.calculator import divide


class TestCalculator(unittest.TestCase):
    """Unit tests for calculator functions."""

    def test_divide_success(self) -> None:
        """Test successful division."""
        assert divide(10.0, 2.0) == 5.0
        assert divide(15.0, 3.0) == 5.0

    def test_divide_by_zero(self) -> None:
        """Test division by zero raises an error."""
        with self.assertRaises(ValueError):
            divide(10.0, 0)


if __name__ == "__main__":
    unittest.main()
