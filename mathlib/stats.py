"""Basic statistical operations for the mathlib utility library."""

from typing import Sequence


def mean(values: Sequence[float]) -> float:
    """Return the arithmetic mean of *values*.

    Raises:
        ValueError: If *values* is empty.
    """
    if not values:
        raise ValueError("mean requires at least one value")
    return sum(values) / len(values)


def median(values: Sequence[float]) -> float:
    """Return the median of *values*.

    Raises:
        ValueError: If *values* is empty.
    """
    if not values:
        raise ValueError("median requires at least one value")
    sorted_vals = sorted(values)
    mid = len(sorted_vals) // 2
    if len(sorted_vals) % 2 == 0:
        return (sorted_vals[mid - 1] + sorted_vals[mid]) / 2
    return sorted_vals[mid]


def variance(values: Sequence[float]) -> float:
    """Return the population variance of *values*.

    Raises:
        ValueError: If *values* has fewer than two elements.
    """
    if len(values) < 2:
        raise ValueError("variance requires at least two values")
    m = mean(values)
    return sum((x - m) ** 2 for x in values) / len(values)
