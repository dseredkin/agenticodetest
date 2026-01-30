"""Module for basic arithmetic operations."""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract the second number from the first."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Divide the first number by the second.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Raises:
        ValueError: If b is zero.

    Returns:
        float: The result of a divided by b.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
