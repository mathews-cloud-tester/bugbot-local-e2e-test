"""
mathlib.f03_multiply - Multiplication utilities
================================================

This module provides multiplication operations for scalars and sequences of
numbers.  It supports integers, floats, and any numeric type compatible with
the ``*`` operator.  All public functions are fully type-annotated and include
doctest examples.

Functions
---------
multiply(a, b)
    Return the product of two scalar numbers.
multiply_many(*args)
    Return the product of an arbitrary number of scalar values.
running_product(values)
    Return a list of cumulative products for a sequence of numbers.
scale(values, factor)
    Return a new list with every element multiplied by *factor*.
"""

from __future__ import annotations

from typing import Sequence, Union

Number = Union[int, float]


def multiply(a: Number, b: Number) -> Number:
    """Return the arithmetic product ``a * b``.

    Parameters
    ----------
    a:
        First factor.
    b:
        Second factor.

    Returns
    -------
    Number
        ``a * b``.

    Raises
    ------
    TypeError
        If either argument is not numeric.

    Examples
    --------
    >>> multiply(3, 4)
    12
    >>> multiply(-2, 5)
    -10
    >>> multiply(0, 999)
    0
    >>> multiply(1.5, 2.0)
    3.0
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Both arguments must be numeric; got {type(a)} and {type(b)}")
    return a * b


def multiply_many(*args: Number) -> Number:
    """Return the product of all positional arguments.

    At least one argument must be supplied.  With a single argument the value
    itself is returned.

    Parameters
    ----------
    *args:
        Variable-length list of numbers.

    Returns
    -------
    Number
        The total product of all supplied values.

    Raises
    ------
    ValueError
        If no arguments are provided.
    TypeError
        If any argument is not numeric.

    Examples
    --------
    >>> multiply_many(2, 3, 4)
    24
    >>> multiply_many(7)
    7
    >>> multiply_many(-1, -1, -1)
    -1
    >>> multiply_many(0.5, 4.0, 2.0)
    4.0
    """
    if not args:
        raise ValueError("multiply_many requires at least one argument")
    for i, val in enumerate(args):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Argument at index {i} is not numeric: {type(val)}")
    result: Number = 1
    for val in args:
        result = result * val
    return result


def running_product(values: Sequence[Number]) -> list[Number]:
    """Return the cumulative (prefix) product of *values*.

    Each element ``result[i]`` equals ``product(values[:i+1])``.

    Parameters
    ----------
    values:
        A non-empty sequence of numbers.

    Returns
    -------
    list[Number]
        A list of the same length as *values* containing running products.

    Raises
    ------
    ValueError
        If *values* is empty.
    TypeError
        If any element is not numeric.

    Examples
    --------
    >>> running_product([1, 2, 3, 4])
    [1, 2, 6, 24]
    >>> running_product([2, 2, 2, 2])
    [2, 4, 8, 16]
    >>> running_product([5])
    [5]
    >>> running_product([1, -1, 2])
    [1, -1, -2]
    """
    if not values:
        raise ValueError("running_product requires a non-empty sequence")
    result: list[Number] = []
    running: Number = 1
    for i, val in enumerate(values):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Element at index {i} is not numeric: {type(val)}")
        running = running * val
        result.append(running)
    return result


def scale(values: Sequence[Number], factor: Number) -> list[Number]:
    """Return a new list with every element of *values* multiplied by *factor*.

    Parameters
    ----------
    values:
        A sequence of numbers to scale.
    factor:
        The scalar multiplier applied to each element.

    Returns
    -------
    list[Number]
        A new list of the same length as *values*.

    Raises
    ------
    TypeError
        If *factor* or any element of *values* is not numeric.

    Examples
    --------
    >>> scale([1, 2, 3], 3)
    [3, 6, 9]
    >>> scale([10, 20], 0.5)
    [5.0, 10.0]
    >>> scale([], 5)
    []
    >>> scale([-1, 0, 1], -2)
    [2, 0, -2]
    """
    if not isinstance(factor, (int, float)):
        raise TypeError(f"factor must be numeric; got {type(factor)}")
    for i, val in enumerate(values):
        if not isinstance(val, (int, float)):
            raise TypeError(f"Element at index {i} is not numeric: {type(val)}")
    return [val * factor for val in values]


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
