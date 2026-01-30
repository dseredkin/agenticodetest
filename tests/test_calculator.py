import pytest
from src.calculator import divide


def test_divide() -> None:
    """Test the divide function."""
    assert divide(10, 2) == 5.0
    assert divide(10, 5) == 2.0
    with pytest.raises(ValueError):
        divide(10, 0)
