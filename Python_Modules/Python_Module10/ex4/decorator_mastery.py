#!/usr/bin/env python3

import functools
from collections.abc import Callable
import time

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        ...

    def cast_spell(self, spell_name: str, power: int) -> str:
        ...

def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed} seconds")
        return result
    return wrapper

def power_validator(min_power: int) -> Callable:
    ...


def retry_spell(max_attempts: int) -> Callable:
    ...

def main() -> None:
    timer = spell_timer()

main()
