import unittest

from src.calculator import add


class TestCalculator(unittest.TestCase):
    def test_add_valid_numbers(self) -> None:
        """Test adding two valid numbers."""
        assert add(1.0, 2.0) == 3.0

    def test_add_with_none_first(self) -> None:
        """Test adding when the first argument is None."""
        with self.assertRaises(ValueError):
            add(None, 1.0)

    def test_add_with_none_second(self) -> None:
        """Test adding when the second argument is None."""
        with self.assertRaises(ValueError):
            add(1.0, None)

    def test_add_with_both_none(self) -> None:
        """Test adding when both arguments are None."""
        with self.assertRaises(ValueError):
            add(None, None)
