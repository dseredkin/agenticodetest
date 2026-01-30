def add(a: float | None, b: float | None) -> float | None:
    """
    Adds two numbers if both are provided and are numbers.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b if both are numbers, otherwise None.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None:
        raise ValueError("Argument 'a' must not be None")
    if b is None:
        raise ValueError("Argument 'b' must not be None")
    return a + b
