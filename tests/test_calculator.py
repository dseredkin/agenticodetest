"""Tests for the calculator module."""

import pytest
from src.calculator import add, divide, subtract


def test_add_success() -> None:
    """Test successful addition."""
    assert add(2, 3) == 5.0
    assert add(-1, 1) == 0.0


def test_subtract_success() -> None:
    """Test successful subtraction."""
    assert subtract(5, 3) == 2.0
    assert subtract(0, 5) == -5.0


def test_divide_success() -> None:
    """Test successful division."""
    assert divide(10, 5) == 2.0
    assert divide(4, 2) == 2.0


def test_divide_by_zero() -> None:
    """Test division by zero raises an error."""
    with pytest.raises(ValueError, match="Denominator cannot be zero"):
        divide(1, 0)
