"""Tests for the calculator module."""

import pytest
from src.calculator import add


def test_add_success() -> None:
    """Test adding two valid numbers."""
    assert add(2.0, 3.0) == 5.0


def test_add_none_first() -> None:
    """Test adding with the first input as None."""
    with pytest.raises(ValueError, match="The first input cannot be None"):
        add(None, 3.0)


def test_add_none_second() -> None:
    """Test adding with the second input as None."""
    with pytest.raises(ValueError, match="The second input cannot be None"):
        add(2.0, None)


def test_add_none_both() -> None:
    """Test adding with both inputs as None."""
    with pytest.raises(ValueError):
        add(None, None)
