#!/usr/bin/env python3
"""Module that defines a function to compute lengths of elements in an
iterable."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Compute the length of each element in an iterable.

    Args:
        lst (Iterable[Sequence]): an iterable containing sequences.

    Returns:
        List[Tuple[Sequence, int]]: a list of tuples, each containing the
        original element and its length.
    """
    return [(i, len(i)) for i in lst]
