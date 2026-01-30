"""Tests for the calculator module."""

import pytest
from src.calculator import divide


def test_divide() -> None:
    """Test the divide function."""
    assert divide(4.0, 2.0) == 2.0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(4.0, 0.0)
