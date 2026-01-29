import unittest

from src.calculator import newtons_method


def test_function(x: float) -> float:
    """Example function for testing: f(x) = x^2 - 4 (roots at x=2 and x=-2)."""
    return x**2 - 4


def test_derivative(x: float) -> float:
    """Derivative of the test function: df(x) = 2x."""
    return 2 * x


class TestCalculator(unittest.TestCase):
    def test_newtons_method(self) -> None:
        """Test Newton's method with the example function."""
        root_positive = newtons_method(test_function, test_derivative, x0=1.0)
        self.assertAlmostEqual(root_positive, 2.0, places=5)

        root_negative = newtons_method(test_function, test_derivative, x0=-1.0)
        self.assertAlmostEqual(root_negative, -2.0, places=5)

        with self.assertRaises(ValueError):
            newtons_method(
                lambda x: x**2 + 1, lambda x: 2 * x, x0=0, tolerance=1e-6
            )  # No real root

        with self.assertRaises(ValueError):
            newtons_method(test_function, lambda x: 0, x0=1.0)  # Zero derivative
