#!/usr/bin/env python3
"""Module that defines a function to safely get a value from a mapping."""
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Safely get a value from a mapping given a key.

    Args:
        dct (Mapping): the mapping to search in.
        key (Any): the key to look up in the mapping.
        default (Union[T, None]): the value to return if key is not
            found in dct. Defaults to None.

    Returns:
        Union[Any, T]: the value associated with key if found, otherwise
        default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
