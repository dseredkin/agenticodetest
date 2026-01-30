"""Tests for calculator module."""

import pytest
from src.calculator import add, divide, subtract


def test_add_positive() -> None:
    """Test addition with positive numbers."""
    assert add(5, 3) == 8.0


def test_add_negative() -> None:
    """Test addition with negative numbers."""
    assert add(5, -3) == 2.0


def test_subtract_positive() -> None:
    """Test subtraction with positive numbers."""
    assert subtract(5, 3) == 2.0


def test_subtract_negative() -> None:
    """Test subtraction with negative numbers."""
    assert subtract(5, -3) == 8.0


def test_divide_positive() -> None:
    """Test division with positive numbers."""
    assert divide(10, 2) == 5.0


def test_divide_negative() -> None:
    """Test division with negative denominator."""
    assert divide(10, -2) == -5.0


def test_divide_zero_numerator() -> None:
    """Test division with zero numerator."""
    assert divide(0, 5) == 0.0


def test_divide_large_numbers() -> None:
    """Test division with large numbers."""
    assert divide(1e10, 2) == 5e9


def test_divide_by_zero() -> None:
    """Test division by zero raises ValueError."""
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        divide(10, 0)
