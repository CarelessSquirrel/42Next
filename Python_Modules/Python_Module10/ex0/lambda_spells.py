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
    filtered = list(filter(lambda m: m['power'] >= min_power, mages))
    return filtered


def spell_transformer(spells: list[str]) -> list[str]:
    transformed = list(map(lambda s: "* " + s + " *", spells))
    return transformed


def mage_stats(mages: list[dict]) -> dict:
    ranked_max = max(mages, key=lambda m: m['power'])['power']
    ranked_min = min(mages, key=lambda m: m['power'])['power']
    ranked_avg = round(sum(map(lambda a: a['power'], mages)) / len(mages), 2)
    return {
        'max_power': ranked_max,
        'min_power': ranked_min,
        'avg_power': ranked_avg,
    }

def main() -> None:
    print("Lambda Sanctum")
    print("=" * 40)
    sa = artifact_sorter(artifacts)
    print("Testing artifact sorter:")
    print(f"{sa[0]['name']} ({sa[0]['power']} power) comes before {sa[1]['name']} ({sa[1]['power']} power)\n")
    fm = power_filter(mages,40)
    print("Filtering mages who have more than the mininum amount power:")
    for mage in fm:
        print(f"{mage['name']} ({mage['power']} power)")
    print()
    ts = spell_transformer(spells)
    print("Testing spell transformation:")
    print(" ".join(ts))
    print()
    rm = mage_stats(mages)
    print("Printing mage stats:")
    print(f"Max power: {rm['max_power']}")
    print(f"Min power: {rm['min_power']}")
    print(f"Average power: {rm['avg_power']}")
main()