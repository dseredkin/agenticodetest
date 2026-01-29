"""
Tests for the calculator module.
"""

import pytest
from src.calculator import fibonacci_sequence


def test_fibonacci_sequence() -> None:
    assert fibonacci_sequence(0) == []
    assert fibonacci_sequence(1) == [0]
    assert fibonacci_sequence(2) == [0, 1]
    assert fibonacci_sequence(5) == [0, 1, 1, 2, 3]

    with pytest.raises(ValueError):
        fibonacci_sequence(-1)
