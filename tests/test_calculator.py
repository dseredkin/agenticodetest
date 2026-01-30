import unittest

from src.calculator import add


class TestCalculator(unittest.TestCase):
    def test_add_normal(self) -> None:
        """Test adding two valid numbers."""
        assert add(1, 2) == 3  # Integer addition
        assert add(1.5, 2.5) == 4.0  # Float addition

    def test_add_with_none(self) -> None:
        """Test adding with None values."""
        with self.assertRaises(ValueError):
            add(None, 1)
        with self.assertRaises(ValueError):
            add(1, None)
        with self.assertRaises(ValueError):
            add(None, None)
