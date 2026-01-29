"""Tests for hello module."""

from src.hello import print_hello


def test_print_hello(capsys):
    """Test that print_hello outputs Hello, World\!"""
    print_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World\!\n"

