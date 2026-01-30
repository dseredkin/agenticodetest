import pytest
from src.calculator import divide


def test_divide() -> None:
    """Test the divide function."""
    assert divide(10.0, 2.0) == 5.0
    assert divide(20.0, 4.0) == 5.0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10.0, 0)
