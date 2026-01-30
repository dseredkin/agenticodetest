def add(a: float | None, b: float | None) -> float:
    """Add two numbers.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.

    Raises:
        ValueError: If either a or b is None or not a number.
    """
    if a is None:
        raise ValueError("Argument a cannot be None")
    if b is None:
        raise ValueError("Argument b cannot be None")
    if not isinstance(a, (int, float)):
        raise ValueError("Argument a must be a number")
    if not isinstance(b, (int, float)):
        raise ValueError("Argument b must be a number")
    return float(a) + float(b)
