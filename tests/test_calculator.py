import math

import pytest
from src.calculator import newtons_method


def test_newtons_method_quadratic() -> None:
    """Test Newton's method with a simple quadratic function."""

    def f(x: float) -> float:
        return x**2 - 4  # Roots at 2 and -2

    def df(x: float) -> float:
        return 2 * x

    root_positive = newtons_method(f, df, 1.0)
    assert abs(root_positive - 2) < 0.01  # Check approximation

    root_negative = newtons_method(f, df, -1.0)
    assert abs(root_negative + 2) < 0.01  # Check approximation


def test_newtons_method_no_real_root() -> None:
    """Test Newton's method for a function with no real roots."""

    def f(x: float) -> float:
        return math.exp(x) + 1  # No real root

    def df(x: float) -> float:
        return math.exp(x)

    with pytest.raises(ValueError):
        newtons_method(f, df, 0, tol=1e-6, max_iter=5)


def test_newtons_method_small_tolerance() -> None:
    """Test Newton's method with a very small tolerance."""

    def f(x: float) -> float:
        return x**2 - 4

    def df(x: float) -> float:
        return 2 * x

    root = newtons_method(f, df, 1.0, tol=1e-10, max_iter=200)
    assert abs(root - 2) < 1e-8  # Expect high precision


def test_newtons_method_derivative_zero() -> None:
    """Test Newton's method when derivative is zero."""

    def f(x: float) -> float:
        return x**2

    def df(x: float) -> float:
        return 2 * x  # Derivative is zero at x=0

    with pytest.raises(ValueError):
        newtons_method(f, df, 0.0)


def test_newtons_method_input_validation() -> None:
    """Test input validation for non-callable functions."""

    def f(x: float) -> float:
        return x**2 - 4

    with pytest.raises(ValueError):
        newtons_method(5, f, 1.0)  # f is callable, but df is not

    with pytest.raises(ValueError):
        newtons_method(f, 5, 1.0)  # df is not callable
