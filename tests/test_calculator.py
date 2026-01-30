import pytest
from src.calculator import add


def test_add_success() -> None:
    """Test successful addition of two numbers."""
    assert add(1.0, 2.0) == 3.0


def test_add_with_none() -> None:
    """Test that adding with None raises ValueError."""
    with pytest.raises(ValueError):
        add(None, 1.0)
    with pytest.raises(ValueError):
        add(1.0, None)
    with pytest.raises(ValueError):
        add(None, None)
