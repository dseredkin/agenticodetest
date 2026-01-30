"""
Unit tests for the calculator module.
"""

import pytest
from src.calculator import divide


def test_divide_positive_numbers() -> None:
    """Test division with positive numbers."""
    assert divide(10, 2) == 5.0


def test_divide_negative_numbers() -> None:
    """Test division with negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_zero_numerator() -> None:
    """Test division where numerator is zero."""
    assert divide(0, 5) == 0.0


def test_divide_by_zero() -> None:
    """Test division by zero raises an error."""
    with pytest.raises(ValueError, match="Denominator cannot be zero."):
        divide(10, 0)
