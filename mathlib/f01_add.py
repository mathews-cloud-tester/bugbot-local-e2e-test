"""
mathlib.f01_add - Addition utilities.

Provides scalar and iterable addition helpers with full type annotations.
All public functions include doctest examples that can be run with:

    python -m doctest mathlib/f01_add.py -v

Functions
---------
add(a, b)
    Return the sum of two numeric values.
add_many(values)
    Return the sum of all values in an iterable.
"""

from __future__ import annotations

from typing import Iterable, Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of *a* and *b*.

    Parameters
    ----------
    a : int or float
        First operand.
    b : int or float
        Second operand.

    Returns
    -------
    int or float
        The arithmetic sum ``a + b``.

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(1.5, 2.5)
    4.0
    >>> add(-4, 4)
    0
    >>> add(0, 0)
    0
    """
    return a + b


def add_many(values: Iterable[Number]) -> Number:
    """Return the sum of all numbers in *values*.

    Parameters
    ----------
    values : iterable of int or float
        A non-empty iterable of numeric values.

    Returns
    -------
    int or float
        Cumulative sum of every element in *values*.

    Raises
    ------
    TypeError
        If *values* contains non-numeric elements.

    Examples
    --------
    >>> add_many([1, 2, 3, 4])
    10
    >>> add_many((0.5, 1.5, 2.0))
    4.0
    >>> add_many([100])
    100
    >>> add_many(range(1, 6))
    15
    """
    total: Number = 0
    for v in values:
        total = add(total, v)
    return total
