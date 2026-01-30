"""Tests for the calculator module."""

import pytest
from src.calculator import add, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_subtract() -> None:
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0


def test_multiply() -> None:
    assert multiply(4, 2) == 8
    assert multiply(-1, 1) == -1


def test_divide() -> None:
    assert divide(10, 2) == 5.0
    assert divide(5, 1) == 5.0
    with pytest.raises(ValueError, match="Division by zero is not allowed."):
        divide(10, 0)
