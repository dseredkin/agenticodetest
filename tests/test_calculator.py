"""Tests for the calculator module."""

import pytest
from src.calculator import add, subtract


def test_add_normal() -> None:
    """Test adding two valid numbers."""
    assert add(2, 3) == 5.0


def test_add_with_none() -> None:
    """Test adding with None input."""
    with pytest.raises(ValueError, match="One or both arguments are None"):
        add(None, 3)


def test_add_with_non_number() -> None:
    """Test adding with non-number input."""
    with pytest.raises(ValueError, match="Inputs must be numbers"):
        add("a", 3)


def test_subtract_normal() -> None:
    """Test subtracting two valid numbers."""
    assert subtract(5, 3) == 2.0


def test_subtract_with_none() -> None:
    """Test subtracting with None input."""
    with pytest.raises(ValueError, match="One or both arguments are None"):
        subtract(None, 3)


def test_subtract_with_non_number() -> None:
    """Test subtracting with non-number input."""
    with pytest.raises(ValueError, match="Inputs must be numbers"):
        subtract("a", 3)
