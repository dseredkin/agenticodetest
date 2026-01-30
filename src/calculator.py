"""Calculator module providing basic arithmetic operations."""


def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Args:
        a: The numerator.
        b: The denominator. Must not be zero.

    Returns:
        The result of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
