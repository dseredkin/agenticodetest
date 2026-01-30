"""
Unit tests for the calculator module.

These tests verify the behavior of the add and safe_add functions,
ensuring clarity in addition operations.
"""

import pytest
from src.calculator import add, safe_add


def test_add() -> None:
    """Test the add function with various numeric inputs."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(1.5, 2.5) == 4.0
    # Note: add will raise TypeError for non-numbers, but we don't test that here as it's built-in behavior


def test_safe_add() -> None:
    """Test the safe_add function, including error handling."""
    assert safe_add(1, 2) == 3
    assert safe_add(-1, 1) == 0
    assert safe_add(1.5, 2.5) == 4.0
    with pytest.raises(ValueError):
        safe_add("a", 1)
    with pytest.raises(ValueError):
        safe_add(1, "b")
    with pytest.raises(ValueError):
        safe_add("a", "b")
    with pytest.raises(ValueError):
        safe_add(None, 1)
