import pytest
from src.calculator import add, divide, subtract


def test_add() -> None:
    """Test the add function."""
    assert add(2, 3) == 5.0
    assert add(-1, 1) == 0.0  # Test with negative and zero
    assert add(0, 0) == 0.0  # Edge case


def test_subtract() -> None:
    """Test the subtract function."""
    assert subtract(5, 3) == 2.0
    assert subtract(0, 0) == 0.0  # Edge case
    assert subtract(-1, -1) == 0.0  # Test with negatives


def test_divide() -> None:
    """Test the divide function."""
    assert divide(10, 2) == 5.0
    assert divide(15, 3) == 5.0
    assert divide(-10, 2) == -5.0  # Test with negative numerator
    assert divide(10, -2) == -5.0  # Test with negative denominator
    with pytest.raises(ValueError, match="Denominator cannot be zero."):
        divide(10, 0)  # Test division by zero
