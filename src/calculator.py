"""Module for basic calculator functions."""


def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None:
        raise ValueError("The first input must not be None")
    if b is None:
        raise ValueError("The second input must not be None")
    return a + b
