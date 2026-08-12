"""
mathlib.f07_mean - Arithmetic and weighted mean utilities.

Provides arithmetic mean, geometric mean, harmonic mean, and weighted mean
with full type annotations.
All public functions include doctest examples that can be run with:

    python -m doctest mathlib/f07_mean.py -v

Functions
---------
mean(values)
    Return the arithmetic mean of an iterable.
geometric_mean(values)
    Return the geometric mean of a sequence of positive numbers.
harmonic_mean(values)
    Return the harmonic mean of a sequence of positive numbers.
weighted_mean(values, weights)
    Return the weighted arithmetic mean of paired values and weights.
"""

from __future__ import annotations

import math
from typing import Sequence, Union

Number = Union[int, float]


def mean(values: Sequence[Number]) -> float:
    """Return the arithmetic mean of *values*.

    Parameters
    ----------
    values : sequence of int or float
        A non-empty sequence of numeric values.

    Returns
    -------
    float
        ``sum(values) / len(values)``.

    Raises
    ------
    ValueError
        If *values* is empty.

    Examples
    --------
    >>> mean([1, 2, 3, 4, 5])
    3.0
    >>> mean([10, 20])
    15.0
    >>> mean([7])
    7.0
    >>> mean([-2, 0, 2])
    0.0
    """
    if len(values) == 0:
        raise ValueError("mean requires at least one value")
    return sum(values) / len(values)


def geometric_mean(values: Sequence[Number]) -> float:
    """Return the geometric mean of *values*.

    Computed as ``(v1 * v2 * ... * vn) ** (1/n)``.  All values must be
    strictly positive.

    Parameters
    ----------
    values : sequence of int or float
        A non-empty sequence of positive numbers.

    Returns
    -------
    float
        The n-th root of the product of *values*.

    Raises
    ------
    ValueError
        If *values* is empty or contains a non-positive number.

    Examples
    --------
    >>> geometric_mean([1, 4])
    2.0
    >>> abs(geometric_mean([2, 8]) - 4.0) < 1e-9
    True
    >>> geometric_mean([1])
    1.0
    >>> abs(geometric_mean([1, 2, 4]) - 2.0) < 1e-9
    True
    """
    if len(values) == 0:
        raise ValueError("geometric_mean requires at least one value")
    for v in values:
        if v <= 0:
            raise ValueError("geometric_mean requires strictly positive values")
    log_sum = sum(math.log(v) for v in values)
    return math.exp(log_sum / len(values))


def harmonic_mean(values: Sequence[Number]) -> float:
    """Return the harmonic mean of *values*.

    Computed as ``n / (1/v1 + 1/v2 + ... + 1/vn)``.  All values must be
    strictly positive.

    Parameters
    ----------
    values : sequence of int or float
        A non-empty sequence of positive numbers.

    Returns
    -------
    float
        ``len(values) / sum(1/v for v in values)``.

    Raises
    ------
    ValueError
        If *values* is empty or contains a non-positive number.

    Examples
    --------
    >>> harmonic_mean([1, 1])
    1.0
    >>> harmonic_mean([1, 2])
    1.3333333333333333
    >>> harmonic_mean([4])
    4.0
    >>> abs(harmonic_mean([2, 3, 6]) - 3.0) < 1e-9
    True
    """
    if len(values) == 0:
        raise ValueError("harmonic_mean requires at least one value")
    for v in values:
        if v <= 0:
            raise ValueError("harmonic_mean requires strictly positive values")
    return len(values) / sum(1.0 / v for v in values)


def weighted_mean(values: Sequence[Number], weights: Sequence[Number]) -> float:
    """Return the weighted arithmetic mean of *values* with given *weights*.

    Parameters
    ----------
    values : sequence of int or float
        Data values.
    weights : sequence of int or float
        Non-negative weights corresponding to each value.  Must have the same
        length as *values*.  The sum of weights must be non-zero.

    Returns
    -------
    float
        ``sum(v * w for v, w in zip(values, weights)) / sum(weights)``.

    Raises
    ------
    ValueError
        If *values* and *weights* differ in length, are both empty, or
        weights sum to zero.

    Examples
    --------
    >>> weighted_mean([1, 2, 3], [1, 1, 1])
    2.0
    >>> weighted_mean([0, 10], [9, 1])
    1.0
    >>> weighted_mean([5], [3])
    5.0
    >>> weighted_mean([1, 2], [0, 1])
    2.0
    """
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    if len(values) == 0:
        raise ValueError("weighted_mean requires at least one value")
    total_weight = sum(weights)
    if total_weight == 0:
        raise ValueError("sum of weights must not be zero")
    return sum(v * w for v, w in zip(values, weights)) / total_weight
