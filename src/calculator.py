from collections.abc import Callable


def newtons_method(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-6,
    max_iter: int = 100,
) -> float:
    """
    Approximates the root of a function using Newton's method.

    Args:
        f: The function for which to find the root.
        df: The derivative of the function f.
        x0: The initial guess for the root.
        tol: The tolerance for convergence (default: 1e-6).
        max_iter: The maximum number of iterations (default: 100).

    Returns:
        The approximated root of the function.

    Raises:
        ValueError: If the method does not converge or if the derivative is zero.
    """
    x = x0
    for _ in range(max_iter):
        fx = f(x)
        if abs(fx) < tol:
            return x
        dfx = df(x)
        if dfx == 0:
            raise ValueError("Derivative is zero")
        x = x - fx / dfx
    raise ValueError("Did not converge")
