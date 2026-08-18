#!/usr/bin/env python3

from collections.abc import Callable

def mage_counter() -> Callable:
    tracker = 0
    def counter() -> int:
        nonlocal tracker
        tracker += 1
    counter()
    return tracker

mage_counter()
mage_counter()
print(mage_counter())
