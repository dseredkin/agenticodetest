import unittest

from src.calculator import divide


class TestCalculator(unittest.TestCase):
    """Unit tests for the calculator module."""

    def test_divide_success(self) -> None:
        """Test successful division."""
        assert divide(10, 2) == 5.0
        assert divide(5, 1) == 5.0

    def test_divide_zero_denominator(self) -> None:
        """Test division by zero raises an error."""
        with self.assertRaises(ValueError):
            divide(10, 0)
