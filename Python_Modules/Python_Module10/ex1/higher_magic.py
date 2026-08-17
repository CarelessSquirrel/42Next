#!/usr/bin/env python3

from collections.abc import Callable

test_values = [5, 10, 16]

test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def spell(target: str, power: int) -> str:
    ...


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def burn(target: str, power: int) -> str:
    return f"Burn burns {target} for {power} HP"


def fear(target: str, power: int) -> str:
    return f"Fear incapacitates {target} for {power} seconds"


def comet(target: str, power: int) -> str:
    return f"Comet hits {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        amped_power = power * multiplier
        return base_spell(target, amped_power)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def checked(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        else:
            return "Spell fizzled"


def spell_sequence(spells: list[Callable]) -> Callable:
    ...
