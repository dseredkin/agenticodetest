import unittest

from src.calculator import divide


class TestCalculator(unittest.TestCase):
    """Unit tests for the calculator module."""

    def test_divide_normal(self) -> None:
        """Test division with valid inputs."""
        self.assertEqual(divide(10.0, 2.0), 5.0)

    def test_divide_by_zero(self) -> None:
        """Test division by zero raises an error."""
        with self.assertRaises(ValueError):
            divide(10.0, 0)
