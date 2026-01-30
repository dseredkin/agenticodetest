"""Tests for the calculator module."""

import pytest
from src.calculator import add, divide, subtract


def test_add() -> None:
    """Test the add function."""
    assert add(2.0, 3.0) == 5.0
    assert add(-1.0, 1.0) == 0.0
    assert add(1e10, 1e10) == 2e10  # Test large numbers


def test_subtract() -> None:
    """Test the subtract function."""
    assert subtract(5.0, 3.0) == 2.0
    assert subtract(-1.0, -1.0) == 0.0
    assert subtract(1e10, 1e10) == 0.0  # Test large numbers


def test_divide() -> None:
    """Test the divide function."""
    assert divide(10.0, 2.0) == 5.0
    assert divide(-10.0, 2.0) == -5.0  # Test negative numerator
    assert divide(10.0, -2.0) == -5.0  # Test negative denominator
    assert divide(1e10, 2.0) == 5e9  # Test large numbers
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        divide(10.0, 0.0)
