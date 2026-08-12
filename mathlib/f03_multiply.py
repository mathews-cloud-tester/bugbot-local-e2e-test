"""
mathlib.f03_multiply - Multiplication utilities.

Provides scalar and iterable product helpers with full type annotations.
All public functions include doctest examples that can be run with:

    python -m doctest mathlib/f03_multiply.py -v

Functions
---------
multiply(a, b)
    Return the product of two numeric values.
multiply_many(values)
    Return the product of all values in an iterable.
"""

from __future__ import annotations

from typing import Iterable, Union

Number = Union[int, float]


def multiply(a: Number, b: Number) -> Number:
    """Return the product of *a* and *b*.

    Parameters
    ----------
    a : int or float
        First factor.
    b : int or float
        Second factor.

    Returns
    -------
    int or float
        The arithmetic product ``a * b``.

    Examples
    --------
    >>> multiply(3, 4)
    12
    >>> multiply(2.5, 4.0)
    10.0
    >>> multiply(-3, 5)
    -15
    >>> multiply(0, 999)
    0
    """
    return a * b


def multiply_many(values: Iterable[Number]) -> Number:
    """Return the product of all numbers in *values*.

    Parameters
    ----------
    values : iterable of int or float
        An iterable of numeric values.  An empty iterable yields the
        multiplicative identity ``1``.

    Returns
    -------
    int or float
        Cumulative product of every element in *values*.

    Examples
    --------
    >>> multiply_many([1, 2, 3, 4])
    24
    >>> multiply_many([2.0, 3.0, 0.5])
    3.0
    >>> multiply_many([7])
    7
    >>> multiply_many([])
    1
    """
    result: Number = 1
    for v in values:
        result = multiply(result, v)
    return result
