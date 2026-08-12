"""
mathlib.f01_add - Addition utilities
=====================================

This module provides addition operations for scalars and sequences of numbers.
It supports integers, floats, and any numeric type that supports the ``+``
operator.  All public functions are fully type-annotated and include doctest
examples that can be executed with ``python -m doctest f01_add.py -v``.

Functions
---------
add(a, b)
    Return the sum of two scalar numbers.
add_many(*args)
    Return the sum of an arbitrary number of scalar values.
cumulative_sum(values)
    Return a list of running totals for a sequence of numbers.
"""

from __future__ import annotations

from typing import Sequence, Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the arithmetic sum of *a* and *b*.

    Parameters
    ----------
    a:
        First operand.
    b:
        Second operand.

    Returns
    -------
    Number
        ``a + b``.

    Raises
    ------
    TypeError
        If either argument is not a numeric type.

    Examples
    --------
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0.1, 0.2)  # doctest: +ELLIPSIS
    0.30000000000000...
    >>> add(1_000_000, 2_000_000)
    3000000
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numeric; got {type(a)} and {type(b)}")
    return a + b


def add_many(*args: Number) -> Number:
    """Return the sum of all positional arguments.

    At least one argument must be supplied.

    Parameters
    ----------
    *args:
        Variable-length list of numbers to add together.

    Returns
    -------
    Number
        The total sum of all supplied values.

    Raises
    ------
    ValueError
        If no arguments are provided.
    TypeError
        If any argument is not numeric.

    Examples
    --------
    >>> add_many(1, 2, 3)
    6
    >>> add_many(10)
    10
    >>> add_many(1.5, 2.5, 3.0)
    7.0
    >>> add_many(-5, 5, -5, 5)
    0
    """
    if not args:
        raise ValueError("add_many requires at least one argument")
    for i, val in enumerate(args):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Argument at index {i} is not numeric: {type(val)}")
    return sum(args)


def cumulative_sum(values: Sequence[Number]) -> list[Number]:
    """Return the running (prefix) sum of *values*.

    Each element ``result[i]`` equals ``sum(values[:i+1])``.

    Parameters
    ----------
    values:
        A non-empty sequence of numbers.

    Returns
    -------
    list[Number]
        A list of the same length as *values* containing running totals.

    Raises
    ------
    ValueError
        If *values* is empty.
    TypeError
        If any element of *values* is not numeric.

    Examples
    --------
    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> cumulative_sum([10, -3, 5])
    [10, 7, 12]
    >>> cumulative_sum([0.5, 0.5, 1.0])
    [0.5, 1.0, 2.0]
    >>> cumulative_sum([42])
    [42]
    """
    if not values:
        raise ValueError("cumulative_sum requires a non-empty sequence")
    result: list[Number] = []
    running: Number = 0
    for i, val in enumerate(values):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Element at index {i} is not numeric: {type(val)}")
        running = running + val
        result.append(running)
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
