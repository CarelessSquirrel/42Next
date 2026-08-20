#!/usr/bin/env python3

from collections.abc import Callable

def mage_counter() -> Callable:
    tracker = 0
    def counter() -> int:
        nonlocal tracker
        tracker += 1
        return tracker
    return counter


def main():
    print("Testing mage counter:")
    counter_a = mage_counter()
    for call_num in range(1, 3):
        print(f"counter_a call: {call_num}: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

main()