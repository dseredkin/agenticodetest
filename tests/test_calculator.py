"""Unit tests for the calculator module."""

import unittest

from src.calculator import divide


class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""

    def test_divide(self) -> None:
        """Test the divide function."""
        assert divide(10.0, 2.0) == 5.0
        assert divide(15.0, 3.0) == 5.0
        with self.assertRaises(ValueError):
            divide(10.0, 0)
