#!/usr/bin/env python3

from collections.abc import Callable

def mage_counter() -> Callable:
    tracker = 0
    def counter() -> int:
        nonlocal tracker
        tracker += 1
        return tracker
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power
    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def apply(item:str) -> str:
        return f"{enchantment_type} {item}"

    return apply


def memory_vault() -> dict[str, Callable]:
    memory = {}

    def store(key: str, value) -> None:
       memory[key] = value

    def recall(key: str):
        return memory.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


def main():
    print("Testing mage counter:")
    counter_a = mage_counter()
    for call_num in range(1, 3):
        print(f"counter_a call: {call_num}: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")
    print()
    spell_acc = spell_accumulator(100)
    print("Testing spell accumulator:")
    print(f"Base 100, add 20: {spell_acc(20)}")
    print(f"Base 100, add 30: {spell_acc(30)}")
    print()
    flame_enchant = enchantment_factory("Flaming")
    frost_enchant = enchantment_factory("Frozen")
    print(flame_enchant("Sword"))
    print(frost_enchant("Shield"))
    store_mem = memory_vault()
    print(store_mem('secret', 42))
    
main()