#!/usr/bin/env python3
"""Module that defines a function to sum a mixed list of int and float."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sum all elements in a list containing int and float values.

    Args:
        mxd_lst (List[Union[int, float]]): list of int/float numbers.

    Returns:
        float: the sum of all elements in the list.
    """
    return float(sum(mxd_lst))
