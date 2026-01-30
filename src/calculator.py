def divide(a: float, b: float) -> float:
    """Perform division of two numbers.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of a divided by b.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero.")
    return a / b
