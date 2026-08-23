#!/usr/bin/env python3
import functools
from collections.abc import Callable
from typing import Any
import operator

spells = [10, 20, 30]

operation_map = {
    'add': operator.add,
    'multiply': operator.mul,
    'max': max,
    'min': min,
}

def enchant(power: int, element: str, target: str) -> str:
    return f"{element} enchantment ({power}) applied to {target}"


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0
    if operation not in operation_map:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(operation_map[operation], spells)



def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        'fire': functools.partial(base_enchantment, power=50, element='fire'),
        'ice': functools.partial(base_enchantment, power=50, element='ice'),
        'lightning': functools.partial(base_enchantment, power=50, element='lightning'),
    }


def memoized_fibonacci(n: int) -> int:
    ...


def spell_dispatcher() -> Callable[[Any], str]:
    ...

def main():
    sr = spell_reducer(spells, "add")
    print(sr)
    enchanters = partial_enchanter(enchant)
    print(enchanters['fire'](target='Sword'))
main()