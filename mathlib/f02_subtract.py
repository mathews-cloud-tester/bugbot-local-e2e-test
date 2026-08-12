"""
mathlib.f02_subtract - Subtraction utilities
=============================================

This module provides subtraction operations for scalars and sequences of
numbers.  It supports integers, floats, and any numeric type compatible with
the ``-`` operator.  All public functions are fully type-annotated and include
doctest examples.

Functions
---------
subtract(a, b)
    Return the difference of two scalar numbers (``a - b``).
subtract_many(*args)
    Subtract all subsequent values from the first value.
running_difference(values)
    Return a list of successive differences between adjacent elements.
"""

from __future__ import annotations

from typing import Sequence, Union

Number = Union[int, float]


def subtract(a: Number, b: Number) -> Number:
    """Return the arithmetic difference ``a - b``.

    Parameters
    ----------
    a:
        Minuend.
    b:
        Subtrahend.

    Returns
    -------
    Number
        ``a - b``.

    Raises
    ------
    TypeError
        If either argument is not numeric.

    Examples
    --------
    >>> subtract(10, 3)
    7
    >>> subtract(0, 5)
    -5
    >>> subtract(-4, -4)
    0
    >>> subtract(1.5, 0.5)
    1.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numeric; got {type(a)} and {type(b)}")
    return a - b


def subtract_many(*args: Number) -> Number:
    """Subtract all subsequent values from the first value.

    Computes ``args[0] - args[1] - args[2] - ...``.  At least one argument
    must be supplied; if only one argument is given it is returned unchanged.

    Parameters
    ----------
    *args:
        Variable-length list of numbers.  The first element is the starting
        value; all remaining elements are subtracted from it in order.

    Returns
    -------
    Number
        The result of the left-associative subtraction chain.

    Raises
    ------
    ValueError
        If no arguments are provided.
    TypeError
        If any argument is not numeric.

    Examples
    --------
    >>> subtract_many(10, 1, 2, 3)
    4
    >>> subtract_many(100)
    100
    >>> subtract_many(0, -5, -5)
    10
    >>> subtract_many(1.0, 0.5, 0.25)
    0.25
    """
    if not args:
        raise ValueError("subtract_many requires at least one argument")
    for i, val in enumerate(args):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Argument at index {i} is not numeric: {type(val)}")
    result: Number = args[0]
    for val in args[1:]:
        result = result - val
    return result


def running_difference(values: Sequence[Number]) -> list[Number]:
    """Return successive differences between adjacent elements of *values*.

    ``result[i] = values[i+1] - values[i]`` for all valid ``i``.
    The output list has length ``len(values) - 1``.

    Parameters
    ----------
    values:
        A sequence of at least two numbers.

    Returns
    -------
    list[Number]
        A list of pairwise differences.

    Raises
    ------
    ValueError
        If *values* has fewer than two elements.
    TypeError
        If any element is not numeric.

    Examples
    --------
    >>> running_difference([1, 3, 6, 10])
    [2, 3, 4]
    >>> running_difference([10, 5, 3])
    [-5, -2]
    >>> running_difference([0.0, 0.5, 1.5])
    [0.5, 1.0]
    >>> running_difference([7, 7])
    [0]
    """
    if len(values) < 2:
        raise ValueError("running_difference requires a sequence of at least two elements")
    for i, val in enumerate(values):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Element at index {i} is not numeric: {type(val)}")
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
