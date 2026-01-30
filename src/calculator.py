"""Module for basic calculator operations."""


def add(a: float | None, b: float | None) -> float:
    """
    Add two numbers.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None:
        raise ValueError("The first argument cannot be None.")
    if b is None:
        raise ValueError("The second argument cannot be None.")
    return a + b
