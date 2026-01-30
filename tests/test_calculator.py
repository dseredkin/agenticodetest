import pytest
from src.calculator import divide


def test_divide_positive() -> None:
    """Test division with positive numbers."""
    assert divide(10, 2) == 5.0


def test_divide_negative() -> None:
    """Test division with negative numbers."""
    assert divide(-10, 2) == -5.0
    assert divide(10, -2) == -5.0
    assert divide(-10, -2) == 5.0


def test_divide_by_zero() -> None:
    """Test division by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)
