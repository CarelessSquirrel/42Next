#!/usr/bin/env python3
import functools
from collections.abc import Callable
from typing import Any
import operator


operation_map = {
    'add': operator.add,
    'multiply': operator.mul,
    'max': max,
    'min': min,
}

def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation not operation_map:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(operation_map[operation], spells)




def partial_enchancer(base_enchantment: Callable) -> dict[str, Callable]:
    ...


def memoized_fibonacci(n: int) -> int:
    ...


def spell_dispatcher() -> Callable[[Any], str]:
    ...