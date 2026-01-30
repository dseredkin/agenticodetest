def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None or b is None:
        raise ValueError("One or both arguments are None")
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract two numbers.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The result of a minus b.

    Raises:
        ValueError: If either a or b is None.
    """
    if a is None or b is None:
        raise ValueError("One or both arguments are None")
    return a - b
