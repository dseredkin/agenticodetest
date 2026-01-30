"""Module for basic calculator operations."""


def add(a: int | float, b: int | float) -> int | float:
    """
    Add two numbers.

    Args:
        a (int | float): The first number.
        b (int | float): The second number.

    Returns:
        int | float: The sum of a and b.

    Raises:
        ValueError: If either input is None or not a number.
    """
    if a is None:
        raise ValueError("The first input cannot be None")
    if b is None:
        raise ValueError("The second input cannot be None")
    if not isinstance(a, (int, float)):
        raise ValueError("The first input must be a number")
    if not isinstance(b, (int, float)):
        raise ValueError("The second input must be a number")
    return a + b
