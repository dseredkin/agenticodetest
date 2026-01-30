"""Tests for the calculator module."""

import pytest
from src.calculator import add


def test_add_numbers() -> None:
    """Test adding two valid numbers."""
    assert add(1.0, 2.0) == 3.0


def test_add_with_none_first() -> None:
    """Test adding when the first argument is None."""
    with pytest.raises(ValueError):
        add(None, 1.0)


def test_add_with_none_second() -> None:
    """Test adding when the second argument is None."""
    with pytest.raises(ValueError):
        add(1.0, None)


def test_add_with_both_none() -> None:
    """Test adding when both arguments are None."""
    with pytest.raises(ValueError):
        add(None, None)
