#!/usr/bin/env python3
artifacts = [
    {'name': 'Wind Cloak', 'power': 74, 'type': 'focus'},
    {'name': 'Ice Wand', 'power': 64, 'type': 'relic'},
    {'name': 'Light Prism', 'power': 108, 'type': 'armor'},
    {'name': 'Lightning Rod', 'power': 106, 'type': 'armor'}
]

mages = [
    {'name': 'Kai', 'power': 62, 'element': 'fire'},
    {'name': 'Luna', 'power': 80, 'element': 'fire'},
    {'name': 'Phoenix', 'power': 65, 'element': 'lightning'},
    {'name': 'Riley', 'power': 75, 'element': 'fire'},
    {'name': 'Riley', 'power': 50, 'element': 'water'}
]

spells = ['meteor', 'freeze', 'earthquake', 'flash']

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    descending = sorted(artifacts, key=lambda a: a['power'], reverse=True)
    return descending


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered = list(filter(lambda x: x['power'] >= min_power, mages))
    return filtered


def spell_transformer(spells: list[str]) -> list[str]:
    transformed = list(map(lambda x: "* " + x + " *", spells))
    return transformed

def main() -> None:
    sa = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    print(f"{sa[0]['name']} ({sa[0]['power']} power) comes before {sa[1]['name']} ({sa[1]['power']} power)")
    fm = power_filter(mages,40)
    print("Filtering mages who have more than the mininum amount power")
    for mage in fm:
        print(f"{mage['name']} ({mage['power']} power)")
    ts = spell_transformer(spells)
    print(" ".join(ts))
main()