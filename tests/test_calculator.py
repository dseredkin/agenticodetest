import unittest

from src.calculator import add, subtract


class TestCalculator(unittest.TestCase):
    def test_add_success(self) -> None:
        """Test adding two valid numbers."""
        result = add(2.0, 3.0)
        self.assertEqual(result, 5.0)

    def test_add_with_none_a(self) -> None:
        """Test adding when first argument is None."""
        with self.assertRaises(ValueError):
            add(None, 3.0)

    def test_add_with_none_b(self) -> None:
        """Test adding when second argument is None."""
        with self.assertRaises(ValueError):
            add(2.0, None)

    def test_add_with_both_none(self) -> None:
        """Test adding when both arguments are None."""
        with self.assertRaises(ValueError):
            add(None, None)

    def test_add_with_invalid_type_a(self) -> None:
        """Test adding with non-numeric first argument."""
        with self.assertRaises(TypeError):
            add("invalid", 3.0)

    def test_add_with_invalid_type_b(self) -> None:
        """Test adding with non-numeric second argument."""
        with self.assertRaises(TypeError):
            add(2.0, "invalid")

    def test_subtract_success(self) -> None:
        """Test subtracting two valid numbers."""
        result = subtract(5.0, 3.0)
        self.assertEqual(result, 2.0)

    def test_subtract_with_none_a(self) -> None:
        """Test subtracting when first argument is None."""
        with self.assertRaises(ValueError):
            subtract(None, 3.0)

    def test_subtract_with_none_b(self) -> None:
        """Test subtracting when second argument is None."""
        with self.assertRaises(ValueError):
            subtract(5.0, None)

    def test_subtract_with_both_none(self) -> None:
        """Test subtracting when both arguments are None."""
        with self.assertRaises(ValueError):
            subtract(None, None)

    def test_subtract_with_invalid_type_a(self) -> None:
        """Test subtracting with non-numeric first argument."""
        with self.assertRaises(TypeError):
            subtract("invalid", 3.0)

    def test_subtract_with_invalid_type_b(self) -> None:
        """Test subtracting with non-numeric second argument."""
        with self.assertRaises(TypeError):
            subtract(5.0, "invalid")


if __name__ == "__main__":
    unittest.main()
