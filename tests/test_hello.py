"""Tests for hello module."""

from src.hello import greet


def test_greet() -> None:
    """Test the greet function."""
    assert greet() == "Hello, World!"
