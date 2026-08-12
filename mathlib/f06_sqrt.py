"""
mathlib.f06_sqrt - Square-root utilities.

Provides square root, integer square root, and Newton-Raphson approximation
helpers with full type annotations.
All public functions include doctest examples that can be run with:

    python -m doctest mathlib/f06_sqrt.py -v

Functions
---------
sqrt(x)
    Return the square root of *x* using the standard math library.
isqrt(n)
    Return the integer square root (floor) of a non-negative integer *n*.
sqrt_newton(x, tolerance)
    Compute the square root of *x* via Newton-Raphson iteration.
"""

from __future__ import annotations

import math
from typing import Union

Number = Union[int, float]


def sqrt(x: Number) -> float:
    """Return the square root of *x*.

    Parameters
    ----------
    x : int or float
        Non-negative value whose square root is desired.

    Returns
    -------
    float
        ``math.sqrt(x)``.

    Raises
    ------
    ValueError
        If *x* is negative.

    Examples
    --------
    >>> sqrt(4)
    2.0
    >>> sqrt(2.0)
    1.4142135623730951
    >>> sqrt(0)
    0.0
    >>> sqrt(100)
    10.0
    """
    if x < 0:
        raise ValueError("sqrt requires a non-negative number")
    return math.sqrt(x)


def isqrt(n: int) -> int:
    """Return the integer square root (floor) of *n*.

    Equivalent to ``math.isqrt(n)`` but implemented to illustrate the
    binary-search approach.

    Parameters
    ----------
    n : int
        Non-negative integer.

    Returns
    -------
    int
        The largest integer *k* such that ``k * k <= n``.

    Raises
    ------
    ValueError
        If *n* is negative.

    Examples
    --------
    >>> isqrt(16)
    4
    >>> isqrt(15)
    3
    >>> isqrt(0)
    0
    >>> isqrt(1)
    1
    """
    if n < 0:
        raise ValueError("isqrt requires a non-negative integer")
    if n == 0:
        return 0
    lo, hi = 0, n
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


def sqrt_newton(x: Number, tolerance: float = 1e-10) -> float:
    """Compute the square root of *x* via Newton-Raphson iteration.

    Starts from an initial guess of ``x / 2`` and iterates using:

        guess = (guess + x / guess) / 2

    until successive guesses differ by less than *tolerance*.

    Parameters
    ----------
    x : int or float
        Non-negative value whose square root is desired.
    tolerance : float, optional
        Convergence threshold.  Defaults to ``1e-10``.

    Returns
    -------
    float
        Approximation of ``sqrt(x)`` within *tolerance*.

    Raises
    ------
    ValueError
        If *x* is negative.

    Examples
    --------
    >>> abs(sqrt_newton(4) - 2.0) < 1e-9
    True
    >>> abs(sqrt_newton(2) - 1.4142135623730951) < 1e-9
    True
    >>> sqrt_newton(0)
    0.0
    >>> abs(sqrt_newton(9, tolerance=1e-6) - 3.0) < 1e-5
    True
    """
    if x < 0:
        raise ValueError("sqrt_newton requires a non-negative number")
    if x == 0:
        return 0.0
    guess: float = x / 2.0
    while True:
        next_guess = (guess + x / guess) / 2.0
        if abs(next_guess - guess) < tolerance:
            return next_guess
        guess = next_guess
