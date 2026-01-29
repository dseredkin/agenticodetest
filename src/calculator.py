from collections.abc import (
    Callable as TypingCallable,  # To avoid confusion with collections
)


def newtons_method(
    f: TypingCallable[[float], float],
    df: TypingCallable[[float], float],
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
        ValueError: If the method does not converge, if the derivative is zero,
                    or if f or df are not callable.
    """
    if not callable(f):
        raise ValueError("f must be a callable function")
    if not callable(df):
        raise ValueError("df must be a callable function")

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
