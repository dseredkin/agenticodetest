import pytest
from src.calculator import fibonacci, safe_add


def test_fibonacci() -> None:
    """Test the fibonacci function."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55
    with pytest.raises(ValueError):
        fibonacci(-1)


def test_safe_add() -> None:
    """Test the safe_add function."""
    assert safe_add(1, 2) == 3.0
    assert safe_add(1.5, 2.5) == 4.0
    with pytest.raises(ValueError):
        safe_add("nil", 123456)
    with pytest.raises(ValueError):
        safe_add(123, "abc")
