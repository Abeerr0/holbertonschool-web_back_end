#!/usr/bin/env python3
"""Module that defines a function returning a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier (float): the value to multiply by.

    Returns:
        Callable[[float], float]: a function that takes a float and
        returns it multiplied by multiplier.
    """
    def multiplier_function(value: float) -> float:
        """Multiply value by the outer multiplier."""
        return value * multiplier

    return multiplier_function
