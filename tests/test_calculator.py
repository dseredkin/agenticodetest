import pytest
from src.calculator import add, subtract


def test_add_success() -> None:
    """Test successful addition of two numbers."""
    assert add(1.0, 2.0) == 3.0


def test_add_with_none() -> None:
    """Test that ValueError is raised when one or both arguments are None."""
    with pytest.raises(ValueError):
        add(None, 1.0)
    with pytest.raises(ValueError):
        add(1.0, None)
    with pytest.raises(ValueError):
        add(None, None)


def test_subtract_success() -> None:
    """Test successful subtraction of two numbers."""
    assert subtract(5.0, 3.0) == 2.0
