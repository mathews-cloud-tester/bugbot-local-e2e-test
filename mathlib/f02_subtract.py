"""
mathlib.f02_subtract - Subtraction utilities.

Provides scalar and cumulative subtraction helpers with full type annotations.
All public functions include doctest examples that can be run with:

    python -m doctest mathlib/f02_subtract.py -v

Functions
---------
subtract(a, b)
    Return the difference of two numeric values.
subtract_many(values)
    Subtract each successive value from the first element in an iterable.
"""

from __future__ import annotations

from typing import Iterable, Union

Number = Union[int, float]


def subtract(a: Number, b: Number) -> Number:
    """Return *a* minus *b*.

    Parameters
    ----------
    a : int or float
        Minuend.
    b : int or float
        Subtrahend.

    Returns
    -------
    int or float
        The arithmetic difference ``a - b``.

    Examples
    --------
    >>> subtract(10, 3)
    7
    >>> subtract(1.5, 0.5)
    1.0
    >>> subtract(0, 5)
    -5
    >>> subtract(-3, -3)
    0
    """
    return a - b


def subtract_many(values: Iterable[Number]) -> Number:
    """Subtract each successive value from the first element.

    Equivalent to ``values[0] - values[1] - values[2] - ...``.

    Parameters
    ----------
    values : iterable of int or float
        An iterable with at least one element.  The first element is used as
        the initial accumulator; all subsequent elements are subtracted from it.

    Returns
    -------
    int or float
        Result of left-associative subtraction across *values*.

    Raises
    ------
    ValueError
        If *values* is empty.

    Examples
    --------
    >>> subtract_many([10, 1, 2, 3])
    4
    >>> subtract_many([100, 50])
    50
    >>> subtract_many([5])
    5
    >>> subtract_many([0.0, 0.5, 0.25])
    -0.75
    """
    it = iter(values)
    try:
        result: Number = next(it)
    except StopIteration:
        raise ValueError("subtract_many requires at least one value")
    for v in it:
        result = subtract(result, v)
    return result
