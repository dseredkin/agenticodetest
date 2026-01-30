def add(a: float | None, b: float | None) -> float:
    """
    Adds two numbers.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b.

    Raises:
        ValueError: If either a or b is None.
        TypeError: If a or b is not a number.
    """
    if a is None:
        raise ValueError("Argument 'a' must not be None")
    if b is None:
        raise ValueError("Argument 'b' must not be None")
    return a + b


def subtract(a: float | None, b: float | None) -> float:
    """
    Subtracts two numbers.

    Args:
        a: The number to subtract from.
        b: The number to subtract.

    Returns:
        The result of a minus b.

    Raises:
        ValueError: If either a or b is None.
        TypeError: If a or b is not a number.
    """
    if a is None:
        raise ValueError("Argument 'a' must not be None")
    if b is None:
        raise ValueError("Argument 'b' must not be None")
    return a - b
