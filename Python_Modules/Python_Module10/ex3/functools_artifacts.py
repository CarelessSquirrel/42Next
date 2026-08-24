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

@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @functools.singledispatch
    def cast(spell: Any) -> str:
        return "Unknown spell type"

    @cast.register(int)
    def _(spell: int) -> str:
        return f"{spell} damage"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast: {len(spell) spells}"

    return cast

def main():
    sr = spell_reducer(spells, "add")
    print(sr)
    enchanters = partial_enchanter(enchant)
    print(enchanters['fire'](target='Sword'))
    print(enchanters['lightning'](target='Hammer'))
    print(enchanters['ice'](target='Staff'))
    fib = memoized_fibonacci(0)
    print(fib)
    fib = memoized_fibonacci(1)
    print(fib)
    fib = memoized_fibonacci(10)
    print(fib)
    fib = memoized_fibonacci(15)
    print(fib)
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher('fireball'))
    print(dispatcher([1, 2, 3]))
    print(dispatcher(4.2))

main()