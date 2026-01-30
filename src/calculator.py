"""Module for basic calculator functions."""


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None:
        raise ValueError("The first argument cannot be None")
    if b is None:
        raise ValueError("The second argument cannot be None")
    return a + b
