"""Module for basic calculator functions."""


def add(a: float | None, b: float | None) -> float | None:
    """
    Add two numbers.

    Args:
        a (float | None): The first number.
        b (float | None): The second number.

    Returns:
        float | None: The sum of a and b if both are numbers, otherwise None.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None or b is None:
        raise ValueError("Both inputs must be numbers; None values are not allowed.")
    return a + b
