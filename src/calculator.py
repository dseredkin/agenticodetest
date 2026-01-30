"""Module for basic calculator operations."""


def divide(numerator: float, denominator: float) -> float:
    """Divide two numbers.

    Args:
        numerator: The number to divide from.
        denominator: The number to divide by.

    Returns:
        The result of the division.

    Raises:
        ValueError: If the denominator is zero.
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    return numerator / denominator
