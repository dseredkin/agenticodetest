"""Tests for the calculator module."""

import pytest
from src.calculator import add


def test_add_normal() -> None:
    """Test adding two valid numbers."""
    assert add(2, 3) == 5.0


def test_add_with_none() -> None:
    """Test adding with None input."""
    with pytest.raises(ValueError, match="Inputs must not be None"):
        add(None, 3)


def test_add_with_non_number() -> None:
    """Test adding with non-number input."""
    with pytest.raises(ValueError, match="Inputs must be numbers"):
        add("a", 3)
