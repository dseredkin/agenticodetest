"""Unit tests for the calculator module."""

import unittest

from src.calculator import add, subtract


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

    def test_add_non_number_first(self) -> None:
        """Test addition when the first argument is not a number."""
        with self.assertRaises(TypeError):
            add("a", 1.0)

    def test_add_non_number_second(self) -> None:
        """Test addition when the second argument is not a number."""
        with self.assertRaises(TypeError):
            add(1.0, "b")

    def test_add_non_number_both(self) -> None:
        """Test addition when both arguments are not numbers."""
        with self.assertRaises(TypeError):
            add("a", "b")

    def test_add_zero(self) -> None:
        """Test addition with zero."""
        assert add(0.0, 5.0) == 5.0

    def test_add_negative(self) -> None:
        """Test addition with negative numbers."""
        assert add(-1.0, 1.0) == 0.0

    def test_subtract_success(self) -> None:
        """Test successful subtraction of two numbers."""
        assert subtract(5.0, 3.0) == 2.0

    def test_subtract_none_first(self) -> None:
        """Test subtraction when the first argument is None."""
        with self.assertRaises(ValueError):
            subtract(None, 3.0)

    def test_subtract_none_second(self) -> None:
        """Test subtraction when the second argument is None."""
        with self.assertRaises(ValueError):
            subtract(3.0, None)

    def test_subtract_none_both(self) -> None:
        """Test subtraction when both arguments are None."""
        with self.assertRaises(ValueError):
            subtract(None, None)

    def test_subtract_non_number_first(self) -> None:
        """Test subtraction when the first argument is not a number."""
        with self.assertRaises(TypeError):
            subtract("a", 3.0)

    def test_subtract_non_number_second(self) -> None:
        """Test subtraction when the second argument is not a number."""
        with self.assertRaises(TypeError):
            subtract(3.0, "b")

    def test_subtract_non_number_both(self) -> None:
        """Test subtraction when both arguments are not numbers."""
        with self.assertRaises(TypeError):
            subtract("a", "b")

    def test_subtract_zero(self) -> None:
        """Test subtraction with zero."""
        assert subtract(5.0, 0.0) == 5.0

    def test_subtract_negative(self) -> None:
        """Test subtraction with negative numbers."""
        assert subtract(1.0, -1.0) == 2.0
