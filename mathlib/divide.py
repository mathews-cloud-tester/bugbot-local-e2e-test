"""Division operations for the mathlib utility library."""


def divide(a: float, b: float) -> float:
    """Return the quotient of *a* divided by *b*.

    Raises:
        ZeroDivisionError: If *b* is zero.
    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
