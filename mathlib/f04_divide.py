"""
mathlib.f04_divide - Division utilities.

Provides scalar true-division and integer-division helpers with full type
annotations and robust zero-divisor handling.
All public functions include doctest examples that can be run with:

    python -m doctest mathlib/f04_divide.py -v

Functions
---------
divide(a, b)
    Return the true quotient of two numeric values.
floor_divide(a, b)
    Return the floor (integer) quotient of two numeric values.
safe_divide(a, b, default)
    Return the true quotient, or *default* if *b* is zero.
"""

from __future__ import annotations

from typing import Optional, Union

Number = Union[int, float]


def divide(a: Number, b: Number) -> float:
    """Return *a* divided by *b* (true division).

    Parameters
    ----------
    a : int or float
        Dividend.
    b : int or float
        Divisor.  Must not be zero.

    Returns
    -------
    float
        The true quotient ``a / b``.

    Raises
    ------
    ZeroDivisionError
        If *b* is ``0``.

    Examples
    --------
    >>> divide(10, 2)
    5.0
    >>> divide(7, 2)
    3.5
    >>> divide(-9, 3)
    -3.0
    >>> divide(1, 4)
    0.25
    """
    if b == 0:
        raise ZeroDivisionError("divisor must not be zero")
    return a / b


def floor_divide(a: int, b: int) -> int:
    """Return the floor quotient of *a* divided by *b*.

    Parameters
    ----------
    a : int
        Dividend.
    b : int
        Divisor.  Must not be zero.

    Returns
    -------
    int
        ``a // b`` (floor division).

    Raises
    ------
    ZeroDivisionError
        If *b* is ``0``.

    Examples
    --------
    >>> floor_divide(10, 3)
    3
    >>> floor_divide(7, 2)
    3
    >>> floor_divide(-7, 2)
    -4
    >>> floor_divide(9, 9)
    1
    """
    if b == 0:
        raise ZeroDivisionError("divisor must not be zero")
    return a // b


def safe_divide(a: Number, b: Number, default: Optional[Number] = None) -> Optional[float]:
    """Return *a* / *b*, or *default* when *b* is zero.

    Parameters
    ----------
    a : int or float
        Dividend.
    b : int or float
        Divisor.
    default : int, float, or None, optional
        Value returned when *b* is zero.  Defaults to ``None``.

    Returns
    -------
    float or default
        True quotient, or *default* on zero divisor.

    Examples
    --------
    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(5, 0) is None
    True
    >>> safe_divide(5, 0, default=0)
    0
    >>> safe_divide(3.0, 1.5)
    2.0
    """
    if b == 0:
        return default
    return a / b
