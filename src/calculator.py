from collections.abc import Callable


def newtons_method(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tolerance: float = 1e-6,
    max_iter: int = 100,
) -> float:
    """
    Implements Newton's method to find the root of a function f(x) = 0.

    Args:
        f: The function for which to find the root.
        df: The derivative of the function f.
        x0: The initial guess for the root.
        tolerance: The convergence tolerance.
        max_iter: The maximum number of iterations.

    Returns:
        The approximate root of the function.

    Raises:
        ValueError: If the derivative is zero or maximum iterations are exceeded.
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tolerance:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero; no solution found.")
        x = x - fx / dfx
    raise ValueError("Exceeded maximum iterations; no solution found.")
