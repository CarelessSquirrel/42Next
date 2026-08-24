#!/usr/bin/env python3

from collections.abc import Callable

test_values = [5, 10, 16]

test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


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
    return combined


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
    return checked


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return cast


def main() -> None:
    target = test_targets[0]
    power = test_values[1]
    print("spell combiner:")
    combo = spell_combiner(heal, burn)
    print(combo(target, power))
    print()
    mega_comet = power_amplifier(comet, 3)
    print("amplifier:")
    print(mega_comet(target, power))
    print()

    def strong_enough(target: str, power: int) -> bool:
        return power >= 10

    guarded = conditional_caster(strong_enough, fear)
    print("conditional cast:")
    print(guarded(target, power))
    print(guarded(target, 5))
    print()
    sequence = spell_sequence([heal, burn, fear, comet])
    print("spell sequence:")
    print(sequence(target, power))


if __name__ == '__main__':
    main()
