import pytest
from src.calculator import divide


def test_divide() -> None:
    """Test successful division operations."""
    assert divide(10, 2) == 5.0
    assert divide(10, 5) == 2.0


def test_divide_by_zero() -> None:
    """Test division by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)
