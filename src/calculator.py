"""Module for basic calculator functions."""


def add(a: float, b: float) -> float:
    """
    Add two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.

    Raises:
        ValueError: If either a or b is None.
        TypeError: If a or b is not a number.
    """
    if a is None:
        raise ValueError("The first argument cannot be None")
    if b is None:
        raise ValueError("The second argument cannot be None")
    if not isinstance(a, (int, float)):
        raise TypeError("The first argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("The second argument must be a number")
    return float(a) + float(b)


def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference of a and b.

    Raises:
        ValueError: If either a or b is None.
        TypeError: If a or b is not a number.
    """
    if a is None:
        raise ValueError("The first argument cannot be None")
    if b is None:
        raise ValueError("The second argument cannot be None")
    if not isinstance(a, (int, float)):
        raise TypeError("The first argument must be a number")
    if not isinstance(b, (int, float)):
        raise TypeError("The second argument must be a number")
    return float(a) - float(b)
