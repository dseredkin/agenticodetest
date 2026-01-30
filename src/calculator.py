"""Calculator module for basic arithmetic operations."""


def add(a: float | None, b: float | None) -> float | None:
    """
    Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b if both are not None.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None:
        raise ValueError("The first argument must be a number, not None.")
    if b is None:
        raise ValueError("The second argument must be a number, not None.")
    return a + b
