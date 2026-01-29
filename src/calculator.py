def divide(a: float, b: float) -> float:
    """
    Divide two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b
