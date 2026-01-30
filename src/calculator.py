def add(
    a: int | float | None,
    b: int | float | None,
) -> int | float | None:
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
    if a is None or b is None:
        raise ValueError("Inputs must not be None")
    return a + b
