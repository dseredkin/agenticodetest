"""Tests for the calculator module."""

import pytest
from src.calculator import divide


def test_divide_success() -> None:
    """Test successful division."""
    assert divide(10, 5) == 2.0
    assert divide(4, 2) == 2.0


def test_divide_by_zero() -> None:
    """Test division by zero raises an error."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(1, 0)
