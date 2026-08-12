"""mathlib — a small Python utility library for arithmetic and statistics.

Modules:
    add       -- addition
    subtract  -- subtraction
    multiply  -- multiplication
    divide    -- division
    stats     -- mean, median, variance
"""

from mathlib.add import add
from mathlib.subtract import subtract
from mathlib.multiply import multiply
from mathlib.divide import divide
from mathlib.stats import mean, median, variance

__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "mean",
    "median",
    "variance",
]
