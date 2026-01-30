"""Tests for the calculator module."""

import pytest
from src.calculator import add


def test_add_success() -> None:
    """Test successful addition of two numbers."""
    assert add(2.0, 3.0) == 5.0


def test_add_with_none_first() -> None:
    """Test addition when the first argument is None."""
    with pytest.raises(ValueError, match="The first argument cannot be None."):
        add(None, 3.0)


def test_add_with_none_second() -> None:
    """Test addition when the second argument is None."""
    with pytest.raises(ValueError, match="The second argument cannot be None."):
        add(2.0, None)


def test_add_with_both_none() -> None:
    """Test addition when both arguments are None."""
    with pytest.raises(ValueError):
        add(None, None)
