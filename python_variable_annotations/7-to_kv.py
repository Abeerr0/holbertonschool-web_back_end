#!/usr/bin/env python3
"""Module that defines a function to convert a string and number to a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Create a tuple from a string and the square of a number.

    Args:
        k (str): the key/string value.
        v (Union[int, float]): a number (int or float) to be squared.

    Returns:
        Tuple[str, float]: a tuple containing k and the square of v as a
        float.
    """
    return (k, float(v ** 2))
