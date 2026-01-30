def add(a: float | None, b: float | None) -> float | None:
    """Add two numbers.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b if both are valid numbers.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None or b is None:
        raise ValueError("Both arguments must be numbers, not None")
    return a + b
