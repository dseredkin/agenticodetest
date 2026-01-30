"""Module for basic calculator functions."""


def add(a: float | None, b: float | None) -> float:
    """
    Add two numbers.

    Args:
        a (float | None): The first number.
        b (float | None): The second number.

    Returns:
        float: The sum of a and b.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None:
        raise ValueError("The first input cannot be None")
    if b is None:
        raise ValueError("The second input cannot be None")
    return a + b
