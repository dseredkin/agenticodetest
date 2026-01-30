from typing import Any


def fibonacci(n: int) -> int:
    """Compute and return the nth Fibonacci number.

    Args:
        n: A non-negative integer.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


def safe_add(a: Any, b: Any) -> float:
    """Safely add two values if they can be converted to floats.

    Args:
        a: The first value to add.
        b: The second value to add.

    Returns:
        The sum as a float if successful.

    Raises:
        ValueError: If either argument cannot be converted to a float.
    """
    try:
        return float(a) + float(b)
    except ValueError:
        raise ValueError("Both arguments must be convertible to float")
