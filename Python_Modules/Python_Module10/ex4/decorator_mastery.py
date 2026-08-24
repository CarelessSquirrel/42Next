#!/usr/bin/env python3

import functools
from collections.abc import Callable
import time

class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and all(c.isalpha() or c == ' ' for c in name)


    def cast_spell(self, spell_name: str, power: int) -> str:
        ...


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


@spell_timer
def fireball(target: str, power: int) -> str:
    time.sleep(0.1)
    return f"Fireball hits {target} for {power} damage"


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            power = kwargs.get('power', args[-1] if args else None)
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


@power_validator(10)
def lightning_bolt(target: str, power: int) -> str:
    return f"Lighting bolt strikes {target} for {power} damage"


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(f"Spell failed, retrying.. (attempt {attempt}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


@retry_spell(3)
def failing_spell(target: str, power: int) -> str:
    raise RuntimeError("This spell always fails")


def make_halfway_spell() -> Callable:
    attempts = 0
    @retry_spell(3)
    def halfway_spell(target: str, power: int) -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise ValueError("Spell fizzled unexpectedly")
        return f"Halfway spell finally hits {target} for {power} damage"
    return halfway_spell


def main() -> None:
    print(fireball('dragon', 15))
    print('=' * 40)
    print(lightning_bolt('dragon', 5))
    print(lightning_bolt('dragon', 15))
    print('=' * 40)
    print(failing_spell('dragon', 15))
    print('=' * 40)
    hway = make_halfway_spell()
    print(hway('dragon', 15))


if __name__ == '__main__':
    main()
