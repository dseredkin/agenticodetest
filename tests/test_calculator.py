import math

import pytest
from src.calculator import newtons_method


def test_newtons_method() -> None:
    """Test Newton's method with a simple quadratic function."""

    def f(x: float) -> float:
        return x**2 - 4  # Roots at 2 and -2

    def df(x: float) -> float:
        return 2 * x

    root_positive = newtons_method(f, df, 1.0)
    assert abs(root_positive - 2) < 0.01  # Check approximation

    root_negative = newtons_method(f, df, -1.0)
    assert abs(root_negative + 2) < 0.01  # Check approximation

    with pytest.raises(ValueError):
        # Test non-convergence (e.g., bad initial guess for a function that doesn't converge easily)
        def bad_f(x: float) -> float:
            return math.exp(x) + 1  # No real root, but we'll limit by max_iter

        newtons_method(bad_f, lambda x: math.exp(x), 0, tol=1e-6, max_iter=5)
