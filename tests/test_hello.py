"""Tests for hello module."""

from src.hello import hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello() == "Hello, World!"
