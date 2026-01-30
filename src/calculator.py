"""
Module for basic calculator operations including addition, subtraction, and division.
"""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The result of a minus b.
    """
    return a - b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
