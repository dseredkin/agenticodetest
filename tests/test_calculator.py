"""Tests for the calculator module."""

import pytest
from src.calculator import divide


def test_divide() -> None:
    """Test the divide function."""
    assert divide(10.0, 2.0) == 5.0
    assert divide(15.0, 3.0) == 5.0  # Additional test case
    with pytest.raises(ValueError):
        divide(10.0, 0.0)
