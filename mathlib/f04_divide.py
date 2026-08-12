"""
mathlib.f04_divide - Division utilities
========================================

This module provides division operations for scalars and sequences of numbers.
It supports true division (always returns a float) as well as integer (floor)
division.  Division by zero is detected early and raises a clear ``ZeroDivisionError``
rather than propagating a cryptic runtime exception.

All public functions are fully type-annotated and include doctest examples.

Functions
---------
divide(a, b)
    Return the true (float) quotient ``a / b``.
floor_divide(a, b)
    Return the integer (floor) quotient ``a // b``.
safe_divide(a, b, default)
    Return ``a / b``, or *default* when *b* is zero.
divide_sequence(values, divisor)
    Return a new list with every element divided by *divisor*.
"""

from __future__ import annotations

from typing import Optional, Sequence, Union

Number = Union[int, float]


def divide(a: Number, b: Number) -> float:
    """Return the true quotient ``a / b`` as a float.

    Parameters
    ----------
    a:
        Dividend.
    b:
        Divisor.  Must not be zero.

    Returns
    -------
    float
        The result of ``a / b``.

    Raises
    ------
    ZeroDivisionError
        If *b* is zero.
    TypeError
        If either argument is not numeric.

    Examples
    --------
    >>> divide(10, 4)
    2.5
    >>> divide(9, 3)
    3.0
    >>> divide(-6, 2)
    -3.0
    >>> divide(1, 4)
    0.25
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numeric; got {type(a)} and {type(b)}")
    if b == 0:
        raise ZeroDivisionError("Division by zero is undefined")
    return a / b


def floor_divide(a: int, b: int) -> int:
    """Return the integer (floor) quotient ``a // b``.

    Parameters
    ----------
    a:
        Dividend (integer).
    b:
        Divisor (integer).  Must not be zero.

    Returns
    -------
    int
        The largest integer ``q`` such that ``q * b <= a``.

    Raises
    ------
    ZeroDivisionError
        If *b* is zero.
    TypeError
        If either argument is not an integer.

    Examples
    --------
    >>> floor_divide(10, 3)
    3
    >>> floor_divide(9, 3)
    3
    >>> floor_divide(-7, 2)
    -4
    >>> floor_divide(0, 5)
    0
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError(f"Both arguments must be integers; got {type(a)} and {type(b)}")
    if b == 0:
        raise ZeroDivisionError("Floor division by zero is undefined")
    return a // b


def safe_divide(a: Number, b: Number, default: Optional[Number] = None) -> Optional[float]:
    """Return ``a / b``, or *default* when *b* is zero instead of raising.

    This is a convenience wrapper around :func:`divide` that swallows
    ``ZeroDivisionError`` and returns a caller-supplied fallback value.

    Parameters
    ----------
    a:
        Dividend.
    b:
        Divisor.
    default:
        Value to return when *b* is zero.  Defaults to ``None``.

    Returns
    -------
    float or default
        The quotient, or *default* if division is impossible.

    Examples
    --------
    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(5, 0) is None
    True
    >>> safe_divide(5, 0, default=0)
    0
    >>> safe_divide(-8, 4)
    -2.0
    """
    if b == 0:
        return default
    return divide(a, b)


def divide_sequence(values: Sequence[Number], divisor: Number) -> list[float]:
    """Return a new list with every element of *values* divided by *divisor*.

    Parameters
    ----------
    values:
        A sequence of numbers (the dividends).
    divisor:
        A non-zero scalar divisor applied to every element.

    Returns
    -------
    list[float]
        A list of the same length as *values*.

    Raises
    ------
    ZeroDivisionError
        If *divisor* is zero.
    TypeError
        If *divisor* or any element of *values* is not numeric.

    Examples
    --------
    >>> divide_sequence([10, 20, 30], 10)
    [1.0, 2.0, 3.0]
    >>> divide_sequence([1, 2, 3], 2)
    [0.5, 1.0, 1.5]
    >>> divide_sequence([], 5)
    []
    >>> divide_sequence([-6, 0, 9], 3)
    [-2.0, 0.0, 3.0]
    """
    if not isinstance(divisor, (int, float)):
        raise TypeError(f"divisor must be numeric; got {type(divisor)}")
    if divisor == 0:
        raise ZeroDivisionError("divisor must not be zero")
    for i, val in enumerate(values):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Element at index {i} is not numeric: {type(val)}")
    return [val / divisor for val in values]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
