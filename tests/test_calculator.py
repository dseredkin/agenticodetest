import unittest

from src.calculator import divide


class TestCalculator(unittest.TestCase):
    def test_divide_success(self) -> None:
        """Test successful division."""
        assert divide(10.0, 2.0) == 5.0
        assert divide(20.0, 5.0) == 4.0

    def test_divide_by_zero(self) -> None:
        """Test division by zero raises an error."""
        with self.assertRaises(ValueError):
            divide(10.0, 0)
