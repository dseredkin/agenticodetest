"""Module for basic calculator operations."""


def divide(x: float, y: float) -> float:
    """
    Divide two numbers.

    Args:
        x (float): The numerator.
        y (float): The denominator.

    Returns:
        float: The result of x divided by y.

    Raises:
        ValueError: If y is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
