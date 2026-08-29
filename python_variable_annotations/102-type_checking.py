#!/usr/bin/env python3
"""Module that defines a function to zoom into an array."""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Zoom into a tuple by repeating each element factor times.

    Args:
        lst (Tuple): the tuple of items to zoom into.
        factor (int): the number of times to repeat each item.
            Defaults to 2.

    Returns:
        List: a list with each item repeated factor times.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
