"""
Module for basic arithmetic operations with clarification on addition behavior.

This module provides functions for adding numbers, with 'add' performing standard
addition and 'safe_add' including checks to ensure inputs are valid numbers.
"""


def add(a: float, b: float) -> float:
    """
    Adds two numbers.

    This function performs straightforward addition of two floating-point numbers.
    It assumes both inputs are numbers and does not perform any type checks.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b.

    Raises:
        TypeError: If a or b is not a number (handled by Python's built-in addition).
    """
    return a + b


def safe_add(a: float, b: float) -> float:
    """
    Safely adds two numbers after verifying they are numeric.

    This function first checks if both inputs are instances of int or float.
    If not, it raises a ValueError. Otherwise, it performs the addition.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b.

    Raises:
        ValueError: If either a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers (int or float).")
    return a + b
