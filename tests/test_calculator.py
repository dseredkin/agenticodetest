import unittest

from src.calculator import add


class TestCalculator(unittest.TestCase):
    """Unit tests for the calculator module."""

    def test_add_success(self) -> None:
        """Test successful addition of two numbers."""
        result = add(2.0, 3.0)
        self.assertEqual(result, 5.0)

    def test_add_with_none(self) -> None:
        """Test that adding with None raises ValueError."""
        with self.assertRaises(ValueError):
            add(None, 3.0)
        with self.assertRaises(ValueError):
            add(2.0, None)
        with self.assertRaises(ValueError):
            add(None, None)
