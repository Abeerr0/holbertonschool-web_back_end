#!/usr/bin/env python3
"""Module that defines a function to safely get the first element of a
sequence."""
from typing import Any, Optional, Sequence


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """Safely return the first element of a sequence.

    Args:
        lst (Sequence[Any]): a sequence containing elements of any type.

    Returns:
        Optional[Any]: the first element of lst if it is not empty,
        otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
