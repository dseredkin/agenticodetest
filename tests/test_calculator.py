import pytest
from src.calculator import add


def test_add_success() -> None:
    """Test successful addition of two numbers."""
    assert add(1, 2) == 3.0
    assert add(1.5, 2.5) == 4.0


def test_add_with_none() -> None:
    """Test addition with None inputs."""
    with pytest.raises(ValueError, match="Argument a cannot be None"):
        add(None, 1)
    with pytest.raises(ValueError, match="Argument b cannot be None"):
        add(1, None)
    with pytest.raises(ValueError, match="Argument a cannot be None"):
        add(None, None)


def test_add_with_non_number() -> None:
    """Test addition with non-numeric inputs."""
    with pytest.raises(ValueError, match="Argument a must be a number"):
        add("a", 1)
    with pytest.raises(ValueError, match="Argument b must be a number"):
        add(1, "b")
