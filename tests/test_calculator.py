import unittest

from src.calculator import divide


class TestCalculator(unittest.TestCase):
    """Unit tests for the calculator module."""

    def test_divide(self) -> None:
        """Test the divide function."""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(1, 3), 0.3333333333333333, places=10)

        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
