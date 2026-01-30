"""Module for basic calculator functions."""


def add(a: int | float, b: int | float) -> float:
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.

    Raises:
        ValueError: If a or b is None or not a number.
    """
    if a is None or b is None:
        raise ValueError("One or both arguments are None")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")
    return a + b


def subtract(a: int | float, b: int | float) -> float:
    """Subtract two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The difference of a and b.

    Raises:
        ValueError: If a or b is None or not a number.
    """
    if a is None or b is None:
        raise ValueError("One or both arguments are None")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers")
    return a - b
