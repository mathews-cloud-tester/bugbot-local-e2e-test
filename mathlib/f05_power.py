"""
mathlib.f05_power - Exponentiation utilities.

Provides power, modular exponentiation, and repeated-squaring helpers with
full type annotations.
All public functions include doctest examples that can be run with:

    python -m doctest mathlib/f05_power.py -v

Functions
---------
power(base, exp)
    Return *base* raised to the *exp* power.
power_mod(base, exp, mod)
    Return (*base** **exp*) % *mod* using fast modular exponentiation.
integer_power(base, exp)
    Return *base** **exp* for non-negative integer exponents using
    repeated squaring.
"""

from __future__ import annotations

from typing import Union

Number = Union[int, float]


def power(base: Number, exp: Number) -> Number:
    """Return *base* raised to the power *exp*.

    Parameters
    ----------
    base : int or float
        The base value.
    exp : int or float
        The exponent.  May be negative or fractional.

    Returns
    -------
    int or float
        ``base ** exp``.

    Examples
    --------
    >>> power(2, 10)
    1024
    >>> power(3, 0)
    1
    >>> power(2, -1)
    0.5
    >>> power(9, 0.5)
    3.0
    """
    return base ** exp


def power_mod(base: int, exp: int, mod: int) -> int:
    """Return (*base* ** *exp*) modulo *mod*.

    Uses Python's built-in three-argument ``pow`` which internally applies
    fast modular exponentiation (right-to-left binary method), making it
    efficient for large exponents.

    Parameters
    ----------
    base : int
        The base value.
    exp : int
        The exponent.  Must be non-negative.
    mod : int
        The modulus.  Must be a positive integer.

    Returns
    -------
    int
        ``(base ** exp) % mod``.

    Raises
    ------
    ValueError
        If *mod* is not a positive integer or *exp* is negative.

    Examples
    --------
    >>> power_mod(2, 10, 1000)
    24
    >>> power_mod(3, 3, 7)
    6
    >>> power_mod(5, 0, 13)
    1
    >>> power_mod(2, 100, 1000000007)
    976371285
    """
    if mod <= 0:
        raise ValueError("mod must be a positive integer")
    if exp < 0:
        raise ValueError("exp must be non-negative for modular exponentiation")
    return pow(base, exp, mod)


def integer_power(base: int, exp: int) -> int:
    """Return *base* ** *exp* for non-negative integer exponents.

    Implements repeated squaring (exponentiation by squaring) without
    delegating to the built-in ``**`` operator, illustrating the algorithm.

    Parameters
    ----------
    base : int
        The base value.
    exp : int
        The exponent.  Must be >= 0.

    Returns
    -------
    int
        ``base ** exp``.

    Raises
    ------
    ValueError
        If *exp* is negative.

    Examples
    --------
    >>> integer_power(2, 8)
    256
    >>> integer_power(5, 3)
    125
    >>> integer_power(7, 0)
    1
    >>> integer_power(1, 1000)
    1
    """
    if exp < 0:
        raise ValueError("exp must be non-negative")
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2
    return result
