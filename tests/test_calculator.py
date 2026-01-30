"""Tests for the calculator module."""

import pytest
from src.calculator import divide


def test_divide() -> None:
    """Test successful division."""
    assert divide(10.0, 2.0) == 5.0
    assert divide(20.0, 5.0) == 4.0


def test_divide_by_zero() -> None:
    """Test division by zero raises an error."""
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        divide(10.0, 0)
        divide(-10.0, 0)  # Additional check for negative numerator


def test_divide_negative_values() -> None:
    """Test division with negative values."""
    assert divide(-10.0, 2.0) == -5.0
    assert divide(10.0, -2.0) == -5.0
    assert divide(-10.0, -2.0) == 5.0


def test_divide_large_numbers() -> None:
    """Test division with very large numbers."""
    assert divide(1e100, 1e50) == 1e50  # Large positive numbers
    assert divide(-1e100, 1e50) == -1e50  # Large negative numerator
    assert divide(1e100, -1e50) == -1e50  # Large negative denominator
